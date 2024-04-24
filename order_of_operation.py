
"""
For the first question: we store the expression into a 
variable named 'value' to compute the expression.
The expression in the parentheses are computed first.
After we multiply it to the floor expression which yield to zero
So the final result is zero.
"""
value = 5 // 9 * (64-32)
print(f'The value is: {value}')

"""
For this example the expression inside the parentheses is computed first of all
After we multiply the output to five. Since the numerator is greater than the
denominator the floor dvision yield to a number greater than zero.
"""
result = (64-32) * 5 // 9
print(f'The result is: {result}')

