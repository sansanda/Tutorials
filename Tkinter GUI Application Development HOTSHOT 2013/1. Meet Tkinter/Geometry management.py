# *************************
# The pack geometry manager
# *************************

# When you insert button A in the root frame, it captures the left-most area of the frame, it expands, and fills the Y dimension.
# Because expand and fill options are specified in affirmative, it claims all the area it wants and fills the Y dimension.
# If you increase the size of the root window pulling it down, you will notice that the button A expands in the downward direction (along the Y coordinate)
# but a side-wise increase in the window does not result in a horizontal increase in the size of button A.
#
# When you insert the next button, B, into the root window, it picks up space from the remaining area but aligns itself to TOP, expand-fills the available area,
# and fills both X and Y coordinates of the available space.
#
# The third button, C, adjusts to the right-hand side of the remaining space.
# But because fill is specified as NONE, it takes up only that much space as is required to accommodate the text inside the button.
# If you expand the root window, the button C will not change its size.
#
# The anchor attribute used in some lines provides a means to position a widget relative to a reference point.
# If the anchor attribute is not specified, the pack manager places the widget in the center of the available space or the packing box .
# Other allowed options include the four cardinal directions (N, S, E, and W) and a combination of any two directions.
# Therefore, valid values for the anchor attribute are: CENTER (default), N, S, E, W, NW, NE, SW, and SE.

# The best way to study this piece of code would be to comment out all lines of code and introduce each successive button one after another.
# At each step, try to resize the window to see the effect it has on various buttons.

# from tkinter import *
# root = Tk()
# # Button(root, text="A").pack(side=LEFT, expand=YES, fill=Y)
# # Button(root, text="B").pack(side=TOP, expand=YES, fill=BOTH)
# # Button(root, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE)
# # Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y)
# # Button(root, text="E").pack(side=TOP, expand=NO, fill=BOTH)
# # Button(root, text="F").pack(side=RIGHT, expand=NO, fill=NONE)
# # Button(root, text="G").pack(side=BOTTOM, expand=YES, fill=Y)
# # Button(root, text="H").pack(side=TOP, expand=NO, fill=BOTH)
# # Button(root, text="I").pack(side=RIGHT, expand=NO)
# # Button(root, text="J").pack(anchor=SE)
# root.mainloop()


# from tkinter import *
# root = Tk()
# Button(root, text="ALL IS WELL").pack(side=TOP, expand=YES, fill=BOTH)
# Button(root, text="BACK TO BASICS").pack(side=TOP, expand=YES, fill=BOTH)
# Button(root, text="CATCH ME IF U CAN").pack(side=TOP, expand=YES, fill=BOTH)
# Button(root, text="LEFT").pack(side=LEFT, expand=YES, fill=BOTH)
# Button(root, text="CENTER").pack(side=LEFT, expand=YES, fill=BOTH)
# Button(root, text="RIGHT").pack(side=RIGHT, expand=YES, fill=BOTH, anchor=E)
#
# # Button(root, text="B").pack(side=TOP, expand=YES, fill=BOTH)
# # Button(root, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE)
# # Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y)
# # Button(root, text="E").pack(side=TOP, expand=NO, fill=BOTH)
# # Button(root, text="F").pack(side=RIGHT, expand=NO, fill=NONE)
# # Button(root, text="G").pack(side=BOTTOM, expand=YES, fill=Y)
# # Button(root, text="H").pack(side=TOP, expand=NO, fill=BOTH)
# # Button(root, text="I").pack(side=RIGHT, expand=NO)
# # Button(root, text="J").pack(anchor=SE)
# root.mainloop()


# *************************
# The grid geometry manager
# *************************

from tkinter import *
root = Tk()
Label(root, text="Username").grid(row=0, sticky=W)
Label(root, text="Password").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, sticky=W)
Entry(root).grid(row=1, column=1, sticky=W)
b = Button(root, text="Login", width=25)
b.grid(row=2, column=0, sticky=W, columnspan=2, padx=5, pady=5)
b.grid_forget()
b.grid(row=2, column=0, sticky=W, columnspan=2, padx=5, pady=5)

root.mainloop()

# *************************
# The place geometry manager
# *************************

from tkinter import *
root = Tk()
# Absolute positioning
Button(root,text="Absolute Placement").place(x=20, y=10)
# Relative positioning
Button(root, text="Relative").place(relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor = NE)
root.mainloop()
