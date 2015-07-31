__author__ = 'davidiskander'
import Tkinter as tk
import os
import glob
from Tkinter import *
from tkMessageBox import *
import cStringIO


def run_fw_script():
	notif_id = 0
	device_id= ['*_H3C88AED8BABDC0F34DC_*.txt', '*_H33B116C5459404C247A_*.txt']

	print "/Users/davidiskander/Desktop/Parse/5"
	path = raw_input('what\'s the logs directory ?\n')

	for id in device_id:
		print "Device: %s" % id
		for txtfile in glob.glob(os.path.join(path, id) ):
			with open(txtfile, 'rU') as f:
				lines = f.readlines()

				for line in lines:

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


		print "\n"

def run_sw_script():
	a = []
	b = []


	print "\n\n What is the file name?"
	z = raw_input(">")

	with open(z,'rU') as x:
		lines = x.readlines()
		for line in lines:

			if ("notification:" in line):
				a.append (line [7:])
			if ("send title:" in line):
				b.append([line [7:]])
		return (a,b)

#def sheildbox_test():

def about():
	print("About!")

class testapp(tk.Frame):

	# Frame creation
	def __init__(self):
		tk.Frame.__init__(self, master=None, width=500,height=200)
		self.master.title('Stiiv QA Tester \"Demo\" ')
		self.pack_propagate(0)
		self.pack()

		# Button 1
		self.fw_button = tk.Button(self, text='FW Parsing Logs', command=run_fw_script)
		self.fw_button.pack(fill=tk.X, side=tk.TOP)

		# Button 2
		self.sw_button = tk.Button(self, text='SW Parsing Logs', command=run_sw_script)
		self.sw_button.pack(fill=tk.X, side=tk.TOP)

		# Button 3
		#self.sb_button = tk.Button(self, text='Connectivity Sheild Test', command=sheildbox_test)
		#self.sb_button.pack(fill=tk.X, side=tk.TOP)

		# Label
		self.L1 = Label(text="Input Here:")
		self.L1.pack( side = tk.TOP)

		# Entry
		self.E1 = Entry( bd =5)
		self.E1.pack(side = tk.TOP)

		# Put the controls on the form
				#self.submit = tk.Button(self, text = 'Submit', width=20,command=get_input)



		#self.something.pack(fill=tk.X, side=tk.BOTTOM)
		#self.submit.pack(fill=tk.X, side=tk.BOTTOM)


	def run(self):
		''' Run the app '''

		self.mainloop()

class NewMenuDemo(tk.Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.L = Label(self, text='Test instructions:') #REPLACE WITH FUNCTION THAT PRINTS INSTRUCTIONS FOR EACH TEST
		#self.pack(expand=YES, fill=BOTH, side=tk.BOTTOM )
		self.createWidgets()
		#self.master.title("Striiv QA Tester")
		self.master.iconname("tkpython")

	def createWidgets(self):
		self.makeMenuBar()
		self.makeToolBar()
		self.L.config(relief=SUNKEN, width=40, height=10, bg='white')
		self.L.pack(expand=YES, fill=BOTH)

	def makeToolBar(self):
		toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
		toolbar.pack(side=BOTTOM, fill=X)
		Button(toolbar, text='Quit',  command=self.quit    ).pack(side=RIGHT)
		Button(toolbar, text='About', command=self.greeting).pack(side=LEFT)

	def makeMenuBar(self):
		self.menubar = Menu(self.master)
		self.master.config(menu=self.menubar)
		self.fileMenu()
		self.editMenu()

	def fileMenu(self):
		pulldown = Menu(self.menubar)
		pulldown.add_command(label='Open...', command=self.notdone)
		pulldown.add_command(label='Quit',    command=self.quit)
		self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

	def editMenu(self):
		pulldown = Menu(self.menubar)
		pulldown.add_command(label='Paste',   command=self.notdone)
		pulldown.add_command(label='Spam',    command=self.greeting)
		pulldown.add_separator()
		pulldown.add_command(label='Delete',  command=self.greeting)
		pulldown.entryconfig(4, state=DISABLED)
		self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

	def greeting(self):
		showinfo('About', 'Striiv Inc.'
						  '\nAuthor: David Iskander'
						  '\nBeta ver.1     AUG2016')
	def notdone(self):
		showerror('Not implemented', 'Not yet available')
	def quit(self):
		if askyesno('Verify quit', 'Are you sure you want to quit?'):
			Frame.quit(self)

if __name__=='__main__':
	app = testapp()
	#app.run()
	NewMenuDemo().mainloop()  # if I'm run as a script