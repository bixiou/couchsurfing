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

# WARNING: replace identifiers by own
login = "adrifaoudai2@hotmail.com"
password = "hackhack"
# WARNING: choose how many potential hosts you want to spam
nb_users = 11
#TODO: verifier si les noms s'affichent bien en envoyant une requete au nom correspondant a l'id ci-dessous :
mon_id = 2004164630 #2559099 # Witvlei, Omaheke Region NAM 
# /!\ Adapter l'url au lieu et aux preferences pour les hotes
url = "https://www.couchsurfing.com/members/hosts/1?arrival_date=&button=&can_host%5Baccepting_guests%5D=1&can_host%5Bmaybe_accepting_guests%5D=1&country=&date_modal_dismissed=true&departure_date=&gender=All&has_references=1&host_sort=Best+Match&interests=&interests_stored=%5B%5D&join_date=Anytime&keyword=&languages_spoken=&languages_stored=%5B%5D&last_login=Anytime&latitude=45.764043&longitude=4.835659&max_age=35&min_age=18&num_guests=1&perPage=" + str(nb_users) + "&radius=10&region=&search_query=Lyon&smoking=No+Preference&utf8=%E2%9C%93"
arrival_date = "2017-06-13" # yyyy-mm-dd
departure_date="2018-06-13"

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chromeOptions)

def loginCS(driver):
	driver.implicitly_wait(100)
	driver.get("https://www.couchsurfing.org/n/places/paris-ile-de-france-france")
	#TODO: definir proprement time.sleep(), ie attendre que la page ait charge
	time.sleep(1)
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
	driver.find_element_by_name('arrival').send_keys(arrival_date)
	driver.find_element_by_name('departure').send_keys(departure_date)
	driver.find_element_by_name('body').send_keys(writeMessage(name))
	#TODO: selectionner Dates flexibles et "other nearby hosts can send me invitations"
	time.sleep(2)
	driver.find_element_by_name('status').click()
	return

loginCS(driver)
time.sleep(3)
driver.get(url)
time.sleep(15)

users = []
for element in driver.find_elements_by_css_selector("a.mod-black"):
    users.append({"id":element.get_attribute("href").replace("https://www.couchsurfing.com/users/",""),
    	"Surname":element.text.title().partition(' ')[0]})
# /!\ Before un-commenting the following lines, be sure you know what you are doing and check the number of users
# for host in users:
	# write(host['id'], host['Surname'])
write(mon_id, u'R\xe9mi')