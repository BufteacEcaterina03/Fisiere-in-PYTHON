with open('numar.txt', 'r') as f:
    n=f.read()
x=sorted(n)
x=''.join(map(str,x))
with open('nrmin.txt', 'w') as f:
    f.write(str(x))