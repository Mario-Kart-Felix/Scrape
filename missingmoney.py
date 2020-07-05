from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import pandas as pd
import csv
import os


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
# company = 'Drop'

for filename in os.listdir('/Users/danielschwartz/Desktop/SF_csv2'):
  with open(os.path.join('/Users/danielschwartz/Desktop/SF_csv2', filename)) as csvfile:
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

  acceptable_candidate_array = []
  for i in data:
    if i[2] in good_states:
      acceptable_candidate_array.append(i)
    else:
      continue
  employees_with_up = 0
  for state in acceptable_candidate_array:
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
  for i in acceptable_candidate_array:
    name = i[0]
    name_array.append(name)
  print(name_array)
  addy_array = []
  reporter_array = []
  held_in_array = []
  value_array = []

  company_name_array = []
  temp = filename.split('.')[0]
  temp = temp.split('_')[1:]
  company_name = ' '.join(temp)

  for d in acceptable_candidate_array:
    temp_addy = []
    temp_reporter = []
    temp_held_in = []
    temp_value = []
    temp_company_name_array = []
    name_input = driver.find_element_by_xpath('//*[@id="SearchName"]')
    city_input = driver.find_element_by_xpath('//*[@id="City"]')
    state_input = driver.find_element_by_xpath('//*[@id="State"]')
    search = driver.find_element_by_xpath('//*[@id="SearchForm"]/div/div/div/div[4]/button')
    addresses = driver.find_elements_by_xpath('//*[@id="cd-main-content"]')
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
      string = driver.find_element_by_xpath('//*[@id="cd-main-content"]/div/div[4]/div[1]')
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
        held_in = driver.find_element_by_xpath(f'//*[@id="cd-main-content"]/div/table/tbody/tr[{tr}]/td[3]')
        temp_held_in.append(held_in.get_attribute('innerText'))
        value = driver.find_element_by_xpath(f'//*[@id="cd-main-content"]/div/table/tbody/tr[{tr}]/td[6]')
        temp = str(value.get_attribute('innerText'))
        over_under = temp.split()[0]
        temp_value.append(over_under)
        temp_company_name_array.append(company_name)
        tr = tr+3
      addy_array.append(temp_addy)
      reporter_array.append(temp_reporter)
      held_in_array.append(temp_held_in)
      value_array.append(temp_value)
      company_name_array.append(temp_company_name_array)
      time.sleep(1)
      print(addy_array)
      print(reporter_array)
      print(held_in_array)
      print(value_array)
      employees_with_up += 1
    except:
      print("except")
      # temp_addy = []
      # temp_reporter = []
      addy_array.append(temp_addy)
      reporter_array.append(temp_reporter)
      held_in_array.append(temp_held_in)
      value_array.append(temp_value)
      temp_company_name_array.append(company_name)

      time.sleep(1)
      # print(addy_array)
      # print(reporter_array)
      # print(held_in_array)
      # print(value_array)
      employees_with_up = employees_with_up

  sub_array = []
  big_array = []
  count = 0

  while count < len(name_array):
    sub_array.append(company_name_array)
    sub_array.append(name_array[count])
    sub_array.append(addy_array[count])
    sub_array.append(reporter_array[count])
    sub_array.append(held_in_array[count])
    sub_array.append(value_array[count])
    count = count+1
    big_array.append(sub_array)
    sub_array = []
  print(company_name)
  print(big_array)
    
  np_big_array = np.array(big_array)

  df = pd.DataFrame(np_big_array)
  # company = company.replace(" ", "_")
  numemp = filename.split('_')[0]
  percent_with_up = (int(employees_with_up) / int(numemp)) * 100
  mm = 'mm'
  filename = filename.split('_')[1]
  df.to_csv(f"/Users/danielschwartz/Desktop/mm_csv/{mm}_{percent_with_up}_{filename}")
