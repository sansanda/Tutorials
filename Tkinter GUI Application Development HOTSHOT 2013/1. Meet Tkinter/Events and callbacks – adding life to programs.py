# **********************************************
# Events and callbacks – adding life to programs
# **********************************************


# **********************************************
# Command binding
# **********************************************
# from tkinter import *
# root = Tk()
#
# def my_callback ():
#   # do something
#     pass
# Button(root,text="Click",command= my_callback)
#
# def my_callback (somearg):
#     #do something with argument
#     pass
#
# Button(root,text="Click",command=lambda: my_callback ('some argument'))

# **********************************************
# Event binding
# **********************************************

from tkinter import *
root = Tk()
Label(root, text='Click at different\n locations in the frame below').pack()
def mycallback(event):
  print (dir(event))
  print ("you clicked at", event.x, event.y)
myframe = Frame(root, bg='khaki', width=130, height=80)
myframe.bind("<Button-1>", mycallback)
myframe.pack()
root.mainloop()



# **********************************************
# Event pattern
# **********************************************



