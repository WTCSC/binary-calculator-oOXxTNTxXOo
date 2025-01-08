import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.div
}

def binary_calculator(bin1, bin2, operator):

    op_func = ops[operator]
    binn =  op_func(bin1,bin2)
    return binn

"""100 find the power of the 1 and convert"""
print("11111111 = 255 8-bit")
