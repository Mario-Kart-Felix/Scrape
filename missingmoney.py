from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import pandas as pd
import csv


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.missingmoney.com/en/Property/Search')

time.sleep(1)

name_input = driver.find_element_by_xpath('//*[@id="SearchName"]')
city_input = driver.find_element_by_xpath('//*[@id="City"]')
state_input = driver.find_element_by_xpath('//*[@id="State"]')
search = driver.find_element_by_xpath('//*[@id="SearchForm"]/div/div/div/div[4]/button')
addresses = driver.find_elements_by_xpath(('//*[@id="cd-main-content"]'))


good_states = ['AL', 'AK', 'AZ', 'AR', 'CO', 'DC', 
  'FL', 'ID', 'IL', 'IA', 'KY', 'LA', 'ME', 'MD',
  'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 
  'NH', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'RI',
  'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WV', 'WI']

with open('/Users/danielschwartz/Desktop/SF_csv/Blind.csv', newline='') as csvfile:
  data = list(csv.reader(csvfile))
for role in data:
  role.pop(0)
  role.pop(1)
for citystate in data:
  location = citystate[1]
  city, state = location[:-3].strip(", "), location[-2:]
  citystate.pop(1)
  citystate.append(city)
  citystate.append(state)

array = []
for i in data:
  if i[2] in good_states:
    array.append(i)
  else:
    continue

for state in array:
  if state[2] == 'AL':
    state[2] = 'Alabama'
  elif state[2] == 'AK':
    state[2] = 'Alaska'
  elif state[2] == 'AZ':
    state[2] = 'Arizona'
  elif state[2] == 'AR':
    state[2] = 'Arkansas'
  elif state[2] == 'CO':
    state[2] = 'Colorado'
  elif state[2] == 'DC':
    state[2] = 'District of Columbia'
  elif state[2] == 'FL':
    state[2] = 'Florida'
  elif state[2] == 'ID':
    state[2] = 'Idaho'
  elif state[2] == 'IL':
    state[2] = 'Illinois'
  elif state[2] == 'IN':
    state[2] = 'Indiana'
  elif state[2] == 'IA':
    state[2] = 'Iowa'
    state[2] = 'Kentucky'
  elif state[2] == 'LA':
    state[2] = 'Louisiana'
  elif state[2] == 'ME':
    state[2] = 'Maine'
  elif state[2] == 'MD':
    state[2] = 'Maryland'
  elif state[2] == 'MA':
    state[2] = 'Massachusetts'
  elif state[2] == 'MI':
    state[2] = 'Michigan'
  elif state[2] == 'MN':
    state[2] = 'Minnesota'
  elif state[2] == 'MS':
    state[2] = 'Mississippi'
  elif state[2] == 'NE':
    state[2] = 'Nebraska'
  elif state[2] == 'NV':
    state[2] = 'Nevada'
  elif state[2] == 'NH':
    state[2] = 'New Hampshire'
  elif state[2] == 'NJ':
    state[2] = 'New Jersey'
  elif state[2] == 'NM':
    state[2] = 'New Mexico'
  elif state[2] == 'NY':
    state[2] = 'New York'
  elif state[2] == 'NC':
    state[2] = 'North Carolina'
  elif state[2] == 'ND':
    state[2] = 'North Dakota'
  elif state[2] == 'OH':
    state[2] = 'Ohio'
  elif state[2] == 'OK':
    state[2] = 'Oklahoma'
  elif state[2] == 'RI':
    state[2] = 'Rhode Island'
  elif state[2] == 'SC':
    state[2] = 'Sount Carolina'
  elif state[2] == 'SD':
    state[2] = 'South Dakota'
  elif state[2] == 'TN':
    state[2] = 'Tennessee'
  elif state[2] == 'TX':
    state[2] = 'Texas'
  elif state[2] == 'UT':
    state[2] = 'Utah'
  elif state[2] == 'VT':
    state[2] = 'Vermont'
  elif state[2] == 'VA':
    state[2] = 'Virginia'
  elif state[2] == 'WV':
    state[2] = 'West Virginia'
  elif state[2] == 'WI':
    state[2] = 'Wisconsin'
# data.pop(0)
name_array = []
for i in array:
  name = i[0]
  name_array.append(name)
print(name_array)
addy_array = []
temp_addy = []
reporter_array = []
temp_reporter = []
for d in array:
  name_input = driver.find_element_by_xpath('//*[@id="SearchName"]')
  city_input = driver.find_element_by_xpath('//*[@id="City"]')
  state_input = driver.find_element_by_xpath('//*[@id="State"]')
  search = driver.find_element_by_xpath('//*[@id="SearchForm"]/div/div/div/div[4]/button')
  addresses = driver.find_elements_by_xpath(('//*[@id="cd-main-content"]'))
  name = d[0]
  city = d[1]
  state = d[2]
  name_input.click()
  name_input.clear()
  name_input.click()
  name_input.send_keys(name)
  city_input.click()
  city_input.clear()
  city_input.click()
  city_input.send_keys(city)
  state_input.click()
  state_input.send_keys(state)
  search.click()
  time.sleep(3)
  tr = 1
  try:
    string = driver.find_element_by_xpath('//*[@id="cd-main-content"]/div/div[5]/div[1]')
    string = str(string.get_attribute('innerText'))
    split = 'of'
    string = string.partition(split)[2]
    split = 'items'
    count_temp = string.partition(split)[0]
    count = int(count_temp)
    for addy in range(count):
      address = driver.find_element_by_xpath(f'//*[@id="cd-main-content"]/div/table/tbody/tr[{tr}]/td[4]')
      temp_addy.append(address.get_attribute('innerText'))
      reporter = driver.find_element_by_xpath(f'//*[@id="cd-main-content"]/div/table/tbody/tr[{tr}]/td[5]')
      temp_reporter.append(reporter.get_attribute('innerText'))
      tr = tr+3
    addy_array.append(temp_addy)
    reporter_array.append(temp_reporter)
    temp_addy = []
    temp_reporter = []
 
  except:
    temp_addy = []
    temp_reporter = []
    addy_array.append(temp_addy)
    reporter_array.append(temp_reporter)

np_array = np.array(name_array)
np_addy_array = np.array(addy_array)
np_reporter_array = np.array(reporter_array)

print(addy_array)
print(reporter_array)
  


df = pd.DataFrame({"name/city/state" : np_array, "address" : np_addy_array, "reporter" : np_reporter_array})
df.to_csv("/Users/danielschwartz/Desktop/test.csv")
