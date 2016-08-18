from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time,re,sys
from selenium.webdriver.common.keys import Keys

login = "adrifaoudai2@hotmail.com"
password = "hackhack"
url = "https://www.couchsurfing.com/members/hosts?latitude=45.764043&longitude=4.835659&search_query=Lyon&search_type=host"

 #Chrome Options
chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

def loginFacebook(driver):
	driver.implicitly_wait(120)
	driver.get("https://www.facebook.com/")
	#assert "Welcome to Facebook" in driver.title
	time.sleep(3)
	driver.find_element_by_id('email').send_keys(facebook_username)
	driver.find_element_by_id('pass').send_keys(facebook_password)
	driver.find_element_by_id("loginbutton").click()
	global all_cookies
	all_cookies = driver.get_cookies()
	html = driver.page_source
	if "Incorrect Email/Password Combination" in html:
		print "[!] Incorrect Facebook username (email address) or password"
		sys.exit()

def loginCS(driver):
	driver.implicitly_wait(100)
	driver.get("https://www.couchsurfing.org/n/places/paris-ile-de-france-france")
	time.sleep(3)
	driver.find_element_by_id('user_login').send_keys(login)
	driver.find_element_by_id('user_password').send_keys(password)
	driver.find_element_by_name("commit").click()

# Find users IDs

loginCS(driver)
# Go to each user page
time.sleep(8)
driver.get("https://www.couchsurfing.com/users/sign_in")
time.sleep(5)
users = []
for element in driver.find_elements_by_css_selector("a.mod-black"):
    users.append(element.get_attribute("href"))
print(users)
# users = map(replace("users/","couch_visits/new?cs_new_fe=true&to_id="),users)
# print(users)

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
