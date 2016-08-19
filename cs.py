# coding: utf8
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time,re,sys
from selenium.webdriver.common.keys import Keys

# How to use this file: look for "/!\" or "WARNING" in this file to find where the code has to be customized
# and where it has to be un-commented (for safety reasons)			(c) bixiou & bubu		free licence








########## FILL THIS SECTION ##########


## You and your trip
login = "adrifaoudai2@hotmail.com"  # replace identifiers by own
password = "hackhack"

location="Ubud, Indonesia"  #Specify both city and country to avoid confusion

arrival_date = "2017-06-13" # yyyy-mm-dd
departure_date="2018-06-13"  # both needed please
is_flexible_arrival = "Y" # ("Y"/"N")
is_flexible_departure = "Y" #  ("Y"/"N")


number_of_travellers="1"

## Your potential hosts
nb_users = 3  # How many people do you want to spam?

gender="All"  #in ["Male", "Female", "Other", "All"]
min_age="18"  # empty string if no restriction. Min(min_age) is 18
max_age="100" # empty string if no restriction.
restrict_research_by_dates= "N"           # ("Y"/"N")



########################################


print("start")

def wait_for(element):
    def is_here(elem):
        try:
            elem
        except:
            return False
        return True
    while not is_here(element):
        time.sleep(.2)
    return

while not gender in ["Male", "Female", "Other", "All"]:
    gender=raw_input("Please select correct gender (['Male', 'Female', 'Other', 'All']) :")

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chromeOptions)

def loginCS(driver):
    driver.implicitly_wait(100)
    driver.get("https://www.couchsurfing.org/n/places/paris-ile-de-france-france")
    #TODO: definir proprement time.sleep(), ie attendre que la page ait charge
    wait_for(driver.find_element_by_id('user_login'))
    driver.find_element_by_id('user_login').send_keys(login)
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_name("commit").click()


def write(id, name):

    def writeMessage(name):
        # WARNING: "I am Adrien" below /!\
        #TODO: ameliorer le message
        message = "Hello " + name + ", \n I am Adrien, currently traveling on my own in your beautiful country, and I'd like to stay at your place a couple of days: you seem really cool. I've already surfed and hosted dozens of times and I love CS, it's always been great experiences! \nCheers!"
        print(message)
        return message

    user_url = "https://www.couchsurfing.com/couch_visits/new?cs_new_fe=true&to_id=" + str(id)
    driver.get(user_url)
    if is_flexible_arrival != "N":
        driver.find_element_by_name('departure_flexible').click()
    if is_flexible_arrival != "N":
        driver.find_element_by_name('arrival_flexible').click()
    driver.find_element_by_name('arrival').send_keys(arrival_date)
    driver.find_element_by_name('departure').send_keys(departure_date)
    driver.find_element_by_name('number_of_guests').clear()
    driver.find_element_by_name('number_of_guests').send_keys(number_of_travellers)
    driver.find_element_by_name('body').send_keys(writeMessage(name))
    time.sleep(2)
#	driver.find_element_by_name('status').click()
#   WARNING !!!    uncomment to actually send messages
    return


def research():
    #research city url from homepage
    wait_for(driver.find_element_by_css_selector("div.selectize-input.items.has-options.full.has-items"))
    driver.find_element_by_css_selector("div.selectize-input.items.has-options.full.has-items").click()
    wait_for(driver.find_element_by_css_selector("fieldset.mod-inline-block-web div[data-value='host']"))
    driver.find_element_by_css_selector("fieldset.mod-inline-block-web div[data-value='host']").click()
    wait_for(driver.find_element_by_css_selector(
        "div.header-search div[data-search-query-container] div.selectize-input.items.not-full input"))
    driver.find_element_by_css_selector(
        "div.header-search div[data-search-query-container] div.selectize-input.items.not-full input").send_keys(
        location)
    wait_for(driver.find_element_by_css_selector("button[title='Search']").click())
    driver.find_element_by_css_selector("button[title='Search']").click()

    #adjust url for research parameters
    wait_for(driver.find_elements_by_css_selector("div.box-content div.card.mod-user a.mod-black"))
    url = driver.current_url
    url += "&perPage=" + str(
        nb_users) + "&min_age=" + min_age + "&max_age=" + max_age + "&num_guests=" + number_of_travellers
    if restrict_research_by_dates == "Y":
        url += "&arrival_date=" + str(arrival_date) + "&departure_date=" + str(departure_date)
    driver.get(url)
    return


def users_info():
    users = []
    time.sleep(3)
    for element in driver.find_elements_by_css_selector("div.box-content div.card.mod-user a.mod-black"):
        users.append({"id": element.get_attribute("href").replace("https://www.couchsurfing.com/users/", ""),
                      "Surname": element.text.title().partition(' ')[0]})
    return users



loginCS(driver)

research()

users=users_info()
print users

# /!\ Before un-commenting the following lines, be sure you know what you are doing and check the number of users
#for host in users:
#    write(host['id'], host['Surname'])

