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


########## FILL THIS SECTION + 'message' in the beginning of function write (l. 78) ##########


## You and your trip
my_name="Adrien"
login = "adrifaoudai2@hotmail.com" # replace identifiers by own
password = "hackhack"

location="Barcelona, Spain"  #Specify both city and country to avoid confusion

arrival_date = "2018-05-22" # yyyy-mm-dd
departure_date="2018-05-24"  # both needed please
is_flexible_arrival = "Y" # ("Y"/"N")
is_flexible_departure = "Y" #  ("Y"/"N")


number_of_travellers="1"

## Your potential hosts
nb_users = 20 # How many people do you want to spam?
# /!\ in order to make more than 20 requests (say n*20), the simplest is to make n requests with distinct age intervals

gender="All"  #in ["Male", "Female", "Other", "All"]
min_age="18"  # empty string if no restriction. Min(min_age) is 18
max_age="35" # empty string if no restriction.
restrict_research_by_dates= "N"           # ("Y"/"N")

########################################

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

# chromeOptions = webdriver.ChromeOptions()
# driver = webdriver.Chrome(chrome_options=chromeOptions)
# /!\ extract the .zip from https://sites.google.com/a/chromium.org/chromedriver/downloads and add the path below
driver = webdriver.Chrome(executable_path="./chromedriver")

def loginCS(driver):
    driver.implicitly_wait(100)
    driver.get("https://www.couchsurfing.org/n/places/paris-ile-de-france-france")
    #TODO: definir proprement time.sleep(), ie attendre que la page ait charge
    wait_for(driver.find_element_by_id('user_login'))
    driver.find_element_by_id('user_login').send_keys(login)
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_name("commit").click()


def write(id, name):

    message = "Bonjour " + name + "! Je serai à Strasbourg du 22 au 24 mai pour participer à une conférence de doctorants en économie. Tu m'as l'air sympa, et j'aimerais bien profiter de mes deux jours à Strasbourg pour faire ta connaissance. Est-ce que tu pourrais m'héberger ces deux nuits ? Mon train arrive à 20h30 le mardi, et je repars le jeudi soir (sauf si la grève m'oblige à partir le lendemain). Bien à toi."

#    user_url = "https://www.couchsurfing.com/couch_visits/new?cs_new_fe=true&to_id=" + str(id)
    user_url = "https://www.couchsurfing.com/" + str(id)
    driver.get(user_url)
    for el in driver.find_elements_by_css_selector("a.js-send-request"): #.replace("https://www.couchsurfing.com/", "") #
        message_url = el.get_attribute("href").replace("&type=inline", "")
    driver.get(message_url)
    new_person = True
    try:
        driver.find_element_by_name('number_of_guests') # or any CSS selector characteristic of this page
    except:
        new_person = False
    if new_person:
        if is_flexible_departure != "N":
            driver.find_element_by_name('departure_flexible').click()
        if is_flexible_arrival != "N":
            driver.find_element_by_name('arrival_flexible').click()

        driver.find_element_by_name('arrival').send_keys(arrival_date)
        driver.find_element_by_name('departure').send_keys(departure_date)
        # driver.find_element_by_name('number_of_guests').clear()
        # driver.find_element_by_name('number_of_guests').send_keys(number_of_travellers)
        driver.find_element_by_name('body').send_keys(message)
        time.sleep(15)
        driver.find_element_by_name('status').click()
        print(name)
# #   WARNING !!!    uncomment previous line to actually send messages
    else:
        print("already messaged")
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
    time.sleep(4)
    # for element in driver.find_elements_by_css_selector("div.box-content div.card.mod-user a.mod-black"):
    # for element in driver.find_elements_by_css_selector("div.host-results li.user-card a.user-card__content"):
    for element in driver.find_elements_by_css_selector("li.user-card a.user-card__profile-link"):
        users.append({"id": element.get_attribute("href").replace("https://www.couchsurfing.com/", ""),
                      "Surname": element.text.title().partition(' ')[0]})
    return users



loginCS(driver)

# research()
# or paste directly the URL (then comment l. 81 to 84 (right before sending the message and be careful with the number of results perPage)
wait_for(driver.find_element_by_css_selector("div.selectize-input.items.has-options.full.has-items"))
url = "https://www.couchsurfing.com/members/hosts?utf8=%E2%9C%93&search_query=&placeid=&latitude=48.5734053&longitude=7.7521113&country=france&region=europe&city=Strasbourg&date_modal_dismissed=true&arrival_date=2018-05-22&departure_date=2018-05-24&num_guests=1&can_host%5Baccepting_guests%5D=1&can_host%5Bmaybe_accepting_guests%5D=1&last_login=2&join_date=0&gender=0&min_age=&max_age=30&languages_spoken=&interests=&smoking=0&radius=5&keyword=&host_sort=0&button="
driver.get(url)

users=users_info()
print(users)

# /!\ Before un-commenting the following lines, be sure you know what you are doing and check the number of users
for host in users:
    # already_messaged = driver.find_elements_by_css_selector("ul.cs-thread-messages")
    # if not already_messaged:
    if (host['Surname'] != "Verified"):
        write(host['id'], host['Surname'])
        time.sleep(50) # so as to not be catched


