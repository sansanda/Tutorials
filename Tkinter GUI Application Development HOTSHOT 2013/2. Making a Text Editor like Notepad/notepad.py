from tkinter import *
from menuCommands.menuCommands import *



root = Tk()
root.geometry('350x350')

#defining icons for compund menu demonstration
newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')



#************************************************************************
#Menu Variables
#************************************************************************

#we define a color scheme dictionary containg name and color code as key value pair
clrschms = {
'1. Default White': 'FFFFFF',
'2. Greygarious Grey':'D1D4D1',
'3. Lovely Lavender':'E1E1FF' ,
'4. Aquamarine': 'D1E7E0',
'5. Bold Beige': 'FFF0E1',
'6. Cobalt Blue':'333AA',
'7. Olive Green': '5B8340',
}

selectedTheme = StringVar(value='1. Default White')
showLineNumber = BooleanVar(value=True)
showInfoBarAtBottom = BooleanVar(value=True)
highLightCurrentLine = BooleanVar(value=True)


#************************************************************************
#CREATE MENU BAR SECTION
#************************************************************************

#create the menu bar
menubar = Menu(root)
root.config(menu=menubar)

#create the filemenu
fileMenu = Menu(menubar,tearoff=0)

#add menu items
fileMenu.add_command(label="New...", accelerator='Ctrl + N', compound=LEFT, image=newicon, command=newFilecallback)
fileMenu.add_separator()
fileMenu.add_command(label="Open...", accelerator='Ctrl + O', compound=LEFT, image=openicon, command=openFilecallback)
fileMenu.add_command(label="Save", accelerator='Ctrl + S', compound=LEFT, image=saveicon, command=saveFilecallback)


#add the menu to the menu bar
menubar.add_cascade(label='File',menu=fileMenu)

#create the editmenu
editMenu = Menu(menubar,tearoff=0)

#add menu items
editMenu.add_command(label="Undo", accelerator='Ctrl + Z', compound=LEFT, image=undoicon, command=undocallback)
editMenu.add_command(label="Redo", accelerator='Ctrl + Y', compound=LEFT, image=redoicon, command=redocallback)
editMenu.add_separator()
editMenu.add_command(label="Cut", accelerator='Ctrl + X', compound=LEFT, image=cuticon, command=cutcallback)
editMenu.add_command(label="Copy", accelerator='Ctrl + C', compound=LEFT, image=copyicon, command=copycallback)
editMenu.add_command(label="Find All", accelerator='Ctrl + F', compound=LEFT, image="", command=findAllcallback)
editMenu.add_command(label="Select All", accelerator='Ctrl + A', compound=LEFT, image="", command=selectAllcallback)

#add the  menu to the menu bar
menubar.add_cascade(label='Edit',menu=editMenu)

#create the viewmwnu
viewMenu = Menu(menubar,tearoff=0)

#add menu items
viewMenu.add_checkbutton(label="Show Line Number", variable=showLineNumber)
viewMenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showInfoBarAtBottom)
viewMenu.add_checkbutton(label="Highlight Current Line", variable=highLightCurrentLine)

viewMenu.add_separator()

#create theme submenu items
themesMenu = Menu(viewMenu,tearoff=0)
for k in sorted(clrschms):
    themesMenu.add_radiobutton(label=k, variable=selectedTheme)


#add themes submenu items to view Menu
viewMenu.add_cascade(label="Themes",menu=themesMenu)


#add the menu to the menu bar
menubar.add_cascade(label='View',menu=viewMenu)

#create the aboutmenu
aboutMenu = Menu(menubar,tearoff=0)

#add menu items
aboutMenu.add_command(label="About", accelerator='', compound=LEFT, image=None, command=aboutcallback)
aboutMenu.add_separator()
aboutMenu.add_command(label="Help", accelerator='', compound=LEFT, image=None, command=helpcallback)

#add the menu to the menu bar
menubar.add_cascade(label='About',menu=aboutMenu)

#************************************************************************
#CREATE SHORT CUT SECTION
#************************************************************************
shortcutbar = Frame(root,  height=25, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)

#************************************************************************
#CREATE LATERAL LINE (FOR LINE NUMERING) SECTION
#************************************************************************

lnlabel = Label(root,  width=2,  bg = 'antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

#************************************************************************
#CREATE CENTRAL TEXT AREA SECTION
#************************************************************************
textPad = Text(root)
textPad.pack(expand=YES, fill=BOTH)

#************************************************************************
#CREATE RIGHT LATERAL SCROLL BAR SECTION
#************************************************************************
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)


root.mainloop()

