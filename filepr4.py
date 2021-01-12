with open ('input.txt','r') as f:
    a=f.readline()
    n=int(a)
with open ('output.txt','w') as f:
    f.write(str(n-2))
    f.write('  ')
    f.write(str( n-1))
    f.write('  ')
    f.write(str( n))
    f.write('  ')
    f.write(str(n+1))
    f.write('  ')
    f.write(str(n+2))