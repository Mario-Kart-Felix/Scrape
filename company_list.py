import os
import csv
import numpy as np
from ast import literal_eval
import pandas as pd

big_array = []
total = 0
total_people_searched = 0
for company in sorted(os.listdir('/Users/danielschwartz/Desktop/Simplefuture/mm_csvs/2nd_release/mm_mass_2')):
  with open(os.path.join('/Users/danielschwartz/Desktop/Simplefuture/mm_csvs/2nd_release/mm_mass_2', company)) as csvfile:
    data = list(csv.reader(csvfile))
  csv_array = []
  c = company.split('_')[3:]
  c = ' '.join(c)
  c = c[:-4]
  csv_array.append(c)
  total_people = company.split('_')[2]
  # csv_array.append(round(total_people))
  percentage = company.split('_')[1]
  percentage = percentage.split('_')[0]
  percentage = int(percentage) / 100
  total_people_with_up = percentage * int(float(total_people))
  portion_people = 0
  company_total_dollars = 0
  # print(data)
  company_portion_dollars = 0
  
  for person in data[1:]:
    portion_people+=1
    person_total_dollars = 0
    over_under = person[-1]
    over_under = literal_eval(over_under)
    # print(over_under)
    for value in over_under:
      if value == 'Unknown':
        person_total_dollars += 100
      elif value == 'Over':
        person_total_dollars += 200
      elif value == 'Under':
        person_total_dollars += 50
      elif value == 'Less':
        person_total_dollars += 50
      else:
        person_total_dollars = 100
    # print(person_total_dollars)
    company_portion_dollars+=person_total_dollars
  if portion_people >= 10 and percentage != 0:
    total_company_dollars = (int(total_people)/int(portion_people)) * company_portion_dollars
    csv_array.append(str(round(percentage * 100))+"%")
    csv_array.append("$"+str(round(total_company_dollars)))
    csv_array.append('MA')
    big_array.append(csv_array)
    total+=total_company_dollars
    total_people_searched+=portion_people
  else:
    total_people_searched+=portion_people
    continue  

np_big_array = np.array(big_array)
df = pd.DataFrame(np_big_array, columns = ['Company Name', 'Percentage With UP', 'Total Money', 'State'])
df.to_csv("/Users/danielschwartz/Desktop/mass_2.csv")
print(big_array)
print(total)
print(total_people_searched)