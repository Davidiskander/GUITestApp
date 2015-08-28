__author__ = 'davidiskander'
import Tkinter as tk
import glob
from Tkinter import *
from tkMessageBox import *
import serial
import sys
import os
from tkFileDialog import askdirectory
import time

content = ''
path = ''
newfile = ''
counter_open = ''
counter_close = ''
WAIT_TIME_S = ''
WAIT_TIME_M = ''
WAIT_TIME_L = ''

class testapp(tk.Frame):

	# Frame creation
	def __init__(self):
		tk.Frame.__init__(self, master=None, width=500,height=500)
		self.master.title ('Striiv GUI Tester')
		self.pack_propagate(0)
		self.pack()

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
		win = Window(Toplevel(self), 'Firmware, Single Char. Parsing Logs - Notifications', 'firmware')

	def gotosw(self):
		win = Window(Toplevel(self), 'Windows App Parsing Logs - Notifications', 'software')

	def gotosbtest(self):
		win = Window(Toplevel(self), 'Automatic Shield box Test', 'connectivity')

	def run(self):
		self.mainloop()

class Window():
	def __init__(self,master, t, w):
		self.master = master
		self.master.geometry ("480x330+500+50")
		self.master.title (t)

		path = StringVar
		counter_open = StringVar

		global WAIT_TIME_S
		global WAIT_TIME_M
		global WAIT_TIME_L

		self.INST = LabelFrame(self.master, text='Instructions', width=420, height=100, fg='black', font=('Verdana', 14, 'bold', 'italic'))
		self.INST.pack_propagate(0)
		self.INST.pack(pady=10)


		if w == 'firmware':

			# Path
			self.Instruction_label = Label(self.INST,text="1- Using the test app, offload logs to parse\n"
																	  " 2- Go to Parse, download files into a folder\n"
																   "3- Use the browse function below to find the folder then run the test\n"
																   "4- Find test report in the script directory folder ").pack(side=TOP)
			self.Label1 = Label(self.master,text="Select Your Folder").pack(side=TOP)
			self.entry = Entry(self.master, width=50, textvariable=path)
			self.entry.pack(side=TOP)
			self.entry.focus_set()
			self.b1=Button(self.master, text='Browse', command=self.open_file).pack(side=TOP)

			#  Run and get results
			self.back_button = Button(self.master, text='Done', command=self.back).pack(side=BOTTOM, fill=X)
			self.start_button = Button(self.master, bg='green', text='Run test & save results to a txt file', command=self.run_fw_script).pack(side=BOTTOM, padx = 20, pady=10)

		elif w == 'software':
			# Path
			self.Instruction_label = Label(self.INST,text="1- Using the test app, offload logs to parse\n"
																	  " 2- Go to Parse, download files into a folder\n"
																   "3- Use the browse function below to find the folder then run the test\n"
																   "4- Find test report in the script directory folder ").pack(side=TOP)
			self.Label1 = Label(self.master,text="Select Your Folder").pack(side=TOP)
			self.entry = Entry(self.master, width=50, textvariable='path')
			self.entry.pack(side=TOP)
			self.entry.focus_set()
			self.b1=Button(self.master, text='Browse', command=self.open_file).pack(side=TOP)

			#  Run and get results
			self.back_button = Button(self.master, text='Done', command=self.back).pack(side=BOTTOM, fill=X)
			self.start_button = Button(self.master, bg='green', text='Run test & save results to a txt file', command=self.run_sw_script).pack(side=BOTTOM, padx = 20, pady=10)


		elif w == 'connectivity':
			# Head
			self.Instruction_label = Label(self.INST,fg='Red',text="This is used to input the time intervals for the box to open and close\n"
																	  " Make sure that the compressor and the box are connected and secured safely").pack(side=TOP)
			# Time Interval
			self.FWL1 = Label(self.master, text='Input time intervals in minutes:').pack()
			self.entry1 = Entry(self.master).pack()
			self.entry2 = Entry(self.master).pack()
			self.entry3 = Entry(self.master).pack()

			# Run and get results
			self.back_button = Button(self.master, text='Done', command=self.back).pack(side=BOTTOM, fill=X)

			self.counter1 = Label(self.master, fg="dark green")
			#self.counter1.config(text='Box opened: ' + counter_open)
			self.counter1.pack(side=BOTTOM)

			#self.Counter_Close = Label(self.master, fg="dark green", command=counter_close).pack(side=BOTTOM)
			self.Stop_Button = tk.Button(self.master, text='Stop', width=25, command=self.back).pack(side=BOTTOM)
			self.start_button = Button(self.master, text='Start', width=25, command=self.sheildbox_test).pack(side=BOTTOM)
			WAIT_TIME_S = self.entry1.get()
			WAIT_TIME_M = self.entry2.get()
			WAIT_TIME_L = self.entry3.get()

	def run_fw_script(self):
		date_time = time.strftime(" %Y-%m-%d %H-%M-%S-%p")
		print('Creating new text file')
		name = 'FW Parsing Logs'+ date_time +'.txt'

		try:
			newfile = open(name, 'w')
			print ('Created the file')

		except:
			print('Something went wrong! Can\'t tell what?')
			sys.exit(0)

		device_id= ['*_H3C88AED8BABDC0F34DC_*.txt','*_H8DFA9C8C8902F57131A_*.txt', '*_H33B116C5459404C247A_*.txt', '*_H8183A6FCCA70B8193BC_*.txt']
		print('Reading Devices IDs')
		newfile.write('Starting FW parsing Logs')
		for id in device_id:
			print('Parsing Logs ...')
			newfile.write('\n\nDevice:' + id)
			for txtfile in glob.glob(os.path.join(path, id)):
				with open(txtfile, 'rU') as f:
					content = f.readlines()
					for line in content:

						if ("NOTIF:alloc/id:" in line):
							a = "\n|Notification ID: %s" %line [-10:-1]
							aa = "|Arrived at: %s\t|" %line[:20]
							newfile.write(str(a) + "\t" + str(aa))

						if ('NOTIF:attrec:Test' in line):
							b = "Type: Meeting"
							bb = "| Preparing!"
							bbb = "| Info: %s" %line[-9:-1]
							newfile.write(str(b) + "\t" + str(bb) + "\t" + str(bbb))

						if ("+1 (408) 606-2975" in line):
							c = "Type: SMS"
							cc = "| Preparing!"
							newfile.write(str(c) + "\t" + str(cc))

						elif ("NOTIF:post:/id" in line):
							d = "|Sent"
							newfile.write(str(d) + "\t")

						elif ('err_code:3' in line):
							e = "|Fail; error_3"
							newfile.write(str(e))

						elif ('err_code:4' in line):
							f = "|Fail; error #4"
							newfile.write(str(f))

						elif ('err_code:5' in line or  'err_code:7' in line):
							g = "|Fail; error #5&7"
							newfile.write(str(g))


			newfile.write('\n')
		print('Finished Parsing Logs')
		newfile.close()
		print('Closing the file')


	def run_sw_script(self):
		date_time = time.strftime(" %Y-%m-%d %H-%M-%S-%p")
		print('Creating new text file')
		name = 'WinApp Parsing Logs'+ date_time +'.txt'

		try:
			newfile = open(name, 'w')
			print ('Created the file')

		except:
			print('Something went wrong! Can\'t tell what?')
			sys.exit(0)

		a = []
		b = []

		with open(path,'rU') as x:
			lines = x.readlines()
			for line in lines:

				if ("notification:" in line):
					a.append (line [7:])
				if ("send title:" in line):
					b.append([line [7:]])
			newfile.write(str(a) + str(b))
		newfile.close()

	def sheildbox_test(self):
		global counter_open
		global counter_close
		OPEN = "OPEN\f"
		CLOSE = "CLOSE\f"

		print "Time intervals: %s, %s & %s" %(WAIT_TIME_S, WAIT_TIME_S, WAIT_TIME_S)

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
				counter_open += 1

				print "Closing box"
				print ser.write(CLOSE)
				time.sleep (WAIT_TIME_M)
				counter_close += 1

				print "Opening box"
				print ser.write(OPEN)
				time.sleep (WAIT_TIME_M)
				counter_open += 1

				print "Closing box"
				print ser.write(CLOSE)
				time.sleep (WAIT_TIME_L)
				counter_close += 1

				print "Opening box"
				print ser.write(OPEN)
				time.sleep (WAIT_TIME_L)
				counter_open += 1

				print "Closing box"
				print ser.write(CLOSE)
				time.sleep (WAIT_TIME_S)
				counter_close += 1

		ser.close()

	def back(self):
		self.master.destroy()

	def open_file(self):
		global content
		global path
		path = askdirectory()
		self.entry.delete(0, END)
		self.entry.insert(0, path)

if __name__=='__main__':
	app = testapp()
	app.run()
