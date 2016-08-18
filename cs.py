from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time,re,sys
from selenium.webdriver.common.keys import Keys

 #Chrome Options
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
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
	driver.implicitly_wait(120)
	driver.get("https://www.couchsurfing.com/users/sign_in")
	time.sleep(3)
	driver.find_element_by_id('user_login').send_keys("adrifaoudai2@hotmail.com")
	driver.find_element_by_id('user_password').send_keys("hackhack")

loginCS(driver)

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
