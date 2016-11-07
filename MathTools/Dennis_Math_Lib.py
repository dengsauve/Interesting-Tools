###########################################
# Synthetic Division Testing Method
# Because testing 0's by hand sucks
# Requires list of polynomial coefficients
# from highest factor to constant in
# descending order. Also, only one zero.


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
