###########################################
# Synthetic Division Testing Method
# Because testing 0's by hand sucks
# Requires list of polynomial coefficients
# from highest factor to constant in
# descending order. Also, only one zero.
import math

def synthetic_division(coefficients, zero):
    x = float(coefficients[0])
    for i in range(1, len(coefficients)):
        x = (x * zero) + float(coefficients[i])
    return x


def get_coefficients():
    c, return_list = '', []
    while c != 'f':
        c = input("f to finish; enter a co-efficient: ")
        if c != 'f':
            return_list.append(float(c))
    return return_list

def reverse_polish(input_stack):
    #Requires input_stack to be a list.
    f = {
		'+': lambda t, b: b + t,
		'-': lambda t, b: b - t,
		'*': lambda t, b: b * t,
		'/': lambda t, b: b / t,
		'//':lambda t, b: b // t,
		'%': lambda t, b: b % t,
		'^': lambda t, b: b ** t}
    short_stack = []
    for i in input_stack:
        if i == '!':short_stack.append(math.factorial(short_stack.pop()))
        elif i in f:
            t, b = short_stack.pop(), short_stack.pop()
            short_stack.append(f[i](t, b))
        else:short_stack.append(float(i))
    return short_stack[0] if len(short_stack) == 1 else 'failed'
