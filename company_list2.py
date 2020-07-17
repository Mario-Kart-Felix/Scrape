import os
import csv
import numpy as np
from ast import literal_eval
import pandas as pd


for company in sorted(os.listdir('/Users/danielschwartz/Desktop/Simplefuture/mm_csvs/mm_layoffs')):
  with open(os.path.join('/Users/danielschwartz/Desktop/Simplefuture/mm_csvs/mm_layoffs', company)) as csvfile:
    data = list(csv.reader(csvfile))
  big_array = []
  c = company.split('_')[3:]
  c = ' '.join(c)
  c = c[:-4]
  
  for person in data[1:]:
    csv_array = []
    csv_array.append(person[2])
    print(person[2])
    if len(person[3]) > 2:
      csv_array.append(u'\u2713')
    else:
      csv_array.append('')


    big_array.append(csv_array)

  np_big_array = np.array(big_array)
  df = pd.DataFrame(np_big_array, columns = ['Name', 'Has Unclaimed Property'])
  df.to_csv(f'/Users/danielschwartz/Desktop/Simplefuture/csv_for_company/layoffs/{c}.csv')
