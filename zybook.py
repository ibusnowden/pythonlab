expt_samples = []

tokens = input().split()
for token in tokens:
    expt_samples.append(int(token))
  
print('Original samples:', end=' ')
for samples in expt_samples:
    print(samples, end=' ')
print()

''' Your code goes here '''
for x in expt_samples:
    if x < 40:
      expt_samples.remove(x)

print('Filtered samples:', end=' ')
for samples in expt_samples:
    print(samples, end=' ')
print()

"""
grid_size = int(input())

pattern_2d = []
for p in range(grid_size):
    row = []
    for q in range(grid_size):
        row.append('-')
    pattern_2d.append(row)

''' Your code goes here '''
for p in range(grid_size):
   for q in range(grid_size):
       if p >= q:
        pattern_2d[p][q] = 'X'
           
for row in pattern_2d:
    for cell in row:
        print(cell, end='')
    print()
"""