my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
sum = 0

for row in my_list:
    for x in range(len(row)):
        sum += row[x]
    sum_list.append(sum)
print(sum_list)

"""
# Get a list of integers from the user
numbers = [int(i) for i in input('Enter numbers:').split()]

# Return a list of only even numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print(f'Even numbers only: {even_numbers}')

###################
#all(a_list) returns True if all the elements in a_list are non-zero.
Read input
num_rows = int(input())
raw_list = []
for i in range(num_rows):
    raw_list.append([int(x) for x in input().split()])

result_list =  [all(row) for row in raw_list if row != 0]# Your code goes here

print(f'All numbers: {raw_list}')
print(f'Row has no zeros: {result_list}')

#######################
# Read input
num_rows = int(input())
data_list = []
for i in range(num_rows):
    data_list.append([int(x) for x in input().split()])

aggregate_value = max([len(row) for row in data_list]) # Your code goes here

print(f'All numbers: {data_list}')
print(f'Each row has at most {aggregate_value} elements.')
"""