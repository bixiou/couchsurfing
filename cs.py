from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time,re,sys
from selenium.webdriver.common.keys import Keys

login = "adrifaoudai2@hotmail.com"
password = "hackhack"
url = "https://www.couchsurfing.com/members/hosts?latitude=45.764043&longitude=4.835659&search_query=Lyon&search_type=host"

# yyyy-mm-dd
arrival_date = "2017-06-13"
departure_date="2018-06-13"


message = "Hi!!! :))))))))))))qzmmoij"

 #Chrome Options
chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

def loginCS(driver):
	driver.implicitly_wait(100)
	driver.get("https://www.couchsurfing.org/n/places/paris-ile-de-france-france")
	time.sleep(1)
	driver.find_element_by_id('user_login').send_keys(login)
	driver.find_element_by_id('user_password').send_keys(password)
	driver.find_element_by_name("commit").click()

def writeMessage():
	return message
# Find users IDs

def write_to_user(user_url):
	driver.get(user_url)
	driver.find_element_by_name('arrival').send_keys(arrival_date)
	driver.find_element_by_name('departure').send_keys(departure_date)
	driver.find_element_by_name('body').send_keys(writeMessage())
	time.sleep(2)
	driver.find_element_by_name('status').click()
	return

loginCS(driver)
time.sleep(3)

driver.get(url)
print("go PARIS")

time.sleep(2)

users0 = []
users = []
for element in driver.find_elements_by_css_selector("a.mod-black"):
    users0.append(element.get_attribute("href"))
for el in users0:
	users.append(el.replace("users/","couch_visits/new?cs_new_fe=true&to_id="))

print(users[1])


write_to_user("https://www.couchsurfing.com/couch_visits/new?cs_new_fe=true&to_id=2559099")



# https://www.couchsurfing.com/users/2468753
# https://www.couchsurfing.com/couch_visits/new?cs_new_fe=true&to_id=2468753

# driver.get("https://www.couchsurfing.com/couch_visits/new?cs_new_fe=true&to_id=5378052")
# Send message

# envoyer requete a utilisateur 5378052:
# https://www.couchsurfing.com/couch_visits/new?cs_new_fe=true&to_id=5378052

# def mainProcess(username):
# 	loginFacebook(driver)

# if __name__ == '__main__':
# 	if len(sys.argv) <= 1:
# 		showhelp()
# 		driver.close()
# 		driver.quit
# 		conn.close()
# 		sys.exit()
#  	else:
# 		if len(facebook_username)<1 or len(facebook_password)<1:
# 			print "[*] Please fill in 'facebook_username' and 'facebook_password' before continuing."
# 			sys.exit()
#   		options(sys.argv)
