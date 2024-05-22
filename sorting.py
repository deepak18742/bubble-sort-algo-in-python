# BUBBLE SORING

list_of_number = [1,23,3,17,-1,50,-2]

for i in range(len(list_of_number)):
    for j in range(len(list_of_number)):
    
      if list_of_number[i] < list_of_number[j]:
            temp =list_of_number[i]
            list_of_number[i] =list_of_number[j]
            list_of_number[j] =temp
print(list_of_number)