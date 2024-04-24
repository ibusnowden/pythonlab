S = input()
lc = {}
    
for letter in S:
    if letter in lc:
        lc[letter] += 1
    else:
        lc[letter] = 1
    
for i in range(1, len(S) + 1):
    count_i = 0
        
    for count in lc.values():
        if count == i:
            count_i += 1
    
    if count_i not in [0, 2]:
       print("No")
       
print("YES")


