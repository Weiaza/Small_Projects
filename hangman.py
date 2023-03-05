import random

animals=["dog","turtle","rabbit","cat","mouse","hamster","cow","duck","pig","goat","crab","deer","sheep","fish","horse","lion","tiger","giraffe","elephant"]
fruits=["apple","mango","banana","watermelon","orange","pineapple","lichi","cherry","grape","guava","strawberry","papaya","kiwi","apricot","pomegranate"]
colours=["yellow","red","blue","black","white","pink","green","violet","grey","orange","brown","purple"]

print("""Welcome....please press 1 to choose animals
                        2 to choose fruits
                        3 to choose colours""")

n=int(input("Enter choice : "))

if n==1:
    w=random.choice(animals)
    print("Number of blanks : ",len(w))
if n==2:
    w=random.choice(fruits)
    print("Number of blanks : ",len(w))
if n==3:
    w=random.choice(colours)
    print("Number of blanks : ",len(w))

errors=7
tl=len(w)
l1=[]
w2=''
print("Total Allowed Errors : 7")

for i in range(0,tl):
    l1.append("-")

while errors>0:
    s=input("Enter guessed letter : ")
    if s not in w:
        errors=errors-1
        print("Allowed errors : ",errors)
    else:
        for j in range(0,tl):
            if w[j]==s:
                l1[j]=s
        for k in range(0,tl):
            w2=w2+l1[k]
        if w2==w:
            print("Congratulations..!!!.The word is : ",w2)
            break
        else:
            print(w2)
            w2=''
            print("Allowed errors : ",errors)
        
        
    
    
