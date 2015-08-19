from tkFileDialog import askdirectory
from Tkinter import *
import os
import glob


content = ''
path = ''


def open_file():
	global content
	global path
	path = askdirectory()
	entry.delete(0, END)
	entry.insert(0, path)


def script():
	device_id= ['*_H3C88AED8BABDC0F34DC_*.txt','*_H8DFA9C8C8902F57131A_*.txt', '*_H33B116C5459404C247A_*.txt', '*_H8183A6FCCA70B8193BC_*.txt']

	for id in device_id:
		print "\nDevice: %s" % id

		for txtfile in glob.glob(os.path.join(path, id)):
			with open(txtfile, 'rU') as f:

				content = f.readlines()
				for line in content:

					if ("NOTIF:alloc/id:" in line):
						print "\n|Notification ID: %s\t|Arrived at: %s\t|" %(line [-10:-1] , line[:20]),
					if ('NOTIF:attrec:Test' in line):
						print "Type: Meeting\t| Preparing! \t | Info: %s\t|" %line[-9:-1],
					if ("+1 (408) 606-2975" in line):
						print "Type: SMS \t| Preparing! \t|",
					elif ('NOTIF:post:/id' in line):
						print "Sent \t|",
					elif ('err_code:3' in line):
						print "Fail; error_3",
					elif ('err_code:4' in line):
						print "Fail; error #4",
					elif ('err_code:5' in line or  'err_code:7' in line):
						print "Fail; error #5&7",


#~~~~~~ GUI ~~~~~~~~

root = Tk()
root.title('Test')
root.geometry("598x150+250+100")

mf = Frame(root)
mf.pack()


f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()

path = StringVar

Label(f1,text="Select Your File").grid(row=0, column=0, sticky='e')
entry = Entry(f1, width=50, textvariable=path)
entry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f1, text="Browse", command=open_file).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
Button(f2, text="Process Now", width=32, command=script).grid(sticky='ew', padx=10, pady=10)


root.mainloop()