from numpy import insert



m=1

print('Generador de listas')
n =int(input('digame cuantas listas quiere escribir'))
x=1
z=0
listas=list()
while z<n:
    z+=1
    while x < n+1:
        print('Digame cuantas palabras tiene la lista',x)
        a = int(input())
        b=list()
        y=0
        
        while y<a:
            y+=1
            print('digame la palabra',y)
            c=input()
            b.insert(y,c)
            
        if y==a-1:
            break
            
        x+=1
        listas.append(b)
else: 
   
  for b in listas:
     print('la lista',m, b)
     m+=1

        

