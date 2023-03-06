from tkinter import * 
import tkinter as tk
from tkinter import filedialog as fd 
from PIL import Image, ImageTk
#from depreciation_stuff import depreciation

root = tk.Tk()
root.geometry("1000x1000")

filename = fd.askopenfilename()
print(filename)

img = Image.open(filename)
resized_image= img.resize((450,350))
new_image= ImageTk.PhotoImage(resized_image)
label = Label(root, image = new_image)
label.pack()

my_title = tk.Label(root, text = 'Depreciation Estimation of Phone', font = ('Arial',20,'bold') )
my_title.pack()
my_header  = tk.Label(root, text = 'Input necessary features for price estimation')
my_header.pack()   
space = tk.Label(text = ' ')
space.pack()

# #User inputs
L1 = tk.Label(text = 'Choose the model of your phone', font =  ('Arial',12,'bold'))
L1.pack()

clicked = StringVar(root)
clicked.set('Options')
model_options = ['Iphone 7', 'Iphone 8', 'Iphone 9','Iphone 10', 'Iphone 11', 'Iphone 12',\
                    'Iphone 13', 'Iphone 14']
drop = OptionMenu(root,clicked,*model_options)
drop.pack()

def printValue():
    val = clicked.get()

E_button = Button(root, text = 'Submit', command = printValue).pack()

space = tk.Label(text = ' ')
space.pack()

L2 = Label(text = 'Enter the age of your phone: ', font = ('Arial',12,'bold') )
L2.pack()
E2 = Entry(root, font =('Arial', 12))
E2.pack()

def printValue_2():
    pname = int(E2.get())

E2_button = Button(root, text = 'Submit ', command = printValue_2).pack()

def depreciation():
    #if percentage_crack < 1:
    
    #CDPR = 0.35 * percentage_crack

    model = clicked.get()
    AGE = int(E2.get())
    CDPR = 2

    if model == 'iphone 7' or model == 'Iphone 7' :
        RCV=1000
  
    if model == 'iphone 8' or model == 'Iphone 8' :
        RCV=1000
  
    if model == 'iphone 10' or model == 'Iphone 10':
        RCV=1000
  
    if model == 'iphone 11' or model == 'Iphone 11':
        RCV=1000
  
    if model == 'iphone 12' or model == 'Iphone 12':
        RCV=1000
  
    if model == 'iphone 13' or model == 'Iphone 13':
        RCV=1000
  
    if model == 'iphone 14' or model == 'Iphone 14':
        RCV=1000
    
    DPR = 0.25 + 0.2 * AGE
    ACV = RCV - DPR * RCV * AGE * CDPR
  
    Label(root, text=f'The current value of your phone is: {ACV} $', pady=20).pack()

space = tk.Label(text = ' ')
space.pack()

button_1 = Button(root, text = 'Calculate Depreciation', command = depreciation).pack()

root.mainloop()