#import mysql.connector as mysql
from tkinter import *
import random
from tkinter import messagebox

#db=mysql.connect(host="localhost",
#                 user="root",
#                passwd="weiaza",
#                database="Project")

#cur=db.cursor()

root=Tk()

root.title("Memory Game")
root.geometry('500x500')
root['bg']='#FFF5C2'

pframe=Frame(root)
pframe.pack(pady=10)
t="Hello...!!! Welcome to the game. Please enter your name..."

lbl1=Label(pframe,text=t,bg='#FFF5C2',font=("Georgia",14)).pack()
e=Entry(root)
e.pack()
e.get()
    

def easy():
    global count,ans_list,ans_dict,c
    global matches
    global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11
    global play_frame
    global fin_label

    
    rt=Toplevel()
    rt.title("Let's Play "+e.get()+"...!!!")
    rt.geometry('500x500')
    
    rt.wm_attributes("-topmost", 1)
 
    matches=[1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)

    play_frame=Frame(rt)
    play_frame.pack(pady=10)

    count=0
    c=0
    ans_list=[]
    ans_dict={}

    def click(b,number):
        global count,ans_list,ans_dict
        global matches
        global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11

        if b['text']=='' and count<2:
            b['text']=matches[number]
            ans_list.append(number)
            ans_dict[b]=matches[number]
            count=count+1
        
        if len(ans_list)==2:
            if matches[ans_list[0]]==matches[ans_list[1]]:
                messagebox.showinfo("MATCHED!!!","!!! BRILLIANTLY PLAYED  !!!")
                fin_label.config(text='MATCH!!!',font=("Century",16))
                #q="Update memory set scores=scores+2 where player_name=('{}')".format(e.get(),)
                #cur.execute(q)
                #db.commit()
                
                for key in ans_dict:
                    key['state']='disabled'
                count=0
                ans_list=[]
                ans_dict={}
            else:
                count=0
                ans_list=[]

                messagebox.showinfo("!!!","Incorrect!!!")

                
                for key in ans_dict:
                    key['text']=''

                ans_dict={}

    b0=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b0,0))
    b1=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b1,1))
    b2=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b2,2))
    b3=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b3,3))
    b4=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b4,4))
    b5=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b5,5))
    b6=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b6,6))
    b7=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b7,7))
    b8=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b8,8))
    b9=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b9,9))
    b10=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b10,10))
    b11=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b11,11))

    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=1,column=3)

    b8.grid(row=2,column=0)
    b9.grid(row=2,column=1)
    b10.grid(row=2,column=2)
    b11.grid(row=2,column=3)

    fin_label=Label(rt,text='')
    fin_label.pack(pady=20)

def medium():
    global count,ans_list,ans_dict,c
    global matches
    global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11
    global play_frame
    global fin_label

    
    rt=Toplevel()
    rt.title("Let's Play...!!!")
    rt.geometry('500x500')
    
    rt.wm_attributes("-topmost", 1)
 
    matches=[1.5,1.5,-29,-29,6.3,6.3,0.74,0.74,5.2,5.2,16,16]
    random.shuffle(matches)

    play_frame=Frame(rt)
    play_frame.pack(pady=10)

    count=0
    c=0
    ans_list=[]
    ans_dict={}

    def click(b,number):
        global count,ans_list,ans_dict
        global matches
        global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11

        if b['text']=='' and count<2:
            b['text']=matches[number]
            ans_list.append(number)
            ans_dict[b]=matches[number]
            count=count+1
        
        if len(ans_list)==2:
            if matches[ans_list[0]]==matches[ans_list[1]]:
                fin_label.config(text='MATCH!!!',font=("Century",16))
                #q="Update memory set scores=scores+2 where player_name=('{}')".format(e.get(),)
                #cur.execute(q)
                #db.commit()
                
                for key in ans_dict:
                    key['state']='disabled'
                count=0
                ans_list=[]
                ans_dict={}
            else:
                count=0
                ans_list=[]

                messagebox.showinfo("!!!","Incorrect!!!")

               
                for key in ans_dict:
                    key['text']=''

                ans_dict={}

    b0=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b0,0))
    b1=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b1,1))
    b2=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b2,2))
    b3=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b3,3))
    b4=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b4,4))
    b5=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b5,5))
    b6=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b6,6))
    b7=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b7,7))
    b8=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b8,8))
    b9=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b9,9))
    b10=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b10,10))
    b11=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b11,11))

    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=1,column=3)

    b8.grid(row=2,column=0)
    b9.grid(row=2,column=1)
    b10.grid(row=2,column=2)
    b11.grid(row=2,column=3)

    fin_label=Label(rt,text='')
    fin_label.pack(pady=20)

def tough():
    global count,ans_list,ans_dict,c
    global matches
    global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11
    global play_frame
    global fin_label

    
    rt=Toplevel()
    rt.title("Let's Play...!!!")
    rt.geometry('600x780')
    
    rt.wm_attributes("-topmost", 1)
 
    matches=[1.5,1.5,-29,-29,6.3,6.3,0.74,0.74,5.2,5.2,16,16,7.9,7.9,3.42,3.42,-0.11,-0.11,547,547,984,984,365,365,-99,-99,3.14,3.14,857,857]
    random.shuffle(matches)

    play_frame=Frame(rt)
    play_frame.pack(pady=10)

    count=0
    c=0
    ans_list=[]
    ans_dict={}

    def click(b,number):
        global count,ans_list,ans_dict
        global matches
        global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11

        if b['text']=='' and count<2:
            b['text']=matches[number]
            ans_list.append(number)
            ans_dict[b]=matches[number]
            count=count+1
        
        if len(ans_list)==2:
            if matches[ans_list[0]]==matches[ans_list[1]]:
                fin_label.config(text='MATCH!!!',font=("Century",16))
                #q="Update memory set scores=scores+2 where player_name=('{}')".format(e.get(),)
                #cur.execute(q)
                #db.commit()
                
                for key in ans_dict:
                    key['state']='disabled'
                count=0
                ans_list=[]
                ans_dict={}
            else:
                count=0
                ans_list=[]

                messagebox.showinfo("!!!","Incorrect!!!")

               
                for key in ans_dict:
                    key['text']=''

                ans_dict={}

    b0=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b0,0))
    b1=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b1,1))
    b2=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b2,2))
    b3=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b3,3))
    b4=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b4,4))
    b5=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b5,5))
    b6=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b6,6))
    b7=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b7,7))
    b8=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b8,8))
    b9=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b9,9))
    b10=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b10,10))
    b11=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b11,11))
    b12=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b12,12))
    b13=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b13,13))
    b14=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b14,14))
    b15=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b15,15))
    b16=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b16,16))
    b17=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b17,17))
    b18=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b18,18))
    b19=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b19,19))
    b20=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b20,20))
    b21=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b21,21))
    b22=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b22,22))
    b23=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b23,23))
    b24=Button(play_frame,text='',bg='#FEC3DE',font=("Algerian",20),height=3,width=6,command=lambda:click(b24,24))
    b25=Button(play_frame,text='',bg='#E3C9F7',font=("Algerian",20),height=3,width=6,command=lambda:click(b25,25))
    b26=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b26,26))
    b27=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b27,27))
    b28=Button(play_frame,text='',bg='#F1E9DA',font=("Algerian",20),height=3,width=6,command=lambda:click(b28,28))
    b29=Button(play_frame,text='',bg='light blue',font=("Algerian",20),height=3,width=6,command=lambda:click(b29,29))

    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=0,column=4)
    
    b5.grid(row=1,column=0)
    b6.grid(row=1,column=1)
    b7.grid(row=1,column=2)
    b8.grid(row=1,column=3)
    b9.grid(row=1,column=4)

    b10.grid(row=2,column=0)
    b11.grid(row=2,column=1)
    b12.grid(row=2,column=2)
    b13.grid(row=2,column=3)
    b14.grid(row=2,column=4)

    b15.grid(row=3,column=0)
    b16.grid(row=3,column=1)
    b17.grid(row=3,column=2)
    b18.grid(row=3,column=3)
    b19.grid(row=3,column=4)

    b20.grid(row=4,column=0)
    b21.grid(row=4,column=1)
    b22.grid(row=4,column=2)
    b23.grid(row=4,column=3)
    b24.grid(row=4,column=4)

    b25.grid(row=5,column=0)
    b26.grid(row=5,column=1)
    b27.grid(row=5,column=2)
    b28.grid(row=5,column=3)
    b29.grid(row=5,column=4)

    fin_label=Label(rt,text='')
    fin_label.pack(pady=20)


    
def wind1():
    top1=Toplevel()
    
    bt1=Button(top1,text='Easy',font=("Century",18),command=easy).pack()
    bt2=Button(top1,text='Medium',font=("Century",18),command=medium).pack()
    bt3=Button(top1,text='Tough',font=("Century",18),command=tough).pack()

def wind2():
    top1=Toplevel()

    bt1=Button(top1,text='Elements',font=("Century",18),command=top1.destroy).grid(row=0,column=0)
    bt2=Button(top1,text='Wars',font=("Century",18),command=top1.destroy).grid(row=1,column=0)
    bt3=Button(top1,text='Authors',font=("Century",18),command=top1.destroy).grid(row=2,column=0)  

def come_on():
    
    #q="Select * from memory where player_name=('{}')".format(e.get(),)
    #cur.execute(q)
    #record=cur.fetchone()
    #if record!=None:
    #    l=Label(root,text="Player name: "+record[0]+"   Scores:"+str(record[1]),bg='#FFF5C2',font=("Georgia",12)).pack()
    #if record==None:
    #    q1="Insert into memory values('{}',0)".format(e.get(),)
    #    cur.execute(q1)
    #    db.commit()
    
    top=Toplevel()
    top.title("Mode")
    b2=Button(top,text='Casual',font=("Century",18),command=wind1).pack()
    b3=Button(top,text='Learner',font=("Century",18),command=wind2).pack()
    

b=Button(root,text='Play',bg='#FFF5C2',font=("Georgia",12),command=come_on)
b.pack(pady=20)

root.mainloop

