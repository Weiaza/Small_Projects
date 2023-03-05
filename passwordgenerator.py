import random

special=["!","@","#","$","%","^","&","*","?","_","|"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
letters=["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]

p=''
c=''
n=''
a=''
p2=''

a1=int(input("Enter the number of alphabets you require in your password : "))
c1=int(input("Enter the number of special characters you require in your password : "))
n1=int(input("Enter the number of numbers you require in your password : "))

for i in range(0,a1):
    a=a+random.choice(letters)
p=p+a
for i in range(0,c1):
    c=c+random.choice(special)
p=p+c
for i in range(0,n1):
    n=n+random.choice(numbers)
p=p+n

tl=len(p)

p1=list(p)
random.shuffle(p1)

for i in range(0,tl):
    p2=p2+p1[i]

print(p2)
