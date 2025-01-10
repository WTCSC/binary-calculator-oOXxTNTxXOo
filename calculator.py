import operator
import math

#dictionaries 
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

#functions
def checker(x): #verifies that the string is a binary code 
        for i in x:
            if str(i) == "1" or str(i) == "0":
                i=i
            else:
                return False

def opchecker(x): #checks for operator value to verify that the operator is either a +, -, *, /
    try: 
        ops[x]
        return ops[x]
    except:
        return False

def convert(Io): #converts binary numbers into readable base 10 numbers
    x = 0
    for idx, i in enumerate(list(reversed(Io))):
        x = x + int(i)*(2**idx)
    return x

def reconvert(Io): #converts base 10 numbers into binary numbers
    x = 7
    tot = []
    while x >= 0:
        if Io >= 2**x:
            tot.append("1")
            Io = Io - (2**x)
        else:
            tot.append("0")
        x = x-1
    return "".join(tot)

def binary_calculator(bin1, bin2, operator): #function to calculate binary numbers whether added, subtracted, divided, or multiplied.
    if checker(bin1) == False or checker(bin2) == False or opchecker(operator) == False: #checks if binary number is a 8-bit binary number or not
        return "Error"
    try:
        binn = math.floor(opchecker(operator)(convert(bin1),convert(bin2))) #does binary number math || also performs flooring on the final number
    except:
        return "NaN"
    if binn >= 256 or binn < 0: #chekcs whether calculated number is in range of 255-0
        return "Overflow"
    binn = reconvert(binn)
    return binn