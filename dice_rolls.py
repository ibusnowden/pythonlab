first = int(input("How many sides are on your fisrt die? "))
second = int(input("How many sides are on your second die? "))
count = 0
dice = 1 
print("Possible rolls: ")

while dice <= first:
    for i in range(count, second):
        count = count + 1 
        print(f"{dice}, {count}")  
    dice = dice + 1 
    count = count - second


