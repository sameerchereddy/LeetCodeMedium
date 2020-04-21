import sys
def myAtoi(str):
    returnValue=""
    sysMaxSize = 2**31
    for i in range(0,len(str)):
        charVal = str[i]
        if(charVal==" " and returnValue==""):
            continue
        elif(charVal=="+" or charVal=="-"):
            if(len(returnValue)==0):
                returnValue = returnValue+charVal
            elif(returnValue=="+" or returnValue=="-"):
                return 0
            else:
                break
        elif(charVal.isdigit()):
            returnValue= returnValue+charVal
        else:
            break
    if(returnValue=="" or returnValue=="+" or returnValue=="-"):
        return 0
    if(int(returnValue)< (-1*(sysMaxSize))):
        return (-1*(sysMaxSize))
    if(int(returnValue)> sysMaxSize-1):
        return sysMaxSize-1

    return int(returnValue)


print(myAtoi("+_5+0+030000000000"))







