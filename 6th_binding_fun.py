import os
from Tkinter import *
root=Tk()

e=Entry(root)
e.grid(row=1)
username=e.get()
password="abc"
def adduser():
	os.system("useradd -s /bin/bash -d /home/%s -p %s %s -U"%(username,password,username))
#	print(e.get())

b=Button(root,text="submit",command=adduser)
b.grid(row=2)
root.mainloop()
