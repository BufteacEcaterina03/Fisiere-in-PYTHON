with open ('globulete.txt' , 'r') as f:
    a1=f.readline()
    r= int(a1) +3            
    s1= int(a1) +r           
    a2= s1 -2               
    s2= int(a1)+r+a2 
with open ('bradut.txt', 'w') as f:
    f.write(str(s2))    