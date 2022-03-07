def findupper(str):
    #str='AnuSunny'
    count=0

    for i in str:
        if i.isupper():
            count=count+1
    return count



def findlower(str):
    #str='AnuSunny'
    count=0

    for i in str:
        if i.islower():
            count=count+1
    return count