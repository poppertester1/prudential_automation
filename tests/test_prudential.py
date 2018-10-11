# _*_ coding: utf-8 _*_
__author__ = "Karunakar"

from all_imports import *
url = 'https://openweathermap.org/'

'''
    INTRO: Using TestCase from the unittest which allows us to write tests as each test case and can also be linked to the individual manual test cases which helps in simplifying the test execution, maintainace, coverage, reporting and pointing at the area of the bugs.
    - Added pytest for setting up sequence of test execution
    - set to chrome browser latest 69 version which is using latest chromedriver 42
'''


class TestOpenWeatherMap(unittest.TestCase):
    def setUp(self):
        # setup will run before every test
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.addCleanup(self.driver.quit)


    def is_element_present(self, what):
        # verify element is present or not
        try: self.driver.find_element(By.CLASS_NAME, value=what)
        except NoSuchElementException as e: return False
        return True
    
    
    @pytest.mark.run(order=1)
    def test_verify_open_weather_map_page(self):
        # task one, test to verify the open page is right and all the basic page objects are visible
        '''
            1     Write a first end-to-end test that
            1.1     Starts at https://openweathermap.org/- DONE
            1.2     Verifies that all important information is there, e.g.  labels etc. (Give it a thought for what is important to test) - DONE
        '''
        # verify page title to make sure that we have landed on the right page
        self.assertIn('Сurrent weather and forecast - OpenWeatherMap', self.driver.title)
        # verify logo element is visible
        assert True == self.is_element_present('navbar-brand')
        # verify search button is present
        assert True == self.is_element_present('btn-orange')
        # verify menu bar is present
        assert True == self.is_element_present('navbar-collapse')
        # verify footer is present
        assert True == self.is_element_present('footer-dark')
    
    @pytest.mark.run(order=2)
    def test_verify_invalid_city_search(self):
        # task two, test to verify that search for an invalid city displays the "Not Found" alert.
        '''
            2       Write a second end-to-end test that
            2.1       Starts on the https://openweathermap.org/
            2.2       Enters an invalid city name
            2.3       Searches for the weather
            2.4       Verifies that website suggests city is "Not found"
        '''
        invalid_city_name = "hsdasdajdasi"
        # add invalid city name in the search box
        self.driver.find_elements_by_id('q')[1].send_keys(invalid_city_name)
        # tap on search button
        self.driver.find_element_by_class_name("btn-orange").click()
        # verify results should be alert text Not found
        self.assertIn('Not found', self.driver.find_element_by_class_name("alert-warning").text.split('\n')[1])
    
    
    @pytest.mark.run(order=3)
    def test_verify_valid_city_search(self):
        # task three, test to verify that searching with an valid city display the result.
        '''
            3       Write a last end-to-end test that
            3.1       Starts on the https://openweathermap.org/
            3.2       Enters a valid city name
            3.3       Searches for the weather
            3.4       Verifies that website successfully returns weather details for the city.
        '''
        valid_city = "Pune"
        # add valid city name
        self.driver.find_elements_by_id('q')[1].send_keys(valid_city)
        # tap on search button
        self.driver.find_element_by_class_name("btn-orange").click()
        # verify that website successfully returns weather details for the city
        self.assertIn("Pune", self.driver.find_element_by_partial_link_text("Pune").text)
    
    
    @pytest.mark.run(order=4)
    def test_verify_view_current_location_after_performing_a_city_search(self):
        # task four, verify after searching for any city, tap on current location should redirect to current city page
        '''
            4       End-to-end test that
            4.1       Starts on the https://openweathermap.org/
            4.2       Enters a valid city name 
            4.3       Searches for the weather
            4.4       Verifies that viewing current location from the searched city page is redirecting to the current location
        '''
        current_city = self.driver.find_element_by_class_name("weather-widget__city-name").text.replace("Weather in ", '')
        valid_city = "Pune"
        # add valid city name
        self.driver.find_elements_by_id('q')[1].send_keys(valid_city)
        # tap on search button
        self.driver.find_element_by_class_name("btn-orange").click()
        # verify that website successfully returns weather details for searched the city
        self.assertIn("Pune", self.driver.find_element_by_partial_link_text("Pune").text)
        # tap on the searched city page
        self.driver.find_element_by_partial_link_text("Pune").click()
        # tap on current location
        self.driver.find_element_by_class_name("search-cities__lnk").click()
        # verify redirect to the current location is correct
        time.sleep(5)
        self.assertIn(current_city,self.driver.find_element_by_class_name("weather-widget__city-name").text.replace("Weather in ", ''))


    @pytest.mark.run(order=5)
    def test_verify_celsius_to_fahrenheit(self):
        # task five, verify that celsius to farenhait is converting correctly
        '''
            5       End-End test that
            5.1       Starts on the https://openweathermap.org/
            5.2       Verify that page shows celsius by default
            5.3       Change celsius to farenhait
            5.4       Verify that chaning to celsius to farenhait is working and is showing correct converted metrics
        '''
        #celsius = 37.5
        #fahrenheit = (celsius * 1.8) + 32
        time.sleep(2)
        current_celsius = float(self.driver.find_element_by_class_name('weather-widget__temperature').text.split(' ')[0])
        self.driver.find_element_by_id('imperial').click()
        time.sleep(2)
        current_fahrenheit = self.driver.find_element_by_class_name('weather-widget__temperature').text.split(' ')[0]
        assert float(current_fahrenheit) == float((current_celsius * 1.8) + 32)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
