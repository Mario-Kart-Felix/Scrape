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

# files = ['140_JVC_Broadcasting.csv', '140_Jewish_Senior_Life_of_Rochester.csv', '140_Jones_Memorial_Hospital.csv', '140_Jopwell.csv', '140_Jujamcyn_Theaters_LLC.csv', '140_K_Health.csv', '140_Kadmon.csv', '140_Kenmore_Mercy_Hospital.csv', "140_Khan's_Tutorial.csv", '140_Kidz_Therapy_Services.csv', '140_Knock.csv', '140_Kualitatem_Inc..csv', '140_LOOP_Digital_Inc..csv', '140_LREI.csv', '140_Lambda_Legal.csv', '140_Landauer_Metropolitan.csv', '140_Level_Group_-_New_York.csv', '140_Lexington_Center_For_Recovery.csv', '140_Liberty_Life_Assurance_Co.csv', '140_Lineate.csv', '140_Priority_Healthcare_Group.csv', '140_Privet_Investments_LLC.csv', '140_R2Net_Inc_-_JamesAllen.com.csv', '140_RANE_(Risk_Assistance_Network_+_Exchange).csv', '140_RED_Model_Management_-_RED_NYC.csv', '140_Radius_Global_Market_Research.csv', '140_Raia_Drogasil_S.A..csv', '140_Ralph_Appelbaum_Associates.csv', '140_Real_E-Stats.csv', '140_Rebecca_Taylor.csv', '140_Richloom_Fabrics_Group.csv', '140_Rochester_Museum_&_Science_Center.csv', '140_Rockrose_Development_Corp..csv', '140_Rustans_Coffee_CORP.csv', '140_SEVENROOMS.csv', '140_SOMOS_Community_Care.csv', '140_SPIRE_GROUP.csv', '140_SPORTS195.csv', '140_Schools_&_You.csv', '140_Siguler_Guff_&_Company.csv', '140_SmartAsset.csv', '140_Soleo.csv', '140_Solvay_Bank.csv', '140_Something_Digital.csv', '140_Star_Construction.csv', '140_Stellar_Services.csv', '140_StreetWise_Partners.csv', '140_Strong_Hospital.csv', '140_Stuyvesant_High_School.csv', '140_Suffolk_Transportation_Svc_Inc.csv', '140_Suit_KOTE.csv', '140_Super_Enterprises.csv', '140_SupplyHouse.com.csv', '140_Synthesio.csv', '140_TDT_INC.csv', '140_TEC_Systems,_Inc..csv', '140_TMP_Directional_Marketing.csv', '140_TSR_Consulting_Services,_Inc.csv', '140_Team_Whistle.csv', '140_Ted_Moudis_Associates.csv', '140_Terra-Gen,_LLC.csv', '140_The_Alliance_for_Positive_Change.csv', '140_The_C-Suite_Network.csv', '140_The_Explorers_Club.csv', '140_The_Garden_City_Hotel.csv', '140_The_Mental_Health_Association_of_Westchester_Inc..csv', '140_The_NoMad_Hotel_New_York.csv', '140_The_Raine_Group.csv', '140_The_Real_Deal.csv', '140_Theatre_Communications_Group.csv', '140_Tompkins_Insurance.csv', '140_Tompkins_Trust_Company.csv', '140_Topix_Pharmaceuticals,_Inc..csv', '140_Town_and_Country_Living.csv', '140_Traub_Lieberman_Straus_&_Shrewsberry_LLP.csv', '140_Trepp,_LLC.csv', '140_Trinity_Packaging_Corp.csv', '140_Troy_City_Schools.csv', '140_Truelogic_Software.csv', '140_Tully_Rinckey_PLLC.csv', "140_Turkish_Women's_International_Network.csv", '140_Understood.csv', '140_Union_Theological_Seminary.csv', '140_UroGen_Pharma.csv', '140_Usherwood_Office_Technology.csv', '140_VAI_(Vormittag_Associates,_Inc.).csv', '140_VAST_Data.csv', '140_Valiant_Solutions,_Inc..csv', '140_Vibrant_Media.csv', '140_Vicon_Industries.csv', '140_Vince_Camuto.csv', '140_Vistar_Media.csv', '140_WILDTYPE,_a_TBWA\\WorldHealth_Company.csv', '140_WTMC.csv', '140_Wealth_Advisory_Group_LLC.csv', '140_Weiss_Multi-Strategy_Advisers_LLC.csv', '140_Westchester_Institute_For_Human_Development.csv', '140_Windham_Mountain_Resort.csv', '140_Wolf-Gordon.csv', "140_Women's_World_Banking.csv", '140_Woori_America_Bank.csv', '140_Worldwide_Travel_Staffing,_Ltd..csv', '140_Y2k_Computer_Solutions.csv', '140_Yoga_To_The_People.csv', '140_Yonkers_Contracting_Company,_Inc..csv', '140_YouNow,_Inc..csv', '140_Young_Adult_Institute_Inc.csv', '140_Zoni_Language_Centers.csv', '140_eos_Products.csv', '140_innRoad.csv', '150_Art_+_Commerce.csv', '150_Bar_Tabac.csv', '150_Basic_Resources,_Inc..csv', '150_Bliwa_Livförsäkring.csv', 
# '150_CAAT_Inc.csv', '150_CPI_Aerostructures.csv', '150_Carver_Federal_Savings_Bank.csv', '150_Community_Counseling_and_Mediation.csv', '150_Day_Automation.csv', '150_EXCELSIOR_ORTHOPAEDICS.csv', '150_Eger_Health_Care_and_Rehabilitation_Center.csv', '150_Expert_Institute.csv', '150_GDI_Services,_Inc..csv', '150_Generation_Ready.csv', '150_German_American_Chamber_of_Commerce,_Inc..csv', '150_Glens_Falls_National_Bank_&_Trust_Co..csv', '150_Grafana_Labs.csv', '150_Greater_Than_One.csv', '150_Greek_Orthodox_Archdiocese_of_America.csv', '150_Haas,_Inc..csv', '150_Harris_Healthcare.csv', '150_Hearth_Management.csv', '150_Hyperscience.csv', '150_ISAAC_Heating_and_Air_Conditioning.csv', '150_ITT_Enidine.csv', '150_Iglesia_De_Dios_De_La_Profecia.csv', '150_ImpreMedia.csv', '150_InfoDesk.csv', '150_Insider_Intelligence.csv', '150_Installs_LLC.csv', '150_Internal_Medicines.csv', '150_Joomla!.csv', '150_Keller_Williams_Realty_Greater_Rochester.csv', '150_Keller_Williams_Realty_Partners_New_York.csv', '150_Krung_Thai_Bank_LTD.csv', '150_Lee_Spring.csv', '150_MeritDirect.csv', '150_NYIC_(NEW_YORK_INTERNATIONAL_CAPITAL,_LLC).csv', "150_NYS_Teachers'\u200b_Retirement_System.csv", '150_Oneida_Herkimer_Madison_BOCES.csv', '150_PJ_SOLOMON.csv', '150_Packet,_an_Equinix_Company.csv', '150_Power_Drives_Inc..csv', '150_Praytell.csv', '150_SKIP_of_NY.csv', '150_Select_Equity_Group,_L.P..csv', '150_Shiraz_Creative.csv', '150_SmartFlyer.csv', '150_Sunmount_Ddso.csv', '150_Tfl_Transport.csv', '150_The_Chazen_Companies.csv', '150_The_Earth_Institute,_Columbia_University.csv', '150_The_Solomon_Organization.csv', '150_Update_Legal.csv', '150_Vestal_Central_School_District.csv', '150_Vida_Shoes_International.csv', '150_Worth_New_York.csv', '150_Z-Tech.csv', '15_Promesa,_Inc..csv', "160_ST._LUKE'S_ROOSEVELT_HOSPITAL.csv", '170_Wing.csv', '19_Chdc.csv', '207,000_精进电动科技股份有限公司.csv', '220_VIVALDI_.csv', '22_OLE.csv', '242,000_騰訊WE+.csv', '25,000_eni.csv', '260_Pilot.csv', '260_Vernalis..csv', '26_Taco.csv', '27_Merlin.csv', '2_Ladders.csv', '360_KS&R.csv', '3_GreenSlate.csv', '3_The_Principle_Group.csv', '44_GEM.csv', '57_21GRAMS.csv', '66_Seneca.csv', '6_Gravitas.csv', '75_Foodlink.csv', '760_Paperchase.csv', '76_Chrysalis.csv', '76_Scotts_Lawn_Service.csv', '7_PTJ.csv', '7_hue.csv', '80_AWH.csv', '80_Marist_Brothers.csv', '82_New_Horizon_Counseling_Center.csv', '87_DOROT.csv']
# Mass
files = ['150_Aura.csv', '1,200_Commonwealth.csv', '320_Gandara_Center.csv', '300_Servier_Pharmaceuticals.csv', '310_Sullivan_&_Worcester_LLP.csv', '330_Tanisha_Systems,_Inc.csv', '310_VT_MAK.csv', '290_Workable.csv', '290_EF_Go_Ahead_Tours.csv', '310_The_Massachusetts_Eye_and_Ear_Infirmary.csv', '320_Madison_Security_Group,_Inc..csv', '290_Summit_Partners.csv', '320_General_Insulation_Company.csv', '300_Eastern_Nazarene_College.csv', '300_UNICOM_Engineering.csv', '300_Football_Nation.csv', '480_Q3_Technologies.csv', '300_The_Middlesex_Corporation.csv', '330_MSPCA-Angell.csv', '570_National_College.csv', '340_HYCU,_Inc..csv', '330_Balise_Motor_Sales.csv', '300_Alpha_Analytical.csv', '310_Aberdeen.csv', '300_codemantra.csv', '2_MMB.csv', '290_Audax_Group.csv', '320_Boston_Health_Care_for_the_Homeless_Program.csv', '310_Delaware_Life_Insurance_Company.csv', '290_Aubuchon_Hardware.csv', '320_EDENS.csv', '560_PeoplesBank.csv', '300_Akcea_Therapeutics.csv', '290_eBay_Enterprise_Marketing_Solutions_(formerly_e-Dialog).csv', '300_Lab_Pros.csv', '320_Hinckley_Allen.csv', '250_YOU,_Inc..csv', '320_SiliconExpert.csv', '310_Gordon_Conwell_Theological_Seminary.csv', '130_KMA.csv', '330_Learning_Express_Toys.csv', '330_Prime_Motor_Group.csv']
# for filename in sorted(os.listdir('/Users/danielschwartz/Desktop/simplefuture/SF_Schools')):
for filename in files:
  try:
    with open(os.path.join('/Users/danielschwartz/Desktop/simplefuture/apollo_csvs/Mass', filename)) as csvfile:
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
    df.to_csv(f"/Users/danielschwartz/Desktop/simplefuture/mm_csvs/2nd_Release/mm_Mass_2/{mm}_{percent_with_up}_{all_employees}_{filename}")
  except:
    continue