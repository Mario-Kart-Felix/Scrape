from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import pandas as pd

company = input("Enter a Company: ")

strcompany = str(company)


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://app.apollo.io/#/login?redirectTo=https%3A%2F%2Fapp.apollo.io%2F%23%2Fonboarding%2Fbulk%3F_k%3Dnbfzqc&_k=hpz0x5")

time.sleep(2)

logIn = driver.find_element_by_name("email")

logIn.click()

driver.find_element_by_name('email').send_keys('daniel@oursimplefuture.com')
driver.find_element_by_name('password').send_keys('Cessnap1Cessnap1')
logIn = driver.find_element_by_class_name("zp_2z1mP")

time.sleep(1)

logIn.click()

time.sleep(2)

search = driver.find_element_by_class_name("zp_MIz8G")

search.click()

search.send_keys(company)
time.sleep(3)
search.send_keys(Keys.RETURN)

time.sleep(2)
employees = driver.find_element_by_class_name("zp_28q-l")
employees.click()

time.sleep(1)
count=0
# define next
nex = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div/span/div/div[3]")
# define employees
employees = driver.find_elements_by_xpath('//*[@href]')
i=0

array=[]
# for i in [1,2,3]:
tr=1
print("hello")
print("tr" + str(tr))
print("i" + str(i))
# print employees
for e in employees:
  while tr < 26:
    employee = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
    array.append(e.get_attribute('innerText'))
    employee.click()
    # then print city...
    tr=tr+1
# click next
nex.click()
time.sleep(2)

element = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div[3]/div/a')
driver.execute_script("return arguments[0].scrollIntoView(true);", element)

tr = 2
for e in employees:
  while tr < 26:
    employee = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
    array.append(e.get_attribute('innerText'))
    employee.click()
    # then print city...
    tr=tr+1

# click next
nex.click()
time.sleep(2)

element = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div[3]/div/a')
driver.execute_script("return arguments[0].scrollIntoView(true);", element)

tr = 2
for e in employees:
  while tr < 26:
    employee = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
    array.append(e.get_attribute('innerText'))
    employee.click()
    # then print city...
    tr=tr+1

    
      

    
  # time.sleep(2)
  

array = list(filter(None, array))
# delete from array 
while strcompany in array:
  array.remove(strcompany)
while 'Templates' in array:
  array.remove('Templates')
while 'Outbox' in array:
  array.remove('Outbox')
while 'Tasks' in array:
  array.remove('Tasks')
while 'Calls' in array:
  array.remove('Calls')
while 'Companies' in array:
  array.remove('Companies')
while 'Overview' in array:
  array.remove('Overview')
while 'Employees' in array:
  array.remove('Employees')
while 'Locations' in array:
  array.remove('Locations')
while 'Browse' in array:
  array.remove('Browse')
while 'Lists' in array:
  array.remove('Lists')
while 'Saved Searches' in array:
  array.remove('Saved Searches')

# print(array)
nparray = np.array(array)
print(nparray)
str_company = strcompany.replace(" ", "_")
pd.DataFrame(nparray).to_csv(f"/Users/danielschwartz/Desktop/scraping/{str_company}.csv")







# # scroll down
# box = driver.find_elements_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table')
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", box)
# time.sleep(5)




