#pip3 install Pillow
#===========================================================================

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import tkinter.font as font

from PIL import Image, ImageTk

import sys
import os
import functools

#===========================================================================

currentDirectory = os.getcwd()

ImageDirectory = os.path.join(currentDirectory, "_Image")

#--------------------------------------------------------------------------- 

Window = Tk()
Window.title("Number converter")

SW = Window.winfo_screenwidth() 
SH = Window.winfo_screenheight()

WinWidht = 795 
WinHeight = 230 
     
XPos = int(SW/2 - WinWidht/2)   
YPos = int(SH/2 - WinHeight/2)  

Window.geometry('%dx%d+%d+%d' % (WinWidht, WinHeight, XPos, YPos))
Window.resizable(False, False)

IconPath = os.path.join(ImageDirectory, "_Hashtag.png")
NCIco = PhotoImage(file = IconPath)
Window.tk.call('wm', 'iconphoto', Window._w, NCIco)

#---------------------------------------------------------------------------
Font1=font.Font(family="Verdana",size=16)
Font2=font.Font(family="Verdana",size=12)

#---------------------------------------------------------------------------
def clearEnt(*args):

    global Conversion
    btnConversion.configure(text="Convert", command=Conversion)
    btnConversion.update()

    for x in [Entries[0], Entries[1], Entries[2], Entries[3]]:
    
        x.config(validate="none")
        x.delete(0, END)
        x.config(validate="key")
        x.config(fg="black")
        
    return True

#---------------------------------------------------------------------------   
def BinaryConversion():

    try:

        #Binary to Octal
        OctalNum = oct(int(Number, 2))[2:]
       
        #Binary to Decimal
        DecimalNum = int(Number, 2)

        #Binary to Hexadecimal
        HexadecimalNum = hex(int(Number, 2)).upper()[2:]
        
        for _bin in [(Entries[1], OctalNum), (Entries[2], DecimalNum), (Entries[3], HexadecimalNum)]:

            _bin[0].config(validate="none")
            _bin[0].delete(0, END)
            _bin[0].insert(0, _bin[1])

            if len(_bin[0].get()) > 41:
                 _bin[0].config(fg="red")
            else:
                _bin[0].config(fg="blue")

    except ValueError:
        Name.focus()
        Name.selection_range(0, END)
        ErrMsg = messagebox.showerror('Error', 'Input Error! \nInvalid number format.')
   
def OctalConversion():

    try:

        #Octal to Binary    
        BinaryNum = bin(int(str(Number), 8))[2:]

        #Octal to Decimal
        DecimalNum = int(str(Number), 8)

        #Octal to Hexadecimal
        HexadecimalNum = hex(int(str(Number), 8)).upper()[2:]

        for _oct in [(Entries[0], BinaryNum), (Entries[2], DecimalNum), (Entries[3], HexadecimalNum)]:

            _oct[0].config(validate="none")
            _oct[0].delete(0, END)
            _oct[0].insert(0, _oct[1])

            if len(_oct[0].get()) > 41:
                _oct[0].config(fg="red")
            else:
                _oct[0].config(fg="blue")            

    except ValueError:
        Name.focus()
        Name.selection_range(0, END)
        ErrMsg = messagebox.showerror('Error', 'Input Error! \nInvalid number format.')
       
def DecimalConversion():

    try:
        
        #Decimal to Binary 
        BinaryNum = bin(int(Number))[2:]

        #Decimal to Octal
        OctalNum = oct(int(Number))[2:]

        #Decimal to Hexadecimal
        HexadecimalNum = hex(int(Number)).upper()[2:]

        for _dec in [(Entries[0], BinaryNum), (Entries[1], OctalNum), (Entries[3], HexadecimalNum)]:

            _dec[0].config(validate="none")
            _dec[0].delete(0, END)
            _dec[0].insert(0, _dec[1])
            
            if len(_dec[0].get()) > 41:
                _dec[0].config(fg="red")
            else:
                _dec[0].config(fg="blue")

    except ValueError:
        Name.focus()
        Name.selection_range(0, END)
        ErrMsg = messagebox.showerror('Error', 'Input Error! \nInvalid number format.')
        
def HexadecimalConversion():

    try:
        
        #Hexadecimal to Binary 
        BinaryNum = bin(int(str(Number), 16))[2:]

        #Hexadecimal to Octal
        OctalNum = oct(int(str(Number), 16))[2:]

        #Hexadecimal to Decimal
        DecimalNum = int(str(Number), 16)

        for _hex in [(Entries[0], BinaryNum), (Entries[1], OctalNum), (Entries[2], DecimalNum)]:

            _hex[0].config(validate="none")
            _hex[0].delete(0, END)
            _hex[0].insert(0, _hex[1])

            if len(_hex[0].get()) > 41:
                _hex[0].config(fg="red")
            else:
                _hex[0].config(fg="blue")
            
    except ValueError:
        Name.focus()
        Name.selection_range(0, END)
        ErrMsg = messagebox.showerror('Error', 'Input Error! \nInvalid number format.')
        
#---------------------------------------------------------------------------        
def Conversion(*args):

    global clearEnt
    btnConversion.configure(text="Clear", command=clearEnt)
    btnConversion.update()
    
    global Number
    
    if len(Entries[0].get()) != 0:
        Number = Entries[0].get()
        BinaryConversion()

    elif len(Entries[1].get()) != 0:
        Number = Entries[1].get()
        OctalConversion()

    elif len(Entries[2].get()) != 0:
        Number = Entries[2].get()
        DecimalConversion()

    elif len(Entries[3].get()) != 0:
        Number = Entries[3].get()
        HexadecimalConversion()

    else:
        ErrMsg = messagebox.showerror('Error', 'Input Error! \nInvalid number format.')

        global Conversion
        btnConversion.configure(text="Convert", command=Conversion)
        btnConversion.update()
        
#---------------------------------------------------------------------------
def HexTrace(*args):   
    hexStr.set(hexStr.get().upper())

hexStr = StringVar(Window)  

hexStr.trace('w', HexTrace)

#---------------------------------------------------------------------------
def testBinary(char, P):
    if char in '01':
        return True                                                      
    return False 

def testOctal(S):
    if S in ['0', '1', '2', '3', '4', '5', '6', '7']:
        return True
    return False

def testDecimal(S):
    if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False

def testHexadecimal(char, P):
    if char in '0123456789ABCDEFabcdef':
        return True                                                       
    return False

#---------------------------------------------------------------------------
def SelectAll(event=None):
   
    Name.focus()
    Name.selection_range(0, END)
    Name.icursor(END)
    return 'break'
   
#---------------------------------------------------------------------------
def doBackspace(event):

    Name.config(validate="none")

    global CursorPos

    if Name.select_present():
     
        selection = Name.selection_get()
        
        Window.clipboard_clear()
        Window.clipboard_append(selection)

        CursorPos = Name.index("sel.first")
        
        Name.delete(Name.index("sel.first"), Name.index("sel.last"))
        Name.update()
       
        return "break"
    
    else:

        try:
            selection = Name.get()
            last_char = selection[-1]

            CursorPos = Name.index(INSERT)
            
            Window.clipboard_clear()
            Window.clipboard_append(last_char)

        except IndexError:
            pass
            
    Name.config(validate="key")

#---------------------------------------------------------------------------
def CopyToClipboard(event):

    if not Name.select_present():
        Name.focus()
        Name.selection_range(0, END)
        Name.icursor(END)
    
        _Clipboard=Name.get().rstrip()

    else:
       _Clipboard = Name.selection_get().rstrip()

    Window.clipboard_clear()
    Window.clipboard_append(_Clipboard)
         
#---------------------------------------------------------------------------
def PasteFromClipboard(event):

    Name.config(validate="none")

    if Name.select_present():
  
        Name.focus()
  
        Name.delete(Name.index("sel.first"), Name.index("sel.last"))
        Name.update()

    position = Name.index(INSERT)
   
    _Clipboard = (Window.clipboard_get())   
    Name.insert(position, _Clipboard)
    Name.icursor(END)

    Name.config(validate="key")
    
#---------------------------------------------------------------------------
def GetName(event):

    global Name
    
    if str(event.widget.myId) == "bin_Ent1" or str(event.widget.myId) == "bin_Ent2" or str(event.widget.myId) == "bin_Ent3":
        Name = Entries[0]
                
    elif str(event.widget.myId) == "oct_Ent1" or str(event.widget.myId) == "oct_Ent2" or str(event.widget.myId) == "oct_Ent3":
        Name = Entries[1]       

    elif str(event.widget.myId) == "dec_Ent1" or str(event.widget.myId) == "dec_Ent2" or str(event.widget.myId) == "dec_Ent3":
        Name = Entries[2]

    elif str(event.widget.myId) == "hex_Ent1" or str(event.widget.myId) == "hex_Ent2" or str(event.widget.myId) == "hex_Ent3":
        Name = Entries[3]

#===========================================================================   
yPos0 = 10

LblName = ["Binary:", "Octal:", "Decimal:", "Hexadecimal:"]

for Lbl in LblName:

    _LblName = Label(Window,text=Lbl, font=Font1)
    _LblName.place(x=10, y=yPos0)
    
    yPos0 += 40

#---------------------------------------------------------------------------   
EntryID = ["bin_Ent1", "oct_Ent1", "dec_Ent1", "hex_Ent1"]

ValCmd = [(Window.register(testBinary),'%S','%P'), (Window.register(testOctal),'%S'),
          (Window.register(testDecimal),'%S'), (Window.register(testHexadecimal),'%S','%P')]

TxtVar = ["", "", "", hexStr]

yPos1 = 10

entWidth = 41

Entries = []

for q in range (0, 4):

    _Entry = Entry(Window, text="", textvariable=TxtVar[q], font = Font1, justify='center',
                   validate='key', validatecommand=ValCmd[q], width=entWidth)
    _Entry.place(x=175, y=yPos1)
    
    _Entry.bind("<Button-1>", GetName)
    _Entry.bind("<Control-a>", SelectAll)
    _Entry.bind('<Control-c>', CopyToClipboard)   
    _Entry.bind('<Control-v>', PasteFromClipboard) 
    _Entry.bind("<BackSpace>", doBackspace)
    _Entry.bind( '<Delete>', doBackspace )
    
    _Entry.myId = EntryID[q]

    Entries.append(_Entry)
    
    yPos1 += 40  

#===========================================================================  
def ConverterExit():
    Window.destroy()
    
#---------------------------------------------------------------------------    
btnConversion = Button(Window, text="Convert",font = Font2, command = Conversion)
btnConversion.place(x=int(WinWidht/2 - 60), y=180, width=90, height=35)

btnExit = Button(Window, text="Exit",font = Font2, command = ConverterExit)
btnExit.place(x=WinWidht-100, y=180, width=90, height=35)

#---------------------------------------------------------------------------
btnF=Frame(Window)
btnF.config(width=70, height=165)
btnF.place(x=int(WinWidht - 75), y=0)
btnF.pack_propagate(False)

#---------------------------------------------------------------------------
CopyImgPath = os.path.join(ImageDirectory, "_Copy.png")
CopyImg = ImageTk.PhotoImage(Image.open(CopyImgPath))

yPos2 = 10

CopyBtnID = ["bin_Ent2", "oct_Ent2", "dec_Ent2", "hex_Ent2"]

for n in range (0, 4):

    CopyBtn = Button(btnF, image = CopyImg, command=functools.partial(CopyToClipboard, n))
    CopyBtn.place(x=0, y=yPos2, width=30, height=30)
    CopyBtn.bind("<Button-1>", GetName)
    
    CopyBtn.myId = CopyBtnID[n]

    yPos2 += 40
   
#---------------------------------------------------------------------------
PasteImgPath = os.path.join(ImageDirectory, "_Paste.png")
PasteImg = ImageTk.PhotoImage(Image.open(PasteImgPath))

yPos3 = 10

PasteBtnID = ["bin_Ent3", "oct_Ent3", "dec_Ent3", "hex_Ent3"]

for m in range (0, 4):

    PasteBtn = Button(btnF, image = PasteImg, command=functools.partial(PasteFromClipboard, m))
    PasteBtn.place(x=35, y=yPos3, width=30, height=30)
    PasteBtn.bind("<Button-1>", GetName)

    PasteBtn.myId = PasteBtnID[m]
    
    yPos3 += 40
    
#---------------------------------------------------------------------------
Window.bind('<Return>', Conversion)
Window.bind("<Escape>", clearEnt)

#---------------------------------------------------------------------------
Window.mainloop()
