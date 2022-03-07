
P=int(input('Enter principal amount'))
r=float(input('Enter rate of interest'))
n=int(input('Enter no of years'))


A=P*((1+(r/100))**n)

C=A-P

print('\n')
print('The compound interest  is :',round(C))

