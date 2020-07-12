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

files = ['160_Altamarea_Group.csv', '160_American_Transit_Insurance_C.csv', '160_Applied_Data_Finance.csv', '160_Big_Spaceship.csv', '160_Catalyst_Inc.csv', '160_Civic_Entertainment_Group,_LLC_(A_Seacrest_Global_Group_Company.csv', '160_Coalition_for_Hispanic_Family_Service.csv', '160_Concordia_International_Forwarding_Corporatio.csv', '160_DFO_Global_Performance_Commerce.csv', '160_DLC_Management_Corp..csv', '160_Datalo.csv', '160_Dayton_T._Brown,_Inc.csv', '160_DeCrescente_Dist._Co.,_Inc..csv', '160_Deloitte_Tax_LLP.csv', '160_Echidna.csv', '160_Edwin_Gould_Services_for_Children_&_Familie.csv', '160_ExecOnline,_Inc..csv', '160_FIAF_-_French_Institute_Alliance_Francaise.csv', '160_Frenkel_&_Compan.csv', '160_Garfunkel_Wild,_P.C..csv', '160_GroundLin.csv', '160_Hospice_&_Palliative_Care_Buffal.csv', '160_Kindergarten_Kid.csv', '160_MSA_MODEL.csv', '160_Marymount_School_of_New_York.csv', '160_Meadowbrook_Financial_Mortgage_Bankers_Corp..csv', '160_NY_Kids_Club_and_NY_Preschool.csv', '160_NoHo_Hospitality_Group.csv', '160_Norwich_Pharma_Services.csv', '160_ONEGROUP_Risk_Management_and_Insurance.csv', '160_Oswego_Health.csv', '160_Plate.csv', '160_Property_Markets_Group.csv', '160_Public_Preparatory_Networ.csv', '160_Royal_Health_Care.csv', "160_ST._LUKE'S_ROOSEVELT_HOSPITAL.csv", '160_Sailthru.csv', '160_Skyhorse_Publishing,_Inc.csv', '160_Smithsonian_Channel.csv', '160_TDX_Construction_Corporation.csv', '160_The_IMA_Grou.csv', '160_The_Wall_Group.csv', '160_Town_of_Colonie.csv', '160_Vector_Media.csv', '160_Westcon-Comstor_North_America.csv', "160_Women_Presidents'\u200b_Organization.csv", '160_Xaverian_High_School.csv', '160_pymetrics.csv', '170_Blue_Stat.csv', '170_CDG_NY.csv', '170_Democrat_and_Chronicle_-_Part_of_the_USA_Today_Networ.csv', '170_Elite_Dail.csv', '170_Fluent,_In.csv', '170_JUV_Consultin.csv', '170_Kernel,_Created_by_Spectrum_Reac.csv', '170_Optimedia_U.csv', '170_Thrillis.csv', '180_McCann_Health_New_Yor.csv', '180_Mother_New_Yor.csv', '180_Partners_+_Napie.csv', '180_Search_Laboratory_Inc.csv', '180_United_Entertainment_Grou.csv', '18_Amalgamated.csv', '190_121_Graphic_Desig.csv', '190_Influenste.csv', '190_Orion_Worldwid.csv', '190_The_Webby_Award.csv', '190_bayarda.csv', '2,400_Fairfield_Inn_&_Suites.csv', '2,900_Department_of_Public_Wor.csv', '200_9.8_Grou.csv', '200_Captivate,_LL.csv', '200_GALE_Partner.csv', '200_H4B_Chelse.csv', '200_Horizon_Nex.csv', '200_Neon_-_An_FCB_Health_Network_Compan.csv', '200_Remedy_Health_Medi.csv', '32_Rumble.csv', '360_KS&R.csv', '57_21GRAMS.csv', '6_Gravitas.csv', '730_Wartburg.csv', '75_Foodlink.csv', '7_PTJ.csv']
# for filename in sorted(os.listdir('/Users/danielschwartz/Desktop/simplefuture/SF_Schools')):
for filename in files:
  try:
    with open(os.path.join('/Users/danielschwartz/Desktop/simplefuture/apollo_csvs/NY_NoFunding', filename)) as csvfile:
      data = list(csv.reader(csvfile))
    all_employees = filename.split('_')[0]
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
    total_employees = 0
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
    print(company_name)
    for d in acceptable_candidate_array:
      has_up = False
      temp_addy = []
      temp_reporter = []
      temp_held_in = []
      temp_value = []
      temp_company_name = [f"{company_name}"]
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
        print("trying")
        string = driver.find_element_by_xpath('//*[@id="cd-main-content"]/div/div[4]/div[1]')
        string = str(string.get_attribute('innerText'))
        split = 'of'
        string = string.partition(split)[2]
        split = 'items'
        count_temp = string.partition(split)[0]
        count = int(count_temp)
        print('before for loop')
        for addy in range(count):
          print("in loop")
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
          tr = tr+3
          has_up = True
        print("after for loop")
        addy_array.append(temp_addy)
        reporter_array.append(temp_reporter)
        held_in_array.append(temp_held_in)
        value_array.append(temp_value)
        time.sleep(1)
        # print(addy_array)
        # print(reporter_array)
        # print(held_in_array)
        # print(value_array)
        total_employees += 1
        print("tried")
      except:
        print("except")
        addy_array.append(temp_addy)
        reporter_array.append(temp_reporter)
        held_in_array.append(temp_held_in)
        value_array.append(temp_value)    

        time.sleep(1)
        # print(addy_array)
        # print(reporter_array)
        # print(held_in_array)
        # print(value_array)
        total_employees += 1
      if has_up == True:
        employees_with_up += 1
      else:
        employees_with_up = employees_with_up
    company_name_array.append(temp_company_name)
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

    df = pd.DataFrame(np_big_array, columns = ['Company Name', 'Name', 'Addresses', 'Reporting Entity', 'State Holding', 'Value (Under/Over 100$)'])
    # numemp = filename.split('_')[0]

    try:
      percent_with_up = round((int(float(employees_with_up)) / int(float(total_employees))) * 100)
    except:
      percent_with_up = 0
    mm = 'mm'
    filename = filename.split('_')[1:]
    filename = ' '.join(filename)
    filename = filename.replace(" ", "_")
    df.to_csv(f"/Users/danielschwartz/Desktop/simplefuture/mm_csvs/mm_NY_NoFunding2/{mm}_{percent_with_up}_{all_employees}_{filename}")
  except:
    continue