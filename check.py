# Read input and split input into tokens
tokens = input().split()

input_list = []
for token in tokens:
    input_list.append(int(token))

print(f'Sequence: {input_list}')
for x in range(1, len(input_list)-1, 1):
    if input_list[x]  > input_list[x-1] and input_list[x]  > input_list[x+1]:
        print(f'Knob: {input_list[x-1]} {input_list[x]} {input_list[x+1]}')

        # iterate using enumerate
        for index, item in enumerate(input_list):
            print(index, item)