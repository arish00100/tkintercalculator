from tkinter import *
from tkinter import font

#Initial window configuration
win=Tk()
win.title("Calculator")
win.geometry('295x320')
win.configure(bg='gray20')

#Changing default font and size
def_font=font.nametofont("TkDefaultFont")
def_font.configure(size=15,weight='bold')

ent_font=font.nametofont("TkTextFont")
ent_font.configure(size=22,weight='bold')


result=StringVar()
result='0'
num1=0
num2=0
opcd=-1

ent=Entry(master=win,textvariable=result,bg='gray20',fg='white',relief='sunken',justify='right')
ent.insert(0,result)
ent.pack(fill=X,padx=5,pady=5)


frabtns=Frame(bg='gray20')
frabtns.pack(fill=BOTH,expand=True,)

def clrent():
    ent.delete(0,END)
    ent.insert(0,'0')
    

def bksp():
    entinp=ent.get()
    ent.delete(0,END)
    if(len(entinp)!=1):
        ent.insert(0,entinp[:-1])
    else:
        ent.insert(0,'0')

def inpnum1():
    global num1
    num1=float(ent.get())
    ent.delete(0,END)
    ent.insert(0,'0')

def plus():
    inpnum1()
    global opcd
    opcd=0

def minus():
    inpnum1()
    global opcd
    opcd=1

def mult():
    inpnum1()
    global opcd
    opcd=2

def divide():
    inpnum1()
    global opcd
    opcd=3

def root():
    inpnum1()
    global opcd
    opcd=4

def power():
    inpnum1()
    global opcd
    opcd=5





def equal():
    #global num2
    num2=float(ent.get())
    ent.delete(0,END)
    if opcd==0:
        res=num1+num2
    elif opcd==1:
        res=num1-num2
    elif opcd==2:
        res=num1*num2
    elif opcd==3:
        res=num1/num2
    elif opcd==4:
        res=num2**(1/2)
    elif opcd==5:
        res=num1**num2
    ent.insert(0,str(res))


    
    

def inp0():
    ent.insert(END,'0')
def inp1():
    clr0()
    ent.insert(END,'1')
def inp2():
    clr0()
    ent.insert(END,'2')
def inp3():
    clr0()
    ent.insert(END,'3')
def inp4():
    clr0()
    ent.insert(END,'4')
def inp5():
    clr0()
    ent.insert(END,'5')
def inp6():
    clr0()
    ent.insert(END,'6')
def inp7():
    clr0()
    ent.insert(END,'7')
def inp8():
    clr0()
    ent.insert(END,'8')
def inp9():
    clr0()
    ent.insert(END,'9')
'''def inpdot():
    clr0()
    if float(ent.get())==0:
        ent.insert(END,'0.')
    else:
        ent.insert(END,'.')'''
####################
        #Functionality of dot
        #Responsive
        #Precision
#####################
    
def clr0():
    strnum=ent.get()
    #if '.' in strnum:
        #strnum=strnum+'0'
    if float(strnum)==0:
        ent.delete(0,END)




btn_1=Button(master=frabtns,bg='black',fg='white',text='1',justify='center',width=5,command=inp1)
btn_2=Button(master=frabtns,text='2',bg='black',fg='white',justify='center',width=5,command=inp2)
btn_3=Button(master=frabtns,text='3',bg='black',fg='white',justify='center',width=5,command=inp3)
btn_4=Button(master=frabtns,text='4',bg='black',fg='white',justify='center',width=5,command=inp4)
btn_5=Button(master=frabtns,text='5',bg='black',fg='white',justify='center',width=5,command=inp5)
btn_6=Button(master=frabtns,text='6',bg='black',fg='white',justify='center',width=5,command=inp6)
btn_7=Button(master=frabtns,text='7',bg='black',fg='white',justify='center',width=5,command=inp7)
btn_8=Button(master=frabtns,text='8',bg='black',fg='white',justify='center',width=5,command=inp8)
btn_9=Button(master=frabtns,text='9',bg='black',fg='white',justify='center',width=5,command=inp9)
btn_0=Button(master=frabtns,text='0',bg='black',fg='white',justify='center',width=5,command=inp0)

btn_pls=Button(master=frabtns,text='+',bg='black',fg='white',justify='center',width=5,command=plus)
btn_min=Button(master=frabtns,text='-',bg='black',fg='white',justify='center',width=5,command=minus)
btn_mul=Button(master=frabtns,text='*',bg='black',fg='white',justify='center',width=5,command=mult)
btn_div=Button(master=frabtns,text='/',bg='black',fg='white',justify='center',width=5,command=divide)
btn_equ=Button(master=frabtns,text='=',bg='black',fg='white',justify='center',width=5,command=equal)
btn_rot=Button(master=frabtns,text='√',bg='black',fg='white',justify='center',width=5,command=root)
btn_exp=Button(master=frabtns,text='x^y',bg='black',fg='white',justify='center',width=5,command=power)

btn_dot=Button(master=frabtns,text='.',bg='black',fg='white',justify='center',width=5)
btn_clr=Button(master=frabtns,text='C',bg='black',fg='white',justify='center',width=5,command=clrent)
btn_bsp=Button(master=frabtns,text='c',bg='black',fg='white',justify='center',width=5,command=bksp)

btn_list=[btn_clr,btn_rot,btn_exp,btn_div,
          btn_7,btn_8,btn_9,btn_mul,
          btn_4,btn_5,btn_6,btn_min,
          btn_1,btn_2,btn_3,btn_pls,
          btn_dot,btn_0,btn_bsp,btn_equ
          ]

r,c=0,0
for btn in btn_list:
    btn.grid(row=r,column=c,padx=2,pady=2)
    
    c+=1
    if c==4:
       r+=1
       c=0
    





tk=mainloop()

















