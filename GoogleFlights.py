import time
from selenium.webdriver.common.keys import Keys

class GoogleFlightController:

    def __init__(self, driver):
        self.driver = driver


    def goToHome(self):
        self.driver.get("https://flights.google.com")
        time.sleep(2)

    def closeBrowser(self):
        self.driver.close()

    def setFrom(self, fromAirport):
        print("Setting FROM: "+fromAirport)
        inputElement = self.driver.find_element_by_xpath("//*[@id='i15']/div[1]/div/div/div[1]/div/div/input")
        inputElement.clear()
        for c in fromAirport:
            inputElement.send_keys(c)
            inputElement = self.driver.find_element_by_xpath("//*[@id='i15']/div[6]/div[2]/div[2]/div[1]/div/input")
            time.sleep(0.1)
        time.sleep(1)
        item = self.driver.find_element_by_xpath("//*[@data-code='"+fromAirport+"']")
        item.click()
        time.sleep(0.5)
    
    def setTo(self, toAirport):
        print("Setting TO: "+toAirport)
        inputElement = self.driver.find_element_by_xpath("//*[@id='i15']/div[4]/div/div/div[1]/div/div/input")
        inputElement.clear()
        for c in toAirport:
            inputElement.send_keys(c)
            inputElement = self.driver.find_element_by_xpath("//*[@id='i15']/div[6]/div[2]/div[2]/div[1]/div/input")
            time.sleep(0.1)
        time.sleep(1)
        item = self.driver.find_element_by_xpath("//*[@data-code='"+toAirport+"']")
        item.click()
        time.sleep(0.5)

    def setDates(self, departureDate, returnDate):
        print("Setting Departure Date: "+departureDate)
        calendar = self.driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")
        calendar.click()
        time.sleep(3)
        depDate = self.driver.find_element_by_xpath("//*[@id='ow62']/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input")
        depDate.send_keys(departureDate)
        time.sleep(0.5)

        retDate = self.driver.find_element_by_xpath("//*[@id='ow62']/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input")
        retDate.send_keys(Keys.CONTROL, 'a')
        retDate.send_keys(returnDate)
        time.sleep(0.5)

        concludeButton = self.driver.find_element_by_xpath("//*[@id='ow62']/div[2]/div/div[3]/div[3]/div/button")
        concludeButton.click()
        time.sleep(0.5)

    def searchFlights(self):
        searchButton = self.driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button")
        searchButton.click()
        time.sleep(5)