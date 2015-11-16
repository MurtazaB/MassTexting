from twilio.rest import TwilioRestClient

account = "ACCOUNT ID FROM TWILIO"
token = "SECRET TOKEN FROM TWILIO"
client = TwilioRestClient(account, token)

from tkinter import *
from tkinter import filedialog

import csv

class GUI:
	def __init__(self, window):
		self.win = window
		self.text = StringVar()
		self.phoneNumbers = []

		e = Entry(window, textvariable=self.text, width=100)
		e.pack()
		b1 = Button(window, text="Select File", command=self.getFile)
		b1.pack()
		b = Button(window, text="Send Message", command=self.sendMessage)
		b.pack()
	
	def sendMessage(self):
		text = self.text.get()
		
		for number in self.phoneNumbers:
			message = client.messages.create(to=number, from_="+14045946266", body=text)
			

	def getFile(self):
		filename = filedialog.askopenfilename(defaultextension='.csv')
		aFile = open(filename, 'r', newline='')
		Label(self.win, text=filename).pack()

		reader = csv.reader(aFile)

		for each in reader:
			self.phoneNumbers.append(each)


window = Tk()
window.title("Mass Text")
GUI(window)
windowainloop()