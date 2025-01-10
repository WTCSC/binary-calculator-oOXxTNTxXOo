import operator
import math
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
bin1 = "00000011"
bin2 = "00000111"
operator = "/" 

def checker(x): #verifies that the string is a binary code 
        if len(x) != 8: #could work better with fromat becasue can check for 101 binary numbers 
            return False
        for i in x:
            if str(i) == "1":
                i=i
            elif str(i) == "0":
                i=i
            else:
                return False

def opchecker(x):
    return 

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
    if checker(bin1) == False: #checks if binary number is a 8-bit binary number or not
        return "Error"
    elif checker(bin2) == False:
        return "Error"
    elif opchecker(operator) == False:
        return "Error"
    op_func = ops[operator] #checks for operator value

    if operator == "/": #checks for dived by zero 
        if convert(bin2) == 0:
            return "NaN"

    binn = math.floor(op_func(convert(bin1),convert(bin2))) #does binary number math
    print(convert(bin1),convert(bin2))
    
    if binn >= 256: #verifies that number is with 8-bit binary range //could work better if checked for within range
        return "Overflow"
    elif binn < 0: #verifies that number greater than 0
        return "Overflow"

    binn = reconvert(binn)
    return binn

print(binary_calculator(bin1, bin2, operator))
#dosent handle all zeros 000000000
