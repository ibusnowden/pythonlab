import random

def main():
    new_list = []

    for x in range(5):
        row = []
        for y in range(4):
            number = random.randint(0, 9)
            row.append(number)
        new_list.append(row)

    for row in range(5):
        for column in range(4):
            print(new_list[row][column])
    
    print("Total values of each row")
    for row in range(5):
        row_total = 0
        for column in range(4):
            row_total += new_list[row][column]
        print(f"Row {row+1}: {row_total}")
    print()

    print("Total values of each column")
    for column in range(4):
        column_total = 0
        for row in range(5):
            column_total += new_list[row][column]
        print(f"Column  {column+1}: {column_total}") 

main()


"""
total_row = 0
total_column = 0
new_list = []

for i  in range(0, 5):
  numbers = list([random.randint(0, 9)]*4)
  new_list.append(numbers)

for m in range(len(new_list)):
  for n in range(len(new_list[m])):
    print(new_list[m][n])

"""
   


  