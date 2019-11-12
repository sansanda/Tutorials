from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os



#***************************
#File menu callbacks
#***************************

def newFilecallback(root,textPad,filename):
    root.title("Untitled")
    filename[0] = None
    textPad.delete(1.0, END)


def openFilecallback(root,textPad,filename):
    filename[0] = filedialog.askopenfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filename[0] == "":  # If no file chosen.
        filename[0] = None  # Absence of file.
    else:
        root.title(os.path.basename(filename[0]) + " - pyPad")  #
        # Returning the basename of 'file'
        textPad.delete(1.0, END)
        fh = open(filename[0], "r")
        textPad.insert(1.0, fh.read())
        fh.close()

def savecallback(root,textPad,filename):
    try:
        f = open(filename[0], 'w')
        letter = textPad.get(1.0, 'end')
        f.write(letter)
        f.close()
    except:
        saveAsFilecallback(root,textPad,filename)

def saveAsFilecallback(root,textPad,filename):
    try:
        # Getting a filename to save the file.
        filename[0] = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        fh = open(filename[0], 'w')
        textoutput = textPad.get(1.0, END)
        fh.write(textoutput)
        fh.close()
        root.title(os.path.basename(filename[0]) + " - pyPad")
    except:
        pass

def exitEditorcallback(root,textPad,filename):
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

#***************************
#Edit menu callbacks
#***************************

def undocallback(root,textPad,filename):
    textPad.event_generate("<<Undo>>")

def redocallback(root,textPad,filename):
    textPad.event_generate("<<Redo>>")


def cutcallback(root,textPad,filename):
    textPad.event_generate("<<Cut>>")

def pastecallback(root,textPad,filename):
    textPad.event_generate("<<Paste>>")

def copycallback(root,textPad,filename):
    textPad.event_generate("<<Copy>>")

#********************************************************
#FIND RELATED FUNCTIONS
#********************************************************

def findcallback(root,textPad,filename):

    def search_for(needle, cssnstv, textPad, t2, e):
        textPad.tag_remove('match', '1.0', END)
        count = 0
        if needle:
            pos = '1.0'
            while True:
                pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
                if not pos:
                    break
                lastpos = '%s+%dc' % (pos, len(needle))
                textPad.tag_add('match', pos, lastpos)
                count += 1
                pos = lastpos

        textPad.tag_config('match', foreground='red', background='yellow')
        e.focus_set()
        t2.title('%d matches found' % count)

    def close_search(textPad,t2):
      textPad.tag_remove('match', '1.0', END)
      t2.destroy()

    t2 = Toplevel(root)
    t2.title('Find')
    t2.geometry('262x65+200+250')
    t2.transient(root)
    Label(t2, text="Find All:").grid(row=0, column=0, sticky='e')
    v = StringVar()
    e = Entry(t2, width=25, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    e.focus_set()
    c = IntVar()
    Checkbutton(t2, text='Ignore Case', variable=c).grid(row=1, column=1, sticky='e', padx=2, pady=2)
    Button(t2, text="Find All", underline=0, command=lambda: search_for(v.get(), c.get(), textPad, t2, e)).grid(row=0,column=2,sticky='e' + 'w',padx=2,pady=2)

    t2.protocol('WM_DELETE_WINDOW', lambda: close_search(textPad,t2))#override close



def selectAllcallback(root,textPad,filename):
    textPad.tag_add('sel','0.0','end')

#***************************
#View menu callbacks
#***************************
def showLineNumbercallback(root,textPad,filename):
    print('show line number callback')

def showInfoBaratBottomcallback(root,textPad,filename):
    print('show inf bar at bottom callback')

def highlightCurrentLinecallback(root,textPad,filename):
    print('highlight current line callback')

def themescallback(root,textPad,filename):
    print('themes callback')

#***************************
#About menu callbacks
#***************************
def helpcallback(root,textPad,filename):
    messagebox.showinfo("Help","For help refer to book:\n Tkinter GUI Application\n Development Hotshot ", icon='question')

def aboutcallback(root,textPad,filename):
    messagebox.showinfo("About","Tkinter GUI Application\n Development Hotshot",icon='info')

