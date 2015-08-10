__author__ = 'davidiskander'
import Tkinter as tk
import os
import glob
from Tkinter import *
from tkMessageBox import *
import serial
import sys
import time
import os
from tkFileDialog import askopenfilename

content = ''
file_path = ''

def open_file():
	global content
	global file_path

	filename = askopenfilename()
	infile = open(filename, 'r')
	content = infile.read()
	file_path = os.path.dirname(filename)
	entry.delete(0, END)
	entry.insert(0, file_path)
	return content

def process_file(content):
	print content

class testapp(tk.Frame):

	# Frame creation
	def __init__(self):
		tk.Frame.__init__(self, master=None, width=500,height=500)
		self.master.title('Stiiv GUI Tester ')
		self.pack_propagate(0)
		self.pack()
		#self.userentry = DoubleVar()

		self.photo = PhotoImage(file="icon.gif")
		self.w = Label(self, image=self.photo)
		self.w.photo = self.photo
		self.w.pack(pady=20)

		# Frames for organizing tests
		self.KK = LabelFrame(self, text='Windows Platform Tests', fg='black', width=400, height=100, font=('Verdana', 14, 'bold', 'italic'))
		self.KK.pack_propagate(0)
		self.KK.pack(pady=10)

		self.MM = LabelFrame(self, text='iOS Platform Tests', fg='black', width=400, height=50, font=('Verdana', 14, 'bold', 'italic'))
		self.MM.pack_propagate(0)
		self.MM.pack_forget()
		self.MM.pack(pady=10)

		self.NN = LabelFrame(self, text='Android Platform Tests', fg='black', width=400, height=50, font=('Verdana', 14, 'bold', 'italic'))
		self.NN.pack_propagate(0)
		self.NN.pack_forget()
		self.NN.pack(pady=10)

		self.OO = LabelFrame(self, text='Connectivity', fg='black', width=400, height=50, font=('Verdana', 14, 'bold', 'italic'))
		self.OO.pack_propagate(0)
		self.OO.pack(pady=10)

		# Button 1
		self.fw_button = tk.Button(self.KK, text='Notifications - FW Parsing Logs', command=self.gotofw, font=("Helvetica", 14))
		self.fw_button.config(relief=FLAT, width=30, height=2)
		self.fw_button.pack_propagate(0)
		self.fw_button.pack()

		# Button 2
		self.sw_button = tk.Button(self.KK, text='Notifications - SW Parsing Logs', command=self.gotosw, font=("Helvetica", 14))
		self.sw_button.config(relief=FLAT, width=30, height=2)
		self.sw_button.pack_propagate(0)
		self.sw_button.pack()

		# Button 3
		self.sb_button = tk.Button(self.OO, text='Automatic Shield-Box Test', command=self.gotosbtest, font=("Helvetica", 14))
		self.sb_button.config(relief=FLAT, width=30, height=2)
		self.sb_button.pack_propagate(0)
		self.sb_button.pack()

		#self.f = tk.Label(self, text='Windows Platform Tests')#.place(relx=.06, rely=0.125,anchor=W)
		#self.f.pack(fill=tk.X)

		#Submit button
		#self.submit_button = tk.Button(self, text="Submit", command=self.on_button)
		#self.submit_button.pack(fill=tk.X, side=tk.BOTTOM)

		# Entry
		#self.entry = tk.Entry(self, textvariable=self.userentry)
		#self.entry.bind=('<Return>',self.on_button)
		#self.entry.pack(fill=tk.X, side=tk.BOTTOM)


		self.createwidgets()

	def on_button(self):
		print(self.entry.get())

	def createwidgets(self):
		self.makeMenuBar()
		self.makeToolBar()

	def makeToolBar(self):
		toolbar = Frame(self, cursor='hand2', relief=FLAT, bd=2)
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
		pulldown.add_command(label='Read me!',   command=self.notdone)
		pulldown.add_command(label='About!',    command=self.greeting)
		pulldown.add_separator()
		pulldown.add_command(label='Delete',  command=self.greeting)
		pulldown.entryconfig(4, state=DISABLED)
		self.menubar.add_cascade(label='Help!', underline=0, menu=pulldown)

	def greeting(self):
		showinfo('About', 'Striiv Inc.'
						  '\nAuthor: David Iskander'
						  '\nBeta ver.1     AUG2016')
	def notdone(self):
		self.showerror('Not implemented', 'Not yet available')
	def quit(self):
		if askyesno('Verify quit', 'Are you sure you want to quit?'):
			Frame.quit(self)

	def gotofw(self):
		win = Window(Toplevel(self), 'FW Test', 'firmware' )

	def gotosw(self):
		win = Window(Toplevel(self), 'SW TEST', 'software')

	def gotosbtest(self):
		win = Window(Toplevel(self), 'Shield-Box Test', 'connectivity')

	def run(self):
		self.mainloop()

class Window():
	def __init__(self,master, t, w):
		self.master = master
		self.master.geometry ("500x200+300+300")
		self.master.title = t

		self.devices = DoubleVar()
		self.devices = []
		self.time_interval = DoubleVar()
		self.file_path = StringVar

		if w == 'firmware':
			# Devices
			self.FWL1 = Label(self.master, text='Input devices IDs here:', fg='blue').grid(row=1, column=1)
			self.entry1 = Entry(self.master, fg='blue', textvariable=self.devices).grid(row=1, column=3)

			# Path
			self.Label1 = Label(self.master,fg='blue',text="Select Your File").grid(row=2, column=1)
			self.entry = Entry(self.master, textvariable=self.file_path).grid(row=2, column=2)
			self.b1=Button(self.master, text='Browse', command=open_file).grid(row=2, column=3)
			self.b2=Button(self.master, text="Process Now", command=lambda: process_file).grid(row=5, column=2)

			#  Run and get results
			self.start_button = Button(self.master, text='Start Test', command=self.run_fw_script).grid(row=7, column=2)
			self.extract_button = Button(self.master, text='Extract Result!', command=self.notdone).grid(row=8, column=2)
			self.back_button = Button(self.master, text='Back', command=self.back).grid(row=9, column=3)

			#self.entry2.bind('<B1-Motion>',self.run_fw_script)


		elif w == 'software':
			# Path
			self.Label1 = Label(self.master,fg='blue',text="Select Your File").grid(row=2, column=1)
			self.entry = Entry(self.master, textvariable=self.file_path).grid(row=2, column=2)
			self.b1=Button(self.master, text='Browse', command=open_file).grid(row=2, column=3)
			self.b2=Button(self.master, text="Process Now", command=lambda: process_file).grid(row=5, column=2)

			#  Run and get results
			self.start_button = Button(self.master, text='Start Test', command=self.run_fw_script).grid(row=7, column=2)
			self.extract_button = Button(self.master, text='Extract Result!', command=self.notdone).grid(row=8, column=2)
			self.back_button = Button(self.master, text='Back', command=self.back).grid(row=9, column=3)


		elif w == 'connectivity':
			# Time Interval
			self.entry1 = Entry(self.master, fg='blue', textvariable=self.time_interval).grid(row=1, column=3)
			self.FWL1 = Label(self.master, text='Input time intervals in minutes:', fg='blue').grid(row=1, column=1)

			# Button
			self.start_button = Button(self.master, text='Start Test', command=self.sheildbox_test).grid(row=5, column=2)
			self.extract_button = Button(self.master, text='Extract Result!', command=self.notdone).grid(row=6, column=2)
			self.back_button = Button(self.master, text='Back', command=self.back).grid(row=9, column=3)

	def run_fw_script(self):

		notif_id = 0
		#device_id= ['*_H3C88AED8BABDC0F34DC_*.txt', '*_H33B116C5459404C247A_*.txt']
		device_id= [self.devices]

		#print (self.entry2.get())
		#print "/Users/davidiskander/Desktop/Parse/5"
		#self.path = raw_input('what\'s the logs directory ?\n')

		for id in device_id:
			print "Device: %s" % id
			for txtfile in glob.glob(os.path.join(file_path, id) ):
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

	def run_sw_script(self):
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

	def sheildbox_test(self):
		OPEN = "OPEN\f"
		CLOSE = "CLOSE\f"
		WAIT_TIME_S = 60
		WAIT_TIME_M = 900
		WAIT_TIME_L = 1800

		ser = ser = serial.Serial(port='/dev/cu.usbserial',
								  baudrate=9600,
								  parity=serial.PARITY_NONE,
								  stopbits=serial.STOPBITS_ONE,
								  bytesize=serial.EIGHTBITS,
								  timeout=1)

		if ser.isOpen():
			while True:
				print "Opening box"
				print ser.write(OPEN)
				time.sleep (WAIT_TIME_S)

				print "Closing box"
				print ser.write(CLOSE)
				time.sleep (WAIT_TIME_M)

				print "Opening box"
				print ser.write(OPEN)
				time.sleep (WAIT_TIME_M)

				print "Closing box"
				print ser.write(CLOSE)
				time.sleep (WAIT_TIME_L)

				print "Opening box"
				print ser.write(OPEN)
				time.sleep (WAIT_TIME_L)

				print "Closing box"
				print ser.write(CLOSE)
				time.sleep (WAIT_TIME_S )
		ser.close()

	def back(self):
		self.master.destroy()

	def notdone(self):
		self.master.showerror('Not implemented', 'Not yet available')





if __name__=='__main__':
	app = testapp()
	app.run()
