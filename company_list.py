import os
import csv
import numpy as np
from ast import literal_eval
import pandas as pd

big_array = []
for company in sorted(os.listdir('/Users/danielschwartz/Desktop/simplefuture/mm_csvs/mm_NY_NoFunding')):
  with open(os.path.join('/Users/danielschwartz/Desktop/simplefuture/mm_csvs/mm_NY_Nofunding', company)) as csvfile:
    data = list(csv.reader(csvfile))
  csv_array = []
  c = company.split('_')[3]
  c = c.split('.')[0]
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
        person_total_dollars = int(value.split('$')[1])
    # print(person_total_dollars)
    company_portion_dollars+=person_total_dollars
  if portion_people >= 10:
    total_company_dollars = (int(total_people)/int(portion_people)) * company_portion_dollars
    csv_array.append(portion_people)
    csv_array.append(round(total_people_with_up))
    csv_array.append(round(total_company_dollars))
    print("######################################")
    big_array.append(csv_array)
  else:
    continue  
np_big_array = np.array(big_array)
df = pd.DataFrame(np_big_array, columns = ['Company Name', 'Portion Employees Checked', 'Total With UP', 'Total Money'])
df.to_csv(f"/Users/danielschwartz/Desktop/simplefuture/aggregate_csv2.csv")

print(big_array)