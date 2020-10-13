from tkinter import *
import tkinter.font as tkfont
from tkinter import *
from random import randint
import time

def No1(event):
    print('no')

def Start(event):
    StartBt.destroy()
    ExpLb2.destroy()
    ExpLbY.destroy()
    ExpLbN.destroy()
    ExpLb1.destroy()
    WelcomeLb1.destroy()
    #ClickBt1.place(x=0,y=0)
    #ClickBt1.config(bg = 'red')
    WarnLb1.place(x=206,y=45)
    BegBt1.place(x=225,y=20)
    print('.') 
    message=print('good, red click room')
    
    root.config(bg='red')
    VersLb.config(bg='red')


#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---Start function END
#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---Begin function BEGIN

def Begin(event):
    ClickBt1.bind('<Button-1>', No1)
    print('timer gen check')
    time = randint(1000, 10000)
    print('check, timer to greenscreen start')
    root.after(time)
# /\generates rand integer, root.after will wait that amount of time before pushing next command

    print('good, greenscreen up')#checkpoint
    BegBt1.destroy()
    WarnLb1.destroy()
    
# /\destroys all uneeded widgets leaving only click

    Strt_Time = start_time()
    print(Strt_Time)
    
# /\begins timer
    ClickBt1.place(x=207,y=75)
    ClickBt1.bind('<Button-1>', Cliick)
    ClickBt1.config(text='CLICK!')
    
# /\only now binds CLICK button to prevent misclick prior to greenscreening
    root.config(bg='green')
    VersLb.config(bg='green')
    
# /\changes all to green, indicating to the user that they have to click now.

#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---BEGIN function END
#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---start_time function BEGIN

def start_time():
   global initial
   print("Timer", "The timer will now begin")
   initial = time.time()
   return initial

#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---start_time function END
#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---stop_time function BEGIN

def stop_time(event):
    global finalVal, final, timerDisplay2
    final = time.time()
    print("Timer", final - initial)
    finalTim = final - initial
    finalVal = round(finalTim, 3)
    timerDisplay2 = Label(root, text = finalVal, bg = 'grey')
    timerDisplay2.config(font=('Calibri', 15))
    return finalVal, initial
  
#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---stop_time function END
#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---Cliick function BEGIN

def Cliick(event):
    global timerDisplay1, timerDisplay2
    stptime = stop_time(event)
# /\ends timer
    print(stptime)
# /\prints the time taken.
    root.config(bg='grey')
    VersLb.config(bg='grey')
    ClickBt1.place_forget()
    timerDisplay1.place(x=150, y=30)
    timerDisplay2.place(x=150,y=62)
# /\ returns to normal state
    
#===---===---===---===---===---===---===---===---===---===---===---===---====---===---===---===---Cliick function END
    
# /\ FUNCTION DEFS=====================================================================================















#----------------------------------------------------------------------------------STRUCTURE-START: A PRIORI TO CLICK SCREEN

root=Tk()

root.title("Reaction Test")

root.geometry ('500x200')
print("Think of either a car, a fish, a dog or a horse.")

WelcomeLb1 = Label(root, text="Welcome to Reaction Test!")
ExpLb1 = Label(root, text = 'Click the button when green!!!')
ExpLb2 = Label(root,text='After start, the game will go to screen, press begin to start....')
ExpLbY = Label(root, text='Green = CLICK!')
ExpLbN = Label(root, text='Red = NO CLICK!')
#ClickBt1 = Button(root, text='', height = 5, width = 10)
StartBt=Button(root, text='Start')
VersLb = Label(root, text='v0.1')


ExpLb1.config (font=('Calibri', 13))
WelcomeLb1.config(font=('Calibri', 25))
ExpLbY.config(fg='green')
ExpLbN.config(fg='red')


StartBt.place(x=230,y=100)
ExpLb2.place(x=100,y=165)
ExpLbY.place(x=15,y=135)
ExpLbN.place(x=390,y=135)
ExpLb1.place(x=75, y=38)
WelcomeLb1.place(x=72, y=2)
VersLb.place(x=3,y=3)


StartBt.bind('<Button-1>', Start)


#---------------------------------------------------------------------------------STRUCTURE-END
#---------------------------------------------------------------------------------STRUCTURE-START: BEFORE AND AFTER CLICK SCREEN

ClickBt1 = Button(root, text='', height = 5, width = 10)
WarnLb1 = Label(root, text='Get ready....', bg='red')
BegBt1 = Button(root, text='Begin')
WarnLb1N= Label(root, text='NOW!')
timerDisplay1 = Label(root, text = "You took, ", bg='grey')

WarnLb1.config(font=('Calibri', 12,))
timerDisplay1.config(font=('Calibri', 15))

BegBt1.bind('<Button-1>', Begin)

# /\ Labels A Priori to click












                 

