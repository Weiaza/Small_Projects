print("Welcome to 'Let's Speak Morse'")
i=int(input("please enter the length of what you want to translate today: "))
r=" "
for x in range(0,i,1):
    c=input("Please start entering the characters ")
    if c=='A' or c=='a':
        r=r+".- "
    if c=='B' or c=='b':
        r=r+"-... "
    if c=='C' or c=='c':
        r=r+"-.-. "
    if c=='D' or c=='d':
        r=r+"-.. "
    if c=='E' or c=='e':
        r=r+". "
    if c=='F' or c=='f':
        r=r+"..-. "
    if c=='G' or c=='g':
        r=r+"--. "
    if c=='H' or c=='h':
        r=r+".... "        
    if c=='I' or c=='i':
        r=r+".. "
    if c=='J' or c=='j':
        r=r+".--- "
    if c=='K' or c=='k':
        r=r+"-.- "
    if c=='L' or c=='l':
        r=r+".-.. "
    if c=='M' or c=='m':
        r=r+"-- "
    if c=='N' or c=='n':
        r=r+"-. "
    if c=='O' or c=='o':
        r=r+"--- "
    if c=='P' or c=='p':
        r=r+".--. "
    if c=='Q' or c=='q':
        r=r+"--.- "
    if c=='R' or c=='r':
        r=r+".-. "
    if c=='S' or c=='s':
        r=r+"... "
    if c=='T' or c=='t':
        r=r+"- "
    if c=='U' or c=='u':
        r=r+"..- "
    if c=='V' or c=='v':
        r=r+"...- "
    if c=='W' or c=='w':
        r=r+".-- "
    if c=='X' or c=='x':
        r=r+"-..- "
    if c=='Y' or c=='y':
        r=r+"-.-- "
    if c=='Z' or c=='z':
        r=r+"--.. "
    if c==' ':
        r=r+" / "
print(" ")
print("The final code is : ",r)        
        
