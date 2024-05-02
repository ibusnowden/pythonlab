# This program displays the combinationof two number
# Ex; 5 and 3.
# REVIEW
n = int(input("Enter a integer: "))
k = int(input("Enter a integer: "))

n_result = 1
n_counter = 0
n_change = n

k_result = 1
k_counter = 0
k_change = k

while k_counter < k:
    k_result *= k_change
    k_change -= 1
    k_counter += 1

while n_counter < n:
    n_result *= n_change
    n_change -= 1
    n_counter += 1


result = n_result // (k_result * 2)
print(f"{n} choose {k} is {result}") 