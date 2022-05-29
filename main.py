from selenium import webdriver
import os
import GoogleFlights
import config

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

googleFlight = GoogleFlights.GoogleFlightController(driver)
googleFlight.goToHome()
googleFlight.setFrom(config.fromAirport)
googleFlight.setTo(config.toAirport)
googleFlight.setDates(config.departureDate,config.returnDate)