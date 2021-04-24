from tkinter import *
import time
from tkinter import filedialog
from deepface import DeepFace
import random as rand

window_dim="600x600"

class ChatInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.botname = 'Movie Recommender'
		self.entry_count = 0
		self.ml_features = []

		# sets default bg for top level windows
		self.tl_bg = "#EEEEEE"
		self.tl_bg2 = "#EEEEEE"
		self.tl_fg = "#000000"
		self.font = "Verdana 10"


		self.text_frame = Frame(self.master, bd=6)
		self.text_frame.pack(expand=True, fill=BOTH)

		# scrollbar for text box
		self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
		self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

		# contains messages
		self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
							 bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
							 width=10, height=1)
		self.text_box.pack(expand=True, fill=BOTH)
		self.text_box_scrollbar.config(command=self.text_box.yview)

		self.text_box.configure(state=NORMAL)
		self.text_box.insert(END, self.botname+' : Hi, May I know Your name?\n')        


		# frame containing user entry field
		self.entry_frame = Frame(self.master, bd=1)
		self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

		# entry field
		self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
		self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
		# self.users_message = self.entry_field.get()

		# frame containing send button and emoji button
		self.send_button_frame = Frame(self.master, bd=0)
		self.send_button_frame.pack(fill=BOTH)

		# send button

		if self.entry_count < 0:
			
			self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
									  bd=1, command=lambda: self.send_message_insert_pause(None), activebackground="#FFFFFF",
									  activeforeground="#000000")
			self.send_button.pack(side=LEFT, ipady=8)
			self.master.bind("<Return>", self.send_message_insert_pause)
			
		else:

			self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
									  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
									  activeforeground="#000000")
			self.send_button.pack(side=LEFT, ipady=8)
			self.master.bind("<Return>", self.send_message_insert)


		self.last_sent_label(date="No messages sent.")


	def send_message_insert_pause(self, message):

		self.text_box.configure(state=NORMAL)
		self.text_box.insert(END, 'Your chat has been ended' + "\n")
		self.text_box.configure(state=DISABLED)
		self.text_box.see(END)


		
	def last_sent_label(self, date):

		try:
			self.sent_label.destroy()
		except AttributeError:
			pass

		self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
		self.sent_label.pack(side=LEFT, fill=X, padx=3)

	def bot_text(self, message):
		self.text_box.configure(state=NORMAL)
		self.text_box.insert(END, self.botname + " : " + message +  "\n")
		self.text_box.configure(state=DISABLED)
		self.text_box.see(END)
		time.sleep(0)

	def user_text(self):
		self.text_box.configure(state=NORMAL)
		user_input = self.entry_field.get()
		self.text_box.insert(END, "You : " + user_input + "\n")
		self.text_box.configure(state=DISABLED)
		self.text_box.see(END)
		self.entry_field.delete(0,END)
		time.sleep(0)
		return user_input


	def open_files(self):
		self.file = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("png files", "*.png")))
		return self.file

	def send_message_insert(self, message):

		if self.entry_count == 0:
			user_input = self.user_text()

			self.bot_text(user_input+", Kindly enter your image.")

			self.bot_text("Press Enter")			

		elif self.entry_count == 1:	
			self.image_path = self.open_files()
			print(self.image_path)
			self.bot_text("Please wait! Let me analyze it. :)")
			if self.image_path != ():
				obj1 = DeepFace.analyze(img_path = self.image_path, actions = ['age'])
				user_age = obj1["age"]
				self.bot_text('Predicted age is ' + str(user_age))

				obj2 = DeepFace.analyze(img_path = self.image_path, actions = ['gender'])
				user_gender = obj2["gender"]
				self.bot_text(str(user_gender))

				obj3 = DeepFace.analyze(img_path = self.image_path, actions = ['emotion'])	 			
				user_emotion = obj3["dominant_emotion"]
				self.bot_text('Predicted emotion is ' + str(user_emotion))
				
				if user_age < 18:
					
					if user_emotion == 'neutral':
						if user_gender == 'Man':
							mov_list = ["a1","b1","c1"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							self.bot_text()
						else:
							mov_list = ["a2","b2","c2"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)	
					elif user_emotion == 'sad':
						if user_gender == 'Man':
							mov_list = ["a3","b3","c3"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Kung Fu Panda"')
						else:
							mov_list = ["a4","b4","c4"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "The Little Mermaid."')	
					elif user_emotion == 'happy':
						if user_gender == 'Man':
							mov_list = ["a5","b5","c5"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Cars"')
						else:
							mov_list = ["a6","b6","c6"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Finding Nemo"')
					else:
						if user_gender == 'Man':
							mov_list = ["a7","b7","c7"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "The Lion King"')
						else:
							mov_list = ["a8","b8","c8"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Mulan"')
								


				elif user_age >= 18 and user_age < 35:
					# mov_list = dict()
					if user_emotion == 'neutral':
						if user_gender == 'Man':
							mov_list = ["a9","b9","c9"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Avengers"')
						else:

							mov_list = ["a10","b10","c10"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Yeh Jawani Hai Diwani."')								
					elif user_emotion == 'sad':
						if user_gender == 'Man':
							mov_list = ["a11","b11","c11"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Andhadhun"')
						else:
							mov_list = ["a12","b12","c12"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Chhichhore"')	
					elif user_emotion == 'happy':
						if user_gender == 'Man':
							mov_list = ["a13","b13","c13"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "De dana dhan"')
						else:
							mov_list = ["a14","b14","c14"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Luka Chuppi"')	
					else:
						if user_gender == 'Man':
							mov_list = ["a15","b15","c15"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Bhaag Milkha Bhaag"')
						else:
							mov_list = ["a16","b16","c16"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Stree"')


				elif user_age >= 35 :
					# mov_list = dict()
					if user_emotion == 'neutral':
						if user_gender == 'Man':
							mov_list = ["a17","b17","c17"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Jo Jeeta Wohi Sikandar"')
						else:
							mov_list = ["a18","b18","c18"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Saaransh"')								
					elif user_emotion == 'sad':
						if user_gender == 'Man':
							mov_list = ["a19","b19","c19"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Lakshya "')
						else:
							mov_list = ["a20","b20","c20"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Baghban"')	
					elif user_emotion == 'happy':
						if user_gender == 'Man':
							mov_list = ["a21","b21","c21"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Rocket Singh"')
						else:
							mov_list = ["a22","b22","c22"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Dil Chahta Hai"')	
					else:
						if user_gender == 'Man':
							mov_list = ["a23","b23","c23"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Lage Raho Munna Bhai"')
						else:
							mov_list = ["a24","b24","c24"]
							ch = rand.choice(mov_list)
							self.bot_text('You should watch ', ch)
							# self.bot_text('You should watch "Ankhon Dekhi"')

		self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
		self.entry_field.delete(0,END)
		#time.sleep(0)

		self.entry_count += 1

		print(self.entry_count)



gui=Tk()

chatbot = ChatInterface(gui)
gui.geometry(window_dim)
gui.title("Movie Recommender")
gui.iconbitmap('m.ico')
gui.mainloop()
