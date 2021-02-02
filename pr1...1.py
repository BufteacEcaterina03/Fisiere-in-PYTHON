with open('lista1.txt','r')as f:
    a=list(f.read())
b=a.count('0')
c=a.count('2')
d=a.count('4')
e=a.count('6')
f=a.count('8')
n=b+c+d+e+f
with open('nr.pare.txt','w')as f:
    f.write(f'Nr de cifre pare =[\{n}')
b=a.count('1')
c=a.count('3')
d=a.count('5')
e=a.count('7')
f=a.count('9')
n=b+c+d+e+f
with open('nr.impare.txt','w')as f:
    f.write(f'Nr de cifre impare =[\{n}')