from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import pandas as pd
import xlrd

# company data
# book = xlrd.open_workbook('/Users/danielschwartz/Desktop/SF_csv/ideal_companies.xlsx')
# sheet = book.sheet_by_name('Sheet1')
# data = [sheet.cell_value(r, c) for c in range(sheet.ncols) for r in range(sheet.nrows)]
# data = list(dict.fromkeys(data))
# data.pop(0)
data = ['Elements Behavioral Health', 'Embark Trucks', 'Emerald Cloud Lab', 'Emissary.io', 'Emtrain.', 'Engage3', 'Enlitic', 'Enviance | a Cority company', 'Envoy.', 'Even', 'Everest Medicines', 'Everlaw.', 'EverString', 'Evidation Health', 'Excelfore Corporation', 'eXelate, A Nielsen Company', 'Exiger', 'Expanse.', 'EZ Texting', 'Farasis Energy', 'FaZe Clan', 'Feedvisor', 'Fetch Robotics', 'Fictiv', 'Fieldin', 'Figma', 'FIGS.', 'Figure', 'Firefly', 'FirstLight Fiber', 'Fivestars', 'Fleetsmith', 'FloQast', 'Fluent City', 'Flutterwave', 'Fluxx', 'FogHorn Systems, Inc', 'Food52', 'Formation', 'Fortanix', 'Forward', 'Forward Networks, Inc.', 'Fountain', 'Frame.io', 'Freenome', 'Freshly', 'Front', 'Fruit Street', 'Fuel50', 'Fulham Co., Inc.', 'Fundbox', 'Fundera', 'Fungible, Inc.', 'Galileo', 'Gamelearn', 'Genvid Technologies Inc.', 'GEO Semiconductor, Inc.', 'GetAccept', 'Ginger', 'GlassesUSA.com', 'GlassPoint Solar', 'Gloat', 'Global Communication Semiconductors,Inc.', 'Globetouch', 'Good Eggs', 'GOOD Worldwide Inc', 'Goodreads.com', 'GOQii', 'goTenna', 'Gotham Greens', 'Greenlots', 'GroundLink', 'Guesty', 'Guideline', 'GWC Inc', 'HackerEarth', 'Handshake', 'Harness', 'Headspace Inc.', 'Heal', 'Healthify', 'HealthTap', 'Hearsay Systems', 'Hello Alfred', 'Hello Heart', 'Helpshift', 'HG Insights', 'hims & hers', 'Hinge Health', 'Hitwise', 'Hive', 'HoneyBook', 'HONK Technologies', 'HOVER Inc.', 'Human Longevity, Inc.', 'Humu', 'Hustle', 'IceKredit, Inc. (上海冰鉴信息科技有限公司)', 'Ike', 'Imbellus', 'Imply', 'Inbenta', 'Inceptio', 'Incorta', 'Indeni', 'inDriver', 'Infoworks.io', 'InMarket', 'Inscopix, Inc.', 'Insightly', 'Inspire', 'Instapage', 'Instawork', 'Internet Archive', 'Invoice2go', 'IP Infusion', 'IPSY', 'Issuu', 'Jamcracker', 'Jetty', 'Jio Health', 'JOOR', 'Jopwell', 'Joveo', 'Jumpstart', 'Jun Group', 'JustAnswer', 'Kaia Health', 'KaiOS Technologies, Inc.', 'Karius', 'Kasisto, Inc.', 'Kettlebell Kitchen', 'Kika Tech, Inc.', 'Kinetica', 'Kitchen United', 'Knock', 'Komprise', 'Kongregate', 'Lastline, Inc.', 'Latch', 'Lattice', 'Le Tote', 'LeafLink', 'LeanData, Inc.', 'Legend3D', 'LetsGetChecked', 'Lever', 'Limelight Health', 'Linden Lab', 'Litify', 'LiveAction - Network Performance Management', 'Localize.city', 'LogDNA', 'Logikcull.com', 'Loom', 'Lumina Networks', 'LvYue Group', 'Lyric', 'M.M.LaFleur', 'MAANA', 'Mad Street Den', 'Magic, Inc', 'Magzter', 'Mainspring Energy', 'Makani', 'Make School', 'Maker Studios Inc', 'Managed by Q', 'ManyChat', 'Mapbox', 'Marco Polo', 'Mark43', 'Marketing Evolution', 'MATRIXX Software', 'MaxPreps', 'MAZ Systems Inc.', 'mCube, Inc.', 'Memphis Meats', 'MenuSifu', 'method products pbc', 'Mettl', 'MeUndies', 'MFour Mobile Research', 'Mindstrong', 'MindTickle', 'MindTouch', 'Mint House', 'Miro', 'Mixmax', 'Mode', 'Modern Health', 'Modsy', 'MoEngage Inc.', 'Mojo Vision Inc.', 'MomentFeed', 'Movable Ink', 'MURAL', 'Mynd Property Management', 'Myspace', 'Narvar', 'Nativo Inc', 'Need More Leads?', 'Netomi', 'Neural Analytics', 'News Break', 'Newsela', 'NEXT Trucking', 'NGINX, Inc.', 'Nitro, Inc.', 'Nom Nom', 'Nor1', 'NoRedInk', 'NotCo', 'Nova Credit', 'NS1', 'Nuna Inc.', 'NuORDER', 'Nuro', 'Nurx', 'Nylas', 'Observe.AI', 'Octane Lending', 'ODK Media, Inc', 'OKCoin', 'Olapic', 'One Concern', 'Onerent', 'OODA Health', 'OpsRamp', 'Optimove', 'Orchard', 'Orion Labs', 'Oro Inc.', 'Osmo', 'otonomo', 'Outdoor Voices', 'OverOps', 'Owkin', 'Owler', 'Packet, an Equinix Company', 'PACT Pharma', 'PandaDoc', 'Parachute Home', 'Parsable', 'Parsley Health', 'PatientPop Inc.', 'PayJoy', 'PCH International', 'PebblePost', 'Peek', 'PeerStreet', 'People.ai', 'PerimeterX', 'PetDesk', 'Phone.com', 'Photomath', 'Pill Club', 'Pilot', 'PingCAP', 'Pipefy', 'Pivot Bio', 'Plated', 'Platzi', 'Playdom', 'Plenty', 'Plus.ai', 'Point', 'Polaris Networks', 'Pony.ai', 'Postman', 'Preempt Security', 'Premise Data', 'Primer.ai', 'productboard', 'Proficio', 'Propertybase', 'Prose', 'Proven Recruiting', 'Provivi, Inc.', 'Proxy', 'Puls', 'Punchh', 'pymetrics', 'Qualia', 'Quip', 'quip.', 'Rainforest QA', 'Raken', 'Rakuten Medical', 'RapidAPI', 'RapidSOS', 'RapidValue', 'Real Capital Analytics', 'Reali', 'RebelMouse', 'Recurly', 'Reflektive', 'Relativity Space', 'Remesh', 'Remix', 'Resilinc', 'Restaurant365', 'Resy', 'Retail Solutions Inc.', 'Returnly', 'Revel', 'Revinate', 'RevJet', 'Rhino', 'Ridecell', 'Rippling', 'Ritual', 'Ro', 'Roadster', 'Rocketrip', 'Rokt', "Rothy's", 'Rumble', 'Sailthru', 'Saviynt', 'SchoolMint', 'Scoop Technologies, Inc.', 'Scout RFP, a Workday company', 'SeatGeek', 'Second Measure', 'SECURITI.ai', 'Securly', 'Seriously Digital Entertainment', 'Seven Lakes Technologies', 'SEVENROOMS', 'Shield AI', 'ShieldX Networks', 'Shortlist Professionals', 'Side', 'Siemplify', 'Sigma Computing', 'Signal Sciences', 'Signals Analytics', 'Simon Data', 'Simpplr', 'SinglePlatform', 'Singular', 'SirionLabs', 'Sitetracker', 'Skip', 'Skydio', 'Skyroam', 'SlashNext', 'Slice Labs', 'SmartAsset', 'SmugMug', 'SnackNation', 'Snackpass', 'Soft Robotics Inc.', 'Soko', 'SoloLearn', 'Somnoware', 'Speakap', 'SpinLaunch', 'Spire Technologies', 'Splice', 'SpokenLayer', 'Sqreen', 'SquareFoot', 'Stampli', 'Standard Cognition', 'States Title', 'Stella Connect', 'StradVision', 'StyleSeat', 'Sunbit', 'Superhuman', 'Supplyframe', 'Suzy', 'Sweeten', 'Swift Health Systems Inc.', 'Swift Navigation', 'Swiftly, Inc.', 'Symphony AyasdiAI', 'Tacit Knowledge', 'Tailor Brands', 'talech', 'Tally Inc', 'Talview', 'Tapad', 'TeleSign', 'Tempo Automation', 'Tend', 'Terminal', 'The Financial Gym', 'The Muse', 'The Sill', 'The Wing', 'theSkimm', 'ThirdLove', 'Tia', 'TicketManager', 'Tigera', 'TodayTix', 'Tonal', 'Touch of Modern', 'Trimble Consulting', 'Triplebyte', 'True Link Financial', 'Truvalue Labs', 'Tubular Labs', 'TuneCore', 'Turvo Inc.', "Two Chairs (We're hiring!)", 'Umbo Computer Vision', 'Unbound Tech', 'Unifonic Inc', 'Unmetric', 'Unqork', 'UNTUCKit', 'Upfluence', 'UserZoom', 'UVeye', 'Van Leeuwen Ice Cream', 'Verkada', 'Versa Networks', 'Vettery', 'Vim', 'Vineti', 'Virta Health', 'ViSenze - AI for Visual Commerce', 'Vivino', 'Volansi', 'Volta Charging', 'Voyage', 'VSCO®', 'Vudu - Movies & TV', 'Wandera', 'WanderJaunt', 'WayUp', 'Waze', 'Webflow', 'Weee!', 'WellNow Urgent Care', 'Whatfix', 'WhiteSource', 'WineDirect', 'Within (VR/AR)', 'Womply', 'Xertica', 'Yamibuy.com', 'Yellowbrick Data', 'YipitData', 'YouAppi', 'YourMechanic', 'YOUXIN FINANCIAL', 'Zeel.com', 'Zenlayer', 'ZeroCater', 'Zeus Living', 'ZineOne, Inc.', 'Zinier', 'ZINIO', 'Zipari', 'ZL Technologies', 'ZOOM Media']

# company = input("Enter a Company: ")
# print(d)
# company = d
# strcompany = str(company)


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://app.apollo.io/#/login?redirectTo=https%3A%2F%2Fapp.apollo.io%2F%23%2Fonboarding%2Fbulk%3F_k%3Dnbfzqc&_k=hpz0x5")

time.sleep(2)
driver.maximize_window()
time.sleep(1)
logIn = driver.find_element_by_name("email")

logIn.click()

driver.find_element_by_name('email').send_keys('daniel@oursimplefuture.com')
driver.find_element_by_name('password').send_keys('Cessnap1Cessnap1')
logIn = driver.find_element_by_class_name("zp_2z1mP")

time.sleep(1)

logIn.click()

time.sleep(2)

search = driver.find_element_by_class_name("zp_MIz8G")

for d in data:
  company = d
  strcompany = str(company)
  search.click()

  search.send_keys(company)
  time.sleep(3)
  search.send_keys(Keys.RETURN)

  time.sleep(2)
  employees = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/span[1]')
  total_employees = str(employees.get_attribute("innerText"))
  print(total_employees)
  num_total_emp = total_employees.split()[0]
  print(num_total_emp)
  employees.click()


  time.sleep(1)
  numemp = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/span/a/span[1]')
  numempstr = str(numemp.get_attribute('innerText'))
  # numempstr.replace(" ", "_")
  numempint = 0
  try:
    numempint = int(float(numempstr))
  except:
    numempint = 126
  print(numempstr)
  name_array=[]
  role_array=[]
  home_array=[]
  tr=1
  for i in [1,2,3,4,5]:
    print("in loop")
    try:
      print("in try")
      
      
      # define employees
      employees = driver.find_elements_by_xpath('//*[@href]')
      # print employees
      for e in employees:
        while tr < 26:
          employee_name = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[1]/div/div[2]/div[3]/div/a')
          employee_role = driver.find_element_by_xpath(f'//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[{tr}]/td[2]')
          
          name_array.append(employee_name.get_attribute('innerText'))
          role_array.append(employee_role.get_attribute('innerText'))

          print(employee_name.get_attribute('innerText'))
          print(employee_role.get_attribute('innerText'))
          
          employee_role.click()
          try:
            employee_home = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]')
            home_array.append(employee_home.get_attribute('innerText'))
            # print(employee_home.get_attribute('innerText'))
          except Exception:
            home_array.append('NA')
            # print(employee_home.get_attribute('innerText'))
          tr=tr+1
      print("scroll down")
      elemen = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/span/div/div[3]')
      driver.execute_script("return arguments[0].scrollIntoView(true);", elemen)
      print("before sleep")
      time.sleep(1)
      print("after sleep")
      # define next
      nex = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/span/div/div[3]')
      # click next
      nex.click()
      time.sleep(1)
      
      element = driver.find_element_by_xpath('//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div[3]/div/a')
      driver.execute_script("return arguments[0].scrollIntoView(true);", element)
      
      tr = 2
    except:
      print("in except")
      ['NA' if x=='' else x for x in name_array]
      ['NA' if x=='' else x for x in role_array]
      ['NA' if x=='' else x for x in home_array]
      print(name_array)
      print(role_array)
      print(home_array)
      np_name_array = np.array(name_array)
      np_role_array = np.array(role_array)
      np_home_array = np.array(home_array)
      # print(np_name_array)
      # print(np_role_array)
      # print(np_home_array)
      str_company = strcompany.replace(" ", "_")
      df = pd.DataFrame({"name" : np_name_array, "role" : np_role_array, "city" : np_home_array})
      df.to_csv(f"/Users/danielschwartz/Desktop/SF_csv2/{num_total_emp}_{str_company}.csv")
      # driver.quit()

    

  ['NA' if x=='' else x for x in name_array]
  ['NA' if x=='' else x for x in role_array]
  ['NA' if x=='' else x for x in home_array]
  # print(name_array)
  # print(role_array)
  # print(home_array)
  np_name_array = np.array(name_array)
  np_role_array = np.array(role_array)
  np_home_array = np.array(home_array)
  print(np_name_array)
  print(np_role_array)
  print(np_home_array)
  str_company = strcompany.replace(" ", "_")
  df = pd.DataFrame({"name" : np_name_array, "role" : np_role_array, "city" : np_home_array})
  df.to_csv(f"/Users/danielschwartz/Desktop/SF_csv2/{num_total_emp}_{str_company}.csv")
  # driver.quit()
  if numempint > 125:
    ok = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[2]/div/div/div')
    ok.click()
  