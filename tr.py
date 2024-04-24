"""
count = 1
count1 = 1
dice1 = 1
dice2 = 2


for i in range (0, 6):
    print(dice1, count)
    count += 1

for i in range (0, 6):
    print(dice2, count1)
    count1 += 1

#################
food_record = {'plum': 1, 'carrot': 3, 'celery': 2, 'oatmeal': 4}
grade_scale = {1: 'great', 2: 'good', 3: 'fair', 4: 'poor'}

food_name = input()

''' Your code goes here '''
food_num = food_record.pop(food_name, -1)
patient_grade = grade_scale.get(food_num, 'no info')


print(f'{food_name} is {food_num} ({patient_grade})')
print('Remaining food:')
print(food_record)
"""
orders_record = {}

''' Your code goes here '''
while True:
    i = input()
    if i == 'quit':
        break
    key, value = i.split()
    orders_record[key] = value
   

print('Orders record:')
print(orders_record)