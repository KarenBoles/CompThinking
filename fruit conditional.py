x=25
y=100
num1=12
num2=25
num3=87

if(num1<x):
    print('apple')

if(num2<=x):
    print('apple')
print('orange')

if(x>num3):
    print('apple')
print('orange')

if(num3>=y):
    print('apple')
print('orange')
print('pear')

if(num2==x):
    print('apple')
    print('orange')
print('pear')

if(num3-num2<2*x):
    print('apple')
else:
    print('orange')

if(num3+y<=150):
    print('apple')
    print('orange')
else:
    print('pear')

if(num3+num2+num1<124):
    print('mango')
elif(num3+num2+num1==124):
    print('pineapple')
else:
    print('pomegranate')


if(num3-num2-num1<x):
    print('strawberry')
elif(x+y-15<=num3):
    print('blueberry')
else:
    print('raspberry')


a=28
b=47
c=84

if(a<30 and c>=85):
    print('Hello')
else:
    if(b>50 or a>25):
        print('Goodbye')
    else:
        print('I cannot make up my mind')
