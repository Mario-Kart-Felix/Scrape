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

# files = ['120_HONK_Technologies.csv', '120_HoneyBook.csv', '120_Human_Longevity,_Inc..csv', '120_Infoworks.io.csv', '120_Kika_Tech,_Inc..csv', '120_Komprise.csv', '120_Mindstrong.csv', '130_Arxan_Technologies.csv', '130_Beeswax.csv', '130_Betterworks.csv', '130_Buffer.csv', '130_Daylight_Solutions.csv', '130_Fluent_City.csv', '130_Freenome.csv', '130_GlassPoint_Solar.csv', '130_InMarket.csv', '130_Insightly.csv', '140_AutoRABIT.csv', '140_Backblaze_Cloud_Storage_&_Backup.csv', '140_Blavity_Inc..csv', '140_BlueRock_Therapeutics.csv', '140_Clarify_Health_Solutions.csv', '140_EZ_Texting.csv', '140_Fetch_Robotics.csv', '140_Jopwell.csv', '140_ManyChat.csv', '150_Analogix_Semiconductor_Inc..csv', '150_Boulevard.csv', '150_CUJO_AI.csv', '150_Carbon_Health.csv', '150_Elements_Behavioral_Health.csv', '150_Fruit_Street.csv', '150_Greenlots.csv', '150_Inbenta.csv', '150_Internet_Archive.csv', '150_LetsGetChecked.csv', '150_Managed_by_Q.csv', '150_MaxPreps.csv', '160_Bidgely.csv', '160_Bowery_Farming.csv', '160_Chainalysis_Inc..csv', '160_Contently.csv', '160_Corelight,_Inc.csv', '160_CreatorIQ.csv', '160_Deep_Instinct.csv', '160_Dia&Co.csv', '160_Emissary.io.csv', '160_FloQast.csv', '160_Flutterwave.csv', '160_Frame.io.csv', '160_GroundLink.csv', '160_Lastline,_Inc..csv', '160_Mad_Street_Den.csv', '160_Mark43.csv', '160_b8ta.csv', '17,000_Citizen.csv', '170_ATTN:.csv', '170_Clever_Inc..csv', '170_Clique_Brands.csv', '170_CloudCheckr.csv', '170_Codility.csv', '170_Envoy..csv', '170_Expanse..csv', '170_LvYue_Group.csv', '170_M.M.LaFleur.csv', '170_Nativo_Inc.csv', '17_Aquant.csv', '180_Bright_Event_Rentals.csv', '180_Bungalow.csv', '180_CrossBorder_Solutions.csv', '180_Crunchbase.csv', '180_Hello_Alfred.csv', '180_Helpshift.csv', '180_Instapage.csv', '180_Mynd_Property_Management.csv', '190_Apartment_List.csv', '190_BigID.csv', '190_Cyara.csv', '190_Daily_Harvest.csv', '190_KaiOS_Technologies,_Inc..csv', '190_LeanData,_Inc..csv', '190_Maker_Studios_Inc.csv', '19_Castle.csv', '200_Amagi_Corporation.csv', '200_CEIPAL_Corp..csv', '200_Caliva.csv', '200_Cerebras_Systems.csv', '200_Conversica.csv', '200_Fungible,_Inc..csv', '200_HealthTap.csv', '208,000_Apple.csv', '210_Jio_Health.csv', '210_hims_&_hers.csv', '220_Magic,_Inc.csv', '230_Blink_Health.csv', '230_DailyPay,_Inc..csv', '230_Everlaw..csv', '230_Goodreads.com.csv', '230_Instawork.csv', '240_Dolls_Kill.csv', '240_Evidation_Health.csv', '240_Good_Eggs.csv', '240_Hitwise.csv', '240_MATRIXX_Software.csv', '240_inDriver.csv', '240_method_products_pbc.csv', '250_AppZen.csv', '250_Appetize.csv', '250_Ceros.csv', '250_Linden_Lab.csv', '260_Fundbox.csv', '260_Hinge_Health.csv', '270_CleverTap.csv', '270_GWC_Inc.csv', '270_MoEngage_Inc..csv', '280_HG_Insights.csv', '280_HOVER_Inc..csv', '280_Incorta.csv', '290_Biz2Credit.csv', '290_Celigo.csv', '29_Banjo.csv', '300_Cleo.csv', '310_Bright_Machines.csv', '310_IP_Infusion.csv', '320_Armis.csv', '320_FaZe_Clan.csv', '320_GOOD_Worldwide_Inc.csv', '330_ASAPP.csv', '330_Fivestars.csv', '330_Headspace_Inc..csv', '330_Modsy.csv', '330_Movable_Ink.csv', '340_Allegro_Development_Corp..csv', '340_Attentive.csv', '340_Directly.csv', '350_Depositphotos.csv', '350_Hearsay_Systems.csv', '360_Allbirds.csv', '360_Marketing_Evolution.csv', '36_Aspiration.csv', '370_Augmedix.csv', '370_Cloudbeds.csv', '370_FirstLight_Fiber.csv', '390_Crew.csv', '400_Alignment_Healthcare.csv', '400_Healthify.csv', '410_BirdEye.csv', '410_MindTickle.csv', '430_Legend3D.csv', '45_Blind.csv', '480_Brex.csv', '480_CARTO.csv', '490_Mapbox.csv', '5,600_Deliv.csv', '500_Daitan_Group.csv', '51_Genvid_Technologies_Inc..csv', '52_Enlitic.csv', '53_Boosted,_Inc..csv', '54_Arris_Composites,_Inc..csv', '55_At-Bay.csv', '56_Excelfore_Corporation.csv', '56_IceKredit,_Inc._(上海冰鉴信息科技有限公司).csv', '56_MAZ_Systems_Inc..csv', '57_Bright_Pattern.csv', '57_Hello_Heart.csv', '58_Aperia_Technologies.csv', '58_CARMERA.csv', '59_Brandable.csv', '59_Camino_Financial.csv', '59_Commsignia.csv', '59_Kettlebell_Kitchen.csv', '59_Mixmax.csv', '6,900_Collab.csv', '60_eXelate,_A_Nielsen_Company.csv', '61_Imbellus.csv', '62_B12.csv', '62_Inscopix,_Inc..csv', '63_Everest_Medicines.csv', '64_Avanan.csv', '64_Chewse.csv', '64_Coffee_Meets_Bagel.csv', '64_CommonGrounds_Workplace.csv', '64_Emtrain..csv', '64_Forward_Networks,_Inc..csv', '65_CredSimple.csv', '670_Bread.csv', '67_AQS,_Inc..csv', '67_Fortanix.csv', '67_Kaia_Health.csv', '67_Lumina_Networks.csv', '67_MenuSifu.csv', '6_CyberCube.csv', '7,300_Concord.csv', '700_Cadre.csv', '70_Memphis_Meats.csv', '70_goTenna.csv', '73_Comeet.csv', '74_Ansible.csv', '74_Conversocial.csv', '74_Datera.csv', '74_Enviance_|_a_Cority_company.csv', '74_mCube,_Inc..csv', '75_Fleetsmith.csv', '76_CommerceIQ.csv', '76_Emerald_Cloud_Lab.csv', '76_Fuel50.csv', '76_Kitchen_United.csv', '80_Cloud4Wi.csv', '81_Feedvisor.csv', '82_BrightInsight.csv', '84_EverString.csv', '84_MindTouch.csv', '84_Mojo_Vision_Inc..csv', '85_Deliverr_Inc..csv', '85_Global_Communication_Semiconductors,Inc..csv', '86_Kongregate.csv', '87_Amino_Apps.csv', '87_Invoice2go.csv', '87_Kasisto,_Inc..csv', '89_Connected_Cannabis_Co..csv', '89_FogHorn_Systems,_Inc.csv', '89_Logikcull.com.csv', '90_Arkadium.csv', '91_GEO_Semiconductor,_Inc..csv', '92_LogDNA.csv', '930_Common.csv', '93_Embark_Trucks.csv', '94_Alpha_(alphahq.com).csv', '94_MFour_Mobile_Research.csv', '96_August_Home_Inc.csv', '96_Fulham_Co.,_Inc..csv', '97_Animoto.csv']
# files = ['170_CUNY_Graduate_School_of_Public_Health_and_Health_Policy.csv', '170_Chicago_Scholars.csv', '170_Cornell_SC_Johnson_College_of_Business.csv', '170_DePaul_University_College_of_Computing_and_Digital_Media.csv', '180_Chicago-Kent_College_of_Law,_Illinois_Institute_of_Technology.csv', '180_City_Colleges_of_Chicago-Harry_S_Truman_College.csv', '180_City_Colleges_of_Chicago-Wilbur_Wright_College.csv', '180_Donald_&_Barbara_Zucker_School_of_Medicine.csv', '190_Brewton-Parker_College.csv', '190_Campus_Labs.csv', '190_Craig_Newmark_Graduate_School_of_Journalism_at_CUNY.csv', '2,000_Colgate_University.csv', '2,100_Bradley_University.csv', '2,300_Borough_of_Manhattan_Community_College.csv', '2,300_Eastern_Illinois_University.csv', '2,600_Adelphi_University.csv', '2,600_Chamberlain_University.csv', '2,700_Columbia_College_Chicago.csv', '2,800_Baruch_College.csv', '2,900_Bryant_&_Stratton_College.csv', '200_Baruch_College_-_Continuing_and_Professional_Studies_(CAPS).csv', '200_City_Colleges_of_Chicago-Malcolm_X_College.csv', '210_Arnot_Ogden_Medical_Center.csv', '220_Chicago_Kent_College_of_Law.csv', '220_City_University_of_New_York-Brooklyn_College.csv', '220_Cornell_University_College_of_Agriculture_and_Life_Sciences.csv', '220_Cornell_University_ILR_School.csv', '220_Glenville_State_College.csv', '240_Allen_School_of_Health_Sciences.csv', '240_Five_Towns_College.csv', '260_Columbia_|_SIPA.csv', '260_Fullstack_Academy.csv', '270_Columbia_University_-_Columbia_School_of_Social_Work.csv', '3,300_Fashion_Institute_of_Technology.csv', '330_Columbia_University_-_Graduate_School_of_Journalism.csv', '370_Columbia_University_School_of_Professional_Studies.csv', '390_Cayuga_Community_College.csv', '4,800_Fordham_University.csv', '400_Becker_Professional_Education.csv', '420_CUNY_School_of_Professional_Studies.csv', '420_City_School_District_Albany.csv', '450_Elmira_College.csv', '460_Cornell_Johnson_Graduate_School_of_Management.csv', '460_Gies_College_of_Business_-_University_of_Illinois_Urbana-Champaign.csv', '470_Cardozo_School_of_Law.csv', '490_AIU_Online.csv', '500_Black_Hawk_College.csv', '530_Brooklyn_Law_School.csv', '550_Adler_University.csv', '570_Finger_Lakes_Community_College.csv', '570_Genesee_Community_College.csv', '590_Bank_Street_College_of_Education.csv', '670_Alfred_State_College_-_SUNY_College_of_Technology.csv', '680_Dutchess_Community_College.csv', '710_Columbia_University_Mailman_School_of_Public_Health.csv', "720_D'Youville_College.csv", '740_Columbia_Law_School.csv', '760_Daemen_College.csv', '780_Fordham_University_School_of_Law.csv', '790_CUNY_New_York_City_College_of_Technology.csv', '800_ASA_College.csv', '820_Alfred_University.csv', '830_Concordia_University_Chicago.csv', '950_CUNY_Hostos_Community_College.csv']
files = ["150_Let's_Get_Ready.csv", '150_LetsGetChecked.csv', '150_Linium.csv', '150_Little_Lukes.csv', '150_MIAC_-_Mortgage_Industry_Advisory_Corporation.csv', '150_MOTION_PT_Group_Physical,_Occupational_&_Speech_Therapy.csv', '150_MacKenzie-Childs,_LLC.csv', '150_Madwell.csv', '150_Mainstreethost.csv', '150_MakeSpace.csv', '150_Managed_by_Q.csv', '150_Manhattan_Theatre_Club.csv', '150_Margolin,_Winer_&_Evens_LLP.csv', '150_Marietta_Hospitality.csv', '150_McFarland_Johnson.csv', '150_MeritDirect.csv', '150_Mobile_Accessories.csv', '150_Mouse.csv', '150_Mueser_Rutledge_Consulting_Engineers.csv', '150_NEFCU.csv', '150_NYC_Civilian_Complaint_Review_Board_(CCRB).csv', '150_NeueHouse.csv', '150_New_Image_Hair_Salon.csv', '150_New_York_Hilton_Midtown.csv', '150_New_York_State_Department_of_Motor_Vehicles.csv', '150_New_York_State_Office_of_the_Medicaid_Inspector_General.csv', '150_Nicholas_H._Noyes_Memorial_Hospital.csv', '150_Northeast_Home_Medical_Eqp.csv', '150_Octave_Group.csv', '150_Olsten_Staffing_Services.csv', '150_Oneida_Herkimer_Madison_BOCES.csv', '150_Ontario_ARC.csv', '150_Optitex.csv', '150_PDT_Partners.csv', '150_PRFI,_Inc..csv', '150_People10_Technologies_Inc..csv', '150_Platinum_Properties.csv', '150_Premier_Lacrosse_League.csv', '150_Purpose_PBC.csv', '150_Quadio.csv', '150_Quontic_Bank.csv', '150_Rafael_Viñoly_Architects.csv', '150_Recruitics.csv', '150_Revman_International.csv', '150_SHoP_Architects.csv', '150_SRCTec,_LLC.csv', "150_Saint_Dominic's_Home.csv", '150_Salient_Management_Company.csv', '150_Saratoga_Casino_Hotel.csv', '150_Seeds_of_Peace.csv', '150_Sell2World.csv', '150_Seneca_Niagara_Casino.csv', '150_Sidewalk_Labs.csv', '150_SoHo_Experiential.csv', '150_Socure.csv', '150_Softheon.csv', '150_Stadium_Goods.csv', '150_Sterling_Insurance_Company.csv', '150_Story_Pirates.csv', '150_Syracuse_Police_Department.csv', '150_TG_Therapeutics,_Inc..csv', '150_TH_Experiential.csv', '150_TIEGERMAN_(formerly_School_for_Language_&_Communication_Development).csv', '150_Taglit-Birthright_Israel.csv', '150_Tailor_Brands.csv', '150_Talon_Air,_Inc..csv', '150_Tfl_Transport.csv', '150_The_Aish_Center.csv', '150_The_Bowery_Mission.csv', '150_The_Bowery_Presents.csv', '150_The_Forum_Group.csv', '150_The_Henson_Group.csv', '150_The_Hewitt_School.csv', '150_The_Morgan_Library_&_Museum.csv', '150_The_Plaza,_A_Fairmont_Managed_Hotel.csv', '150_The_Switch.csv', '150_Thieme_Group.csv', '150_TodayTix.csv', '150_Topaz_Lighting.csv', '150_Translation_LLC.csv', '150_Vasta_Global.csv', '150_Verve.csv', '150_WAVSYS.csv', '150_WFUV_Public_Radio.csv', '150_White_Ops.csv', '150_Write_Label.csv', '150_Z-Tech.csv', '150_mParticle.csv', '160_305_Fitness.csv', '160_Aetion.csv', '160_AgeWell_New_York.csv', '160_Altamarea_Group.csv', '160_American_Transit_Insurance_C.csv', '160_Applied_Data_Finance.csv', '160_Big_Spaceship.csv', '160_Catalyst_Inc.csv', '160_Civic_Entertainment_Group,_LLC_(A_Seacrest_Global_Group_Company.csv', '160_Coalition_for_Hispanic_Family_Service.csv', '160_Concordia_International_Forwarding_Corporatio.csv', '160_DFO_Global_Performance_Commerce.csv', '160_DLC_Management_Corp..csv', '160_Datalo.csv', '160_Dayton_T._Brown,_Inc.csv', '160_DeCrescente_Dist._Co.,_Inc..csv', '160_Deloitte_Tax_LLP.csv', '160_Echidna.csv', '160_Edwin_Gould_Services_for_Children_&_Familie.csv', '160_ExecOnline,_Inc..csv', '160_FIAF_-_French_Institute_Alliance_Francaise.csv', '160_Frenkel_&_Compan.csv', '160_Garfunkel_Wild,_P.C..csv', '160_GroundLin.csv', '160_Hospice_&_Palliative_Care_Buffal.csv', '160_Kindergarten_Kid.csv', '160_MSA_MODEL.csv', '160_Marymount_School_of_New_York.csv', '160_Meadowbrook_Financial_Mortgage_Bankers_Corp..csv', '160_NY_Kids_Club_and_NY_Preschool.csv', '160_NoHo_Hospitality_Group.csv', '160_Norwich_Pharma_Services.csv', '160_ONEGROUP_Risk_Management_and_Insurance.csv', '160_Oswego_Health.csv', '160_Plate.csv', '160_Property_Markets_Group.csv', '160_Public_Preparatory_Networ.csv', '160_Royal_Health_Care.csv', "160_ST._LUKE'S_ROOSEVELT_HOSPITAL.csv", '160_Sailthru.csv', '160_Skyhorse_Publishing,_Inc.csv', '160_Smithsonian_Channel.csv', '160_TDX_Construction_Corporation.csv', '160_The_IMA_Grou.csv', '160_The_Wall_Group.csv', '160_Town_of_Colonie.csv', '160_Vector_Media.csv', '160_Westcon-Comstor_North_America.csv', "160_Women_Presidents'\u200b_Organization.csv", '160_Xaverian_High_School.csv', '160_pymetrics.csv', '170_Blue_Stat.csv', '170_CDG_NY.csv', '170_Democrat_and_Chronicle_-_Part_of_the_USA_Today_Networ.csv', '170_Elite_Dail.csv', '170_Fluent,_In.csv', '170_JUV_Consultin.csv', '170_Kernel,_Created_by_Spectrum_Reac.csv', '170_Optimedia_U.csv', '170_Thrillis.csv', '180_McCann_Health_New_Yor.csv', '180_Mother_New_Yor.csv', '180_Partners_+_Napie.csv', '180_Search_Laboratory_Inc.csv', '180_United_Entertainment_Grou.csv', '18_Amalgamated.csv', '190_121_Graphic_Desig.csv', '190_Influenste.csv', '190_Orion_Worldwid.csv', '190_The_Webby_Award.csv', '190_bayarda.csv', '2,400_Fairfield_Inn_&_Suites.csv', '2,900_Department_of_Public_Wor.csv', '200_9.8_Grou.csv', '200_Captivate,_LL.csv', '200_GALE_Partner.csv', '200_H4B_Chelse.csv', '200_Horizon_Nex.csv', '200_Neon_-_An_FCB_Health_Network_Compan.csv', '200_Remedy_Health_Medi.csv', '32_Rumble.csv', '360_KS&R.csv', '57_21GRAMS.csv', '6_Gravitas.csv', '730_Wartburg.csv', '75_Foodlink.csv', '7_PTJ.csv']
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
    df.to_csv(f"/Users/danielschwartz/Desktop/simplefuture/mm_csvs/mm_NY_NoFunding/{mm}_{percent_with_up}_{all_employees}_{filename}")
  except:
    continue