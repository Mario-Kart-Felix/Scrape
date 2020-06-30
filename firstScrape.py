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


name_array=[]
role_array=[]
home_array=[]
tr=1
for i in [1,2,3,4,5]:
  try:
    # define next
    nex = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div/span/div/div[3]")
    # define employees
    employees = driver.find_elements_by_xpath('//*[@href]')
    # print employees
    for e in employees:
      while tr < 26:
        employee_name = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[1]/div/div[2]/div[3]/div/a')
        employee_role = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
        
        name_array.append(employee_name.get_attribute('innerText'))
        role_array.append(employee_role.get_attribute('innerText'))

        print(employee_name.get_attribute('innerText'))
        print(employee_role.get_attribute('innerText'))
        
        employee_role.click()
        employee_home = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]')

        
        home_array.append(employee_home.get_attribute('innerText'))
        print(employee_home.get_attribute('innerText'))

        tr=tr+1
    # click next
    nex.click()
    time.sleep(2)

    element = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div[3]/div/a')
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    tr = 2
  except:
    np_name_array = np.array(name_array)
    np_role_array = np.array(role_array)
    np_home_array = np.array(home_array)
    print(np_name_array)
    print(np_role_array)
    print(np_home_array)
    str_company = strcompany.replace(" ", "_")
    df = pd.DataFrame({"name" : np_name_array, "role" : np_role_array, "city" : np_home_array})
    df.to_csv(f"/Users/danielschwartz/Desktop/SF_csv/{str_company}.csv")


  # time.sleep(2)
  

# array = list(filter(None, array))

np_name_array = np.array(name_array)
np_role_array = np.array(role_array)
np_home_array = np.array(home_array)
print(np_name_array)
print(np_role_array)
print(np_home_array)
str_company = strcompany.replace(" ", "_")
df = pd.DataFrame({"name" : np_name_array, "role" : np_role_array, "city" : np_home_array})
df.to_csv(f"/Users/danielschwartz/Desktop/SF_csv/{str_company}.csv")





# for e in employees:
#   while tr < 26:
#     employee_name = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[1]/div/div[2]/div[3]/div/a')
#     employee_role = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
    
#     name_array.append(employee_name.get_attribute('innerText'))
#     role_array.append(employee_role.get_attribute('innerText'))

#     print(employee_name.get_attribute('innerText'))
#     print(employee_role.get_attribute('innerText'))
    
#     employee_role.click()
#     employee_home = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]')

    
#     home_array.append(employee_home.get_attribute('innerText'))
#     print(employee_home.get_attribute('innerText'))

#     tr=tr+1

# # click next
# nex.click()
# time.sleep(2)

# element = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div[3]/div/a')
# driver.execute_script("return arguments[0].scrollIntoView(true);", element)

# tr = 2
# for e in employees:
#   while tr < 26:
#     employee_name = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[1]/div/div[2]/div[3]/div/a')
#     employee_role = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
    
#     name_array.append(employee_name.get_attribute('innerText'))
#     role_array.append(employee_role.get_attribute('innerText'))

#     print(employee_name.get_attribute('innerText'))
#     print(employee_role.get_attribute('innerText'))
    
#     employee_role.click()
#     employee_home = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]')

    
#     home_array.append(employee_home.get_attribute('innerText'))
#     print(employee_home.get_attribute('innerText'))

#     tr=tr+1