'''
This is a python program of a graphical Calculator made using Tkinter.
It operates with the help of MyMath.py module to calculate areas, volumes, csa, tsa of different shapes.
'''

import MyMath
from os import path
from tkinter import Tk,Text,BOTH,END,Menu,StringVar,Label,W,E,N,S,Entry,Button,ttk

def notes():	
	root = Tk() 
	root.geometry("350x250") 
	root.title("Notes") 
	root.minsize(height=250, width=350) 
	root.maxsize(height=250, width=350) 
	text_info = Text(root) 
	text_info.pack(fill=BOTH)
	
	if not path.exists("NOTES.txt"):
		open("NOTES.txt",'w+').close()
	ReadF = open("NOTES.txt",'r')
	text_info.delete('1.0', 'end')
	text_info.insert('1.0',ReadF.read())
	ReadF.close()
	
	def save():	
		WriteF = open('NOTES.txt','w')
		WriteF.write(text_info.get('1.0',END))
		WriteF.close()

	m = Menu(root)
	m.add_command(label="SAVE", command=save)
	root.config(menu=m)

	root.mainloop() 

def calculate():
	funcName = shape.get() + '_' + oper.get() + '_' + unknown.get() 
	l = length.get() 
	b = breadth.get() 
	h = height.get()  
	r = radius.get()  
	k = known.get()   
	try:
		Result.set( str(getattr(MyMath,funcName)(l,b,h,r,k)) )
	except AttributeError:
		Result.set('Invalid Operation')
		
master = Tk()
master.title('CALCULATOR')
Result=StringVar()
Error=StringVar()
ErrorReason=StringVar()

options = {'SELECT SHAPE':{'----------':['----------'] },
		'TRIANGLE'	:{'----------':['----------'],
					  'AREA'  : ['BREADTH','HEIGHT','AREA'] },
		'RECTANGLE'	:{'----------':['----------'],
					  'AREA'  : ['LENGTH','BREADTH','AREA'] }, 
		'CIRCLE'	:{'----------':['----------'],
					  'AREA'  : ['RADIUS','AREA'] }, 
		'CUBE'		:{'----------':['----------'],
					  'VOLUME': ['LENGTH','VOLUME'],
					  'LSA'	  : ['LENGTH','LSA'],
					  'TSA'   : ['LENGTH','TSA']  
					 }, 
		'CUBOID'	:{'----------':['----------'],
					  'VOLUME': ['LENGTH','BREADTH','HEIGHT','VOLUME'],
					  'LSA'	  : ['LENGTH','BREADTH','HEIGHT','LSA'],
					  'TSA'   : ['LENGTH','BREADTH','HEIGHT','TSA']
					 },  
		'SPHERE'	:{'----------':['----------'],
					  'VOLUME': ['RADIUS','VOLUME',],
					  'TSA'   : ['RADIUS','TSA']
					 }, 
		'HEMISPHERE':{'----------':['----------'],
					  'VOLUME': ['RADIUS','VOLUME'],
					  'CSA'	  : ['RADIUS','CSA'],
					  'TSA'   : ['RADIUS','TSA']
					 },  
		'CYLINDER'	:{'----------':['----------'],
					  'VOLUME': ['RADIUS','HEIGHT','VOLUME'],
					  'CSA'	  : ['RADIUS','HEIGHT','CSA'],
					  'TSA'   : ['RADIUS','HEIGHT','TSA']
					 },  
		'CONE'		:{'----------':['----------'],
					  'VOLUME': ['RADIUS','HEIGHT','VOLUME'],
					  'CSA'	  : ['RADIUS','LENGTH','CSA'],
					  'TSA'   : ['RADIUS','LENGTH','TSA']
					 }, 
		}

Label(master, text ="SHAPE").grid(row = 0,sticky=W) 
shapes = list(options.keys())
shape=ttk.Combobox(master, width = 17, state='readonly',value=(shapes)) 
shape.current(0) 

Label(master, text ="OPERATION").grid(row = 1,sticky=W) 
oper=ttk.Combobox(master, width = 17, state='readonly', values = list( options[ shape.get() ].keys() ) ) 
def callback1(eventObject):
	oper.config(values= list( options[ shape.get() ].keys() ) )
oper.bind('<Button-1>', callback1)
oper.current(0) 

Label(master, text ="UNKNOWN").grid(row = 2,sticky=W) 
unknown=ttk.Combobox(master, width = 17, state='readonly', values = options[shape.get()][oper.get()] ) 
def callback2(eventObject):
    unknown.config(values= options[shape.get()][oper.get()] )
unknown.bind('<Button-1>', callback2)
unknown.current(0)

Label(master, text="LENGTH    ").grid(row=3, sticky=W)
Label(master, text="BREADTH   ").grid(row=4, sticky=W)
Label(master, text="HEIGHT    ").grid(row=5, sticky=W)
Label(master, text="RADIUS    ").grid(row=6, sticky=W)
Label(master, text="AREA/VOL  ").grid(row=7, sticky=W)
Label(master, text="          ").grid(row=8, sticky=W)
Label(master, text="RESULT:   ").grid(row=9, sticky=W)
Label(master, text="          ").grid(row=10, sticky=W)
Label(master, text="NOTE:     ").grid(row=11, sticky=W)

Label(master, text="", textvariable=Result).grid(row=9,column=1, sticky=W)
Label(master, text="", textvariable=Error).grid(row=26,column=0, sticky=E)
Label(master, text="", textvariable=ErrorReason).grid(row=26,column=1, sticky=W)
expression = "" 

def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression)

def equalpress(): 
		global expression
		try:
			total = str(eval(expression))
			equation.set(total)
			Error.set("")
			ErrorReason.set("")
		except ZeroDivisionError:
			Error.set("ERROR:")
			ErrorReason.set("Can't divide by 0")
		except:
			Error.set("ERROR:")
			ErrorReason.set("Invalid Expression")
		expression = ""

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

equation = StringVar() 
expression_field = Entry(master, textvariable=equation) 
expression_field.grid(row=20,columnspan=4, ipadx=70)

button1 = Button(master, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=1, width=7) 
button1.grid(row=22, column=0) 

button2 = Button(master, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=1, width=7) 
button2.grid(row=22, column=1) 

button3 = Button(master, text=' 3 ', fg='black', bg='white',command=lambda: press(3), height=1, width=7) 
button3.grid(row=22, column=2) 

button4 = Button(master, text=' 4 ', fg='black', bg='white',command=lambda: press(4), height=1, width=7) 
button4.grid(row=23, column=0) 

button5 = Button(master, text=' 5 ', fg='black', bg='white',command=lambda: press(5), height=1, width=7) 
button5.grid(row=23, column=1) 

button6 = Button(master, text=' 6 ', fg='black', bg='white',command=lambda: press(6), height=1, width=7) 
button6.grid(row=23, column=2) 

button7 = Button(master, text=' 7 ', fg='black', bg='white',command=lambda: press(7), height=1, width=7) 
button7.grid(row=24, column=0) 

button8 = Button(master, text=' 8 ', fg='black', bg='white',command=lambda: press(8), height=1, width=7) 
button8.grid(row=24, column=1) 

button9 = Button(master, text=' 9 ', fg='black', bg='white',command=lambda: press(9), height=1, width=7) 
button9.grid(row=24, column=2) 

button0 = Button(master, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=1, width=7) 
button0.grid(row=25, column=0) 

plus = Button(master, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7) 
plus.grid(row=22, column=4) 

minus = Button(master, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7) 
minus.grid(row=23, column=4) 

multiply = Button(master, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=24, column=4) 

divide = Button(master, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=7) 
divide.grid(row=25, column=4) 

equal = Button(master, text=' = ', fg='black', bg='white',command=equalpress, height=1, width=7) 
equal.grid(row=26, column=4) 

clear = Button(master, text='Clear', fg='black', bg='white',command=clear, height=1, width=7) 
clear.grid(row=25, column=2) 

Decimal= Button(master, text='.', fg='black', bg='white',command=lambda: press('.'), height=1, width=7) 
Decimal.grid(row=25, column=1)

shape.grid   (row=0, column=1)
oper.grid	 (row=1, column=1)
unknown.grid (row=2, column=1)

length  = Entry(master); length.grid  (row=3, column=1)
breadth = Entry(master); breadth.grid (row=4, column=1)
height  = Entry(master); height.grid  (row=5, column=1)
radius  = Entry(master); radius.grid  (row=6, column=1)
known   = Entry(master); known.grid   (row=7, column=1)

def buttons():
	Cal = Button(master, text="Calculate", command=calculate)
	Cal.grid(row=0, column=3,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

	Notes = Button(master, text="Notes", command=notes)
	Notes.grid(row=11, column=1,columnspan=1, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
	
buttons()	
master.mainloop()
