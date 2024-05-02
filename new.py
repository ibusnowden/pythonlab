''' Type your code here. '''
e = input().split()
s = ['Done', 'done', 'd']
while True:
    e = input().split()
    if e in s:
        break
    else:
       t = e[::-1]
    print(t)