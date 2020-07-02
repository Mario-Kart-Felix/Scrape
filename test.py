

# arr1 = [1,2,3]
# arr2 = [6,4,5]
# arr3 = []
# for i in arr1:
#   if i in arr2:
#     arr3.append(arr3.index(i))
#   else:
#     continue
  
# print(arr3)

string = "1 - 7 of 73 items"
split = 'of'
string = string.partition(split)[2]
split = 'items'
count_temp = string.partition(split)[0]
count = int(count_temp)
print(count)