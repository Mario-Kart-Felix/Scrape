import xlrd

book = xlrd.open_workbook('/Users/danielschwartz/Desktop/SF_csv/ideal_companies.xlsx')
sheet = book.sheet_by_name('Sheet1')
data = [sheet.cell_value(r, c) for c in range(sheet.ncols) for r in range(sheet.nrows)]
data = list(dict.fromkeys(data))
data.pop(0)

print(data)






# city = ['Southampton, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'Southampton, NY', 'Southampton, NY', 'New York, NY', 'New York, NY', 'Stamford, CT', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY']
# print(len(city))


# name = ['Mohamed Aly', 'Barnaby', 'Charles Rogers', 'Tom Hunter', 'Alex Nephew', 'Megan Sacks', 'Andrew Ermogenous', 'Eugene Wu', 'Eric Christianson', 'Jane Mikus', 'Aria Ertefaie', 'Colin George', 'Mike Shimerda', 'Fanny Chen', 'Alan Freeman', "Casey O'Hanlon", 'Joe Gallagher', 'Jeremy Kowalski', 'Valentin Roduit', 'Gai Ho', 'Joel Raha', 'Zach Weiss', 'Malte Gabriel', 'Erin Crapser', 'Benjamin Bein', 'Marcin Kloc']
# print(len(name))


# job = ['Cloud Security Architect', 'Director Of Engineering', 'Software Research', 'Product', 'President & Co-Founder', 'Director, Customer Success', 'Director, CRE', 'Data Scientist', 'Chief Financial Officer', 'Customer Success Associate', 'Equity Analyst', 'Head Of Real Estate', 'Director, Strategic Partnerships', 'Talent Acquisition, Corporate & Technical', 'VP, Data Products', 'Executive Assistant To Chief Executive Officer', 'Business Development', 'Director - Business Development', 'Sales Director', 'Senior Graphic Designer', 'Senior Vice President Of Engineering', 'Customer Success Manager', 'Product Management', 'VP, Marketing', 'Data Scientist', 'Director, IT and Security Operations']
# print(len(job))