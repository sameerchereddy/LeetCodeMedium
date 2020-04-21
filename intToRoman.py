def intToRoman(num):   
    numList = makeNumList(num)
    returnString=""
    for num in numList:
        if(num>=1000):
            thou = thousands(num)
            returnString = returnString+thou
        elif(num>99 and num<1000):
            hun = hundreds(num)
            returnString = returnString+hun
        elif(num<100 and num>9):
            ten = tens(num)
            returnString = returnString+ten
        elif(num<10):
            dig = digit(num)
            returnString = returnString+dig
        else:
            break
    return returnString
def thousands(num):
    numThous = num//1000
    return "M"*numThous
def hundreds(num):
    numHuns = num//100
    if(numHuns<4):
        return "C"*numHuns
    elif(numHuns==4):
        return "CD"
    elif(numHuns>5 and numHuns<9):
        return "D" + ("C"*(numHuns-5))
    elif(numHuns==9):
        return "CM"
    elif(numHuns==1):
        return "C"
    elif(numHuns==5):
        return "L"
def tens(num):
    numTens = num//10
    if(numTens<4):
        return "X"*numTens
    elif(numTens==4):
        return "XL"
    elif(numTens>5 and numTens<9):
        return "L" + ("X"*(numTens-5))
    elif(numTens==9):
        return "XC"
    elif(numTens==1):
        return "X"
    elif(numTens==5):
        return "L"
def digit(num):
    if(num<4):
        return "I"*num
    elif(num==4):
        return "IV"
    elif(num>5 and num<9):
        return "V" + ("I"*(num-5))
    elif(num==9):
        return "IX"
    elif(num==1):
        return "I"
    elif(num==5):
        return "V"


def makeNumList(num):
    numList=[]
    k=1
    while num>0:
        numList.append((num%10)*k)
        num = num//10
        k=k*10
    reversedNumList = numList[::-1]
    return reversedNumList


print(intToRoman(500))
