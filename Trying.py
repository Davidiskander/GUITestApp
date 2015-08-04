import Tkinter as tk

class Test(tk.Frame):
	def __init__(self):

		canvas = tk.Canvas()
		canvas.grid(row=0, column=0)

		self.photo = tk.PhotoImage(file='./icon.gif')

		canvas.create_image(0,0, image=self.photo)

	def run(self):

		self.mainloop()
if __name__=='__main__':

	test = Test()
	Test.run()