#import required module

from selenium import webdriver
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

#create a selenium browser
driver = webdriver.Chrome(options=options)

#website link
driver.get("https://stgw.iitmandi.ac.in/ug/login.php")
username=driver.find_element_by_name("username")
username.send_keys("_username_")
username=driver.find_element_by_name("password")
username.send_keys("_password_")

#submit button
driver.find_element_by_xpath("//*[@id='content']/article/form/table/tbody/tr[5]/td[2]/input[1]").click()

#let the signin be over
for i in range(10000000):
    continue

#close the browser
driver.close()