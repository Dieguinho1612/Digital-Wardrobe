"""This program uses Tkinter to create a virtual wardrobe based on my clothes. These are divided into 4 classes:
1. T-Shirts, consisting of two categories: 1 stands for the Good T-Shirts, 2 for the Mediocre T-Shirts
2. Shorts, consisting of two categories: 1 stands for actual Shorts, 2 for Pants (which were added only later, hence the naming)
3. Second Layers, which are most likely shirts and jackets, but were named like this to emphasize that they go on top of a T-Shirt
4. Shoes
This virtual wardrobe should only show combination of clothing pieces that all match each other at any time. 
T-Shirts and Shorts have to match each other. The Second Layer has to match with the T-shirt and with the Short. Shoes have to match with the Short.
On the sides of the Main-Frame there will be 5 visual buttons: One to create a random (matching) outfit, one each to show all T-Shirts, Shorts, Second Layers and Shoes.  
Clicking on the T-Shirts/Shorts button will show all T-Shirts/Shorts. The user will then click on one of them to select it.
Then all matchable items of Shorts/T-Shirts will we shown, the user has to select one again.
Afterwards the program returns to the Main-Frame and a Second Layer and Shoes can be choosen, only matchable items will be shown.
It is also possible to do it the opposite order and first choose a Second Layer and/or Shoes. This way all items will be shown.
When afterwards choosing a T-Shirt/Short, only items matchable with the chosen Second Layer and/or Shoes will be shown.
Since the Second Layer and the Shoes are considered optional, the "see all" button changes to a "remove" button by turning it red as soon as one item is chosen.
In the middle of the Main-Frame the selected Outfit will be displayed. Every clothing-piece is a button itself. 
Clicking on it shows all the other options from clothing pieces of the same kind that match the current outfit.
It is also possible to use the keyboard-arrows. In the Main-Frame, Left/Right will change the T-Shirt to the previous/next one that matches the current outfit.
Down and Up change the Shorts to the previous/next one that matches the current outfit. These keys are also used to scroll the other frames.
The remaining short-cuts are Escape, which closes the entire program. Return create a random outfit when on Main-Frame.
Backspace returns to the Main-Frame and Delete removes the selected outfit and returns everything to the initial status."""

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import pygame

root = Tk()
root.title("Armario Modico")
root.geometry(str(root.maxsize()[0])+"x"+str(root.maxsize()[1]))
root.state('zoomed')
root.bind("<Escape>", lambda e: root.destroy())
root.iconbitmap("images/Layout/clothes.ico")
root.overrideredirect(True)

#Frames
f = Frame(root, width=root.maxsize()[0], height=root.maxsize()[1])							#mainframe
f.grid(row=0, column=0)
f.focus_set()
f_shirts = Frame(root, width=root.maxsize()[0], height=root.maxsize()[1])					#frame so list all tshirts
f_shorts = Frame(root, width=root.maxsize()[0], height=root.maxsize()[1])					#frame to list all shorts and pants
f_seclayer = Frame(root, width=root.maxsize()[0], height=root.maxsize()[1])					#frame to list all second layers such as shirts
f_shoes = Frame(root, width=root.maxsize()[0], height=root.maxsize()[1])					#frame to list all shoes
f_matches = Frame(root, width=root.maxsize()[0], height=root.maxsize()[1])					#frame to list all matching clothes

#background
bg = ImageTk.PhotoImage(Image.open("images/Layout/bg.png").resize(root.maxsize()))						#load background image
for fr in [f, f_shoes]:															#put it in all frames that wont have a canvas
	Label(fr, image=bg, borderwidth=0).grid(row=0, column=0, rowspan=8, columnspan=100)

#sounds
playlist = [
"Dynoro & Gigi D’Agostino - In My Mind.mp3",
"El Profesor - Bella Ciao (HUGEL Remix) [Lyric Video].mp3",
"Two Feet - Go F_ck Yourself.mp3",
"Infinity Ink - Infinity (Dubdogz & Bhaskar Remix) (Bass Boosted).mp3",
"MEDUZA, Goodboys - Piece Of Your Heart (Visualizer) ft. Goodboys.mp3",
"Oliver Heldens - Fire In My Soul (Audio) ft. Shungudzo.mp3",
"SAINt JHN - Roses (Imanbek Remix).mp3",
"Stromae - Alors On Danse (Dubdogz Remix) (Bass Boosted).mp3"]

random.shuffle(playlist)

pygame.mixer.init()
pygame.mixer.music.load("sound/" + playlist.pop())
pygame.mixer.music.play()


#Classes of Clothes
class T_Shirts:

	def __init__(self, n, match):															#shirts are objects, class 1 are the better tshirts
		try:
			self.img = ImageTk.PhotoImage(Image.open("images/T-Shirts/T"+str(n)+"_1.png").resize((230,310)))	#distinguish class by default filename of their image -> y to x factor 0.742
			self.category = 1
		except FileNotFoundError:
			self.img = ImageTk.PhotoImage(Image.open("images/T-Shirts/T"+str(n)+"_2.png").resize((230,310)))
			self.category = 2
		self.match = match																	#self.match will be list of all matching shorts/pants

class Shorts:																				#in this program shorts stands for shorts as well as for pants

	def __init__(self, n, match):
		try:																				#category 1 are shorts, distinguish by default filename of image
			self.img = ImageTk.PhotoImage(Image.open("images/Shorts/S"+str(n)+"_1.png").resize((190,422)))	#img is short image put into pants-background, to fit the outfit -> y to x factor 0.45
			self.img1 = ImageTk.PhotoImage(Image.open("images/Shorts/S"+str(n)+"_1_.png").resize((190,271)))	#img1 is short in original size to fit frame of f_shorts -> y to x factor 0.7
			self.category = 1
		except FileNotFoundError:
			self.img = ImageTk.PhotoImage(Image.open("images/Shorts/S"+str(n)+"_2.png").resize((190,422)))	#category 2 are pants
			self.category = 2
		self.match = match																		#self.match will be list of all matching tshirts
	
class Second_Layer:																			#second layer are shirts and jackets
	
	def __init__(self, n, match_shirt, match_short,match_shoe):
		self.img = ImageTk.PhotoImage(Image.open("images/Second Layer/sec"+str(n)+".png").resize((230,310)))
		self.img_half = ImageTk.PhotoImage(Image.open("images/Second Layer/sec"+str(n)+"_half.png").resize((115,310)))
		self.match = []
		self.match_shirt = match_shirt 													#list of matching shirts
		self.match_short = match_short 													#list of matching shorts
		self.match_shoe = match_shoe													#list of matching shoes
		for t in match_shirt:															#self.match is list of all tuples being combination of matching shirts and shorts
			for s in match_short:
				if s in t.match:
					self.match.append((t,s))

class Shoes:
	
	def __init__(self, n, match_shirt, match_short):
		self.img = ImageTk.PhotoImage(Image.open("images/Shoes/shoe"+str(n)+".png").resize((139,120)))	#y to x factor 1.16
		self.img1 = ImageTk.PhotoImage(Image.open("images/Shoes/shoe"+str(n)+".png").resize((200,172)))
		self.avb = 0
		self.match = []
		self.match_shirt = match_shirt
		self.match_short = match_short													
		for t in match_shirt:															#self.match is list of all tuples being combination of matching shirts and shorts
			for s in match_short:
				if s in t.match:
					self.match.append((t,s))

#Read in the data of my clothes
exec(open("read_in_clothes.py").read())

#global variables
placeholder_layer = Second_Layer(0,shirts,shorts,shoes)			#if no second_layer/shoe is selected, the default-value has to match with every shirt and short, so all of them can be displayed normally
placeholder_shoe = Shoes(0,shirts,shorts)

selected_shirt = None
selected_short = None
selected_layer = placeholder_layer
selected_shoe = placeholder_shoe

options = []													#to choose a random option later

#images
random_img = ImageTk.PhotoImage(Image.open("images/Buttons/random.png").resize((380,90)))
tshirt_img = ImageTk.PhotoImage(Image.open("images/Buttons/tshirts.png").resize((380,90)))
pants_img = ImageTk.PhotoImage(Image.open("images/Buttons/pants.png").resize((380,90)))
layer_img = ImageTk.PhotoImage(Image.open("images/Buttons/layer.png").resize((380,90)))
layer_remove_img = ImageTk.PhotoImage(Image.open("images/Buttons/layer_remove.png").resize((380,90)))
sneaker_img = ImageTk.PhotoImage(Image.open("images/Buttons/sneaker.png").resize((380,90)))
sneaker_remove_img = ImageTk.PhotoImage(Image.open("images/Buttons/sneaker_remove.png").resize((380,90)))

#functions
def create_canvas(canvas, frame):
	"""create canvas that is scrollable with up and down arrows"""

	#pack canvas and create background image
	canvas.pack(side=LEFT, fill=BOTH, expand=1)
	canvas.create_image(0,0, anchor="nw", image=bg, tags="background")

	#customize scroll-function such that background image moves along
	def custom_yview_scroll(i):
		canvas.yview_scroll( i, "units")
		x = canvas.canvasx(0)
		y = canvas.canvasy(0)
		canvas.coords("background", x,y)

	#define scrollable region and bind keys
	canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
	canvas.focus_set()
	canvas.bind("<Up>",  lambda event: custom_yview_scroll(-1))
	canvas.bind("<Down>",  lambda event: custom_yview_scroll(1))
	canvas.bind("<Return>",lambda e: choose_random_option(frame))

def choose_randomly():
	"""create a random outfit"""

	global selected_shirt
	global selected_short
	global selected_layer
	global selected_shoe
	
	remove_second_layer()
	remove_shoe()
	
	#rechoose randomly until an outfit with existing matching shoes is selected
	existence = False
	while existence==False:
		selected_shirt = random.choice(shirts)
		update_shirt()
		selected_short = random.choice(selected_shirt.match)
		update_short()
		
		#check if matching shoes exist
		for shoe in shoes:
			if selected_shirt in shoe.match_shirt and selected_short in shoe.match_short:
				existence=True
				break

	#choose matching shoes, then update buttons
	while True:
		selected_shoe = random.choice(shoes)
		if selected_shirt in selected_shoe.match_shirt and selected_short in selected_shoe.match_short:
			break

	Button_open_shoes.grid_remove()
	Button_remove_shoes.grid(row=4, column=4, padx=20, pady=0, rowspan=1)
	Outfit_shoe.grid(row=5, column=2, rowspan=2, padx=(223,203), pady=(70,0))
	Outfit_shoe.configure(image=selected_shoe.img)
	
	#check if matching second layer exists
	existence=False
	for sec in second_layers:
		if selected_shirt in sec.match_shirt and selected_short in sec.match_short and selected_shoe in sec.match_shoe:
			existence=True
			break
	
	#choose a matching second layer, then update buttons
	if existence==True:
		while True:
			selected_layer = random.choice(second_layers)
			if selected_shirt in selected_layer.match_shirt and selected_short in selected_layer.match_short and selected_shoe in selected_layer.match_shoe:
				break
	
		Button_open_seclay.grid_remove()
		Button_remove_seclay.grid(row=2, column=4, padx=20, pady=0, rowspan=1)
		Outfit_seclay.grid(row=0, column=2, rowspan=3, padx=(90,203), pady=(0,35))
		Outfit_seclay.configure(image=selected_layer.img_half)	
f.bind("<Return>",lambda e: choose_randomly())


def remove_outfit():	
	"""set everything to initial status"""
	
	global selected_shirt
	global selected_short
	
	selected_shirt = None
	Outfit_shirt.configure(image="")
	Outfit_shirt.configure(state="disabled")
	
	selected_short = None
	Outfit_short.configure(image="")
	Outfit_short.configure(state="disabled")
	
	remove_second_layer()
	remove_shoe()
	
	#goeback() does not handle f_matches
	try:
		canvas_matches.destroy()
	except:
		pass
	f_matches.grid_remove()
	goback("event")
root.bind("<Delete>",lambda e: remove_outfit())


def update_shirt():
	Outfit_shirt.configure(image=selected_shirt.img)
	Outfit_shirt.configure(state="active")


def update_short():
	Outfit_short.configure(image=selected_short.img)
	Outfit_short.configure(state="active")


def swap(frame1, frame2):
	frame1.grid_remove()
	frame2.grid(row=0, column=0)
	frame2.tkraise()
	frame2.focus_set()

	
def goback(event):				
	"""return to mainframe without deleting outfit as in outfit_remove()"""
	
	#leave out f_matches, to not have a selected shirt while selected short is None or vice versa
	f_shirts.grid_remove()
	f_shorts.grid_remove()
	f_seclayer.grid_remove()
	f_shoes.grid_remove()
	
	#destroy all opened canvas
	try:
		canvas_seclayer.destroy()
	except:
		pass
	
	try:
		canvas_shirts.destroy()
	except:
		pass
	
	try:
		canvas_shorts.destroy()
	except:
		pass
	
	f.grid(row=0, column=0)
	f.focus_set()
root.bind("<BackSpace>",goback)


def change_short(i):
	"""given a selected shirt we want to change the selected short to the next (if i=1) or previous (if i=-1) matching short"""

	global counter_S
	global selected_short
	
	if selected_shirt!=None:	
		n = len(selected_shirt.match)
		#counter_S gives the position of the current short regarding the list of possible matching shorts for the selected shirt
		counter_S = selected_shirt.match.index(selected_short)
		counter_S = (counter_S+i)%n
		
		#maybe second layer or shoes are selected, so the new shorts have to match them too
		while not (selected_shirt.match[counter_S] in selected_layer.match_short and selected_shirt.match[counter_S] in selected_shoe.match_short):
			counter_S = (counter_S+i)%n
		
		#update selected short
		selected_short = selected_shirt.match[counter_S]
		Outfit_short.configure(image=selected_short.img)


def change_shirt(i):
	"""analog to change_short(i)"""

	global counter_T
	global selected_shirt
	
	if selected_short!=None:
		n = len(selected_short.match)
		counter_T = selected_short.match.index(selected_shirt)
		counter_T = (counter_T+i)%n
		
		while not selected_short.match[counter_T] in selected_layer.match_shirt and selected_short.match[counter_T] in selected_shoe.match_shirt:
			counter_T = (counter_T+i)%n

		selected_shirt = selected_short.match[counter_T]
		Outfit_shirt.configure(image=selected_shirt.img)
		
f.bind("<Right>",lambda e: change_shirt(1))
f.bind("<Left>",lambda e: change_shirt(-1))
f.bind("<Up>",lambda e: change_short(1))
f.bind("<Down>",lambda e: change_short(-1))


def open_matches_shirts(frame,obj):
	"""if a short is clicked, there shall open a list of matching shirts"""

	global selected_short
	global canvas_matches
	global options
	
	try:							#if opened directly from MainFrame by the Outfit-Button
		canvas_shorts.destroy()
	except:
		pass
	
	swap(frame,f_matches)
	
	#by clicking the short it got selected
	selected_short = obj
	update_short()

	#create canvas to display all shirt-options
	canvas_matches = Canvas(f_matches, highlightthickness=0, width=root.maxsize()[0], height=root.maxsize()[1])
	create_canvas(canvas_matches,f_matches)
	
	#every shirt-option is a button
	counter = 0
	category = 1
	r = 0
	options = []

	for m in obj.match:					#look at matching tshirts
		if m in selected_layer.match_shirt:		#check if they match with the second layer
			if m in selected_shoe.match_shirt:	#check if they match with the shoes
				options.append(m)
				if m.category!=category:
					category = 2
					r = (counter-1)//5+1		#row of the element before, add 1 because of Zeilenumbruch
					counter = 0				#reset column
				button = Button(f_matches, image=m.img, borderwidth=0, command=lambda m=m:close_matches(m))
				canvas_matches.create_window(50+(counter%5)*300, 100+(r+counter//5)*410, anchor="nw", window=button)
				counter += 1
	#create an additional empty row so that everything gets displayed properly
	canvas_matches.create_window(0, 100+(r+1+(counter-1)//5)*410, anchor="nw")

		
def open_matches_shorts(frame,obj):
	"""basically the same as open_matches_shirts, only this time a shirt was clicked, so a short has to be selected"""

	global selected_shirt
	global canvas_matches
	global options
	
	try:									#if opened directly from MainFrame by the Outfit-Button
		canvas_shirts.destroy()
	except:
		pass
	
	swap(frame,f_matches)

	selected_shirt = obj
	update_shirt()
	
	canvas_matches = Canvas(f_matches, highlightthickness=0, width=root.maxsize()[0], height=root.maxsize()[1])
	create_canvas(canvas_matches,f_matches)
	
	#shorts and pants have different length, so the row-distance has to be updated when the category changes
	counter = 0
	category = 1
	row_dis = 351								#row-distance for shorts
	r = 0
	options = []

	for m in obj.match:						#look at matching shorts
		if m in selected_layer.match_short:		#check if they match with the second layer
			if m in selected_shoe.match_short:		#check if they match with the shoes
				options.append(m)
				if m.category!=category:
					category = 2
					r = (counter-1)//6+1		#row of the element before, add 1 because of Zeilenumbruch
					row_dis = 502				#row-distance for pants
					counter = 0				#reset column
				#shorts have two images, here we call the original-size image
				if m.category==1:
					button = Button(f_matches, image=m.img1, borderwidth=0, command=lambda m=m:close_matches(m))
				else:
					button = Button(f_matches, image=m.img, borderwidth=0, command=lambda m=m:close_matches(m))
				canvas_matches.create_window(45+(counter%6)*250, 40+r*351+(counter//6)*row_dis, anchor="nw", window=button)
				counter += 1
	canvas_matches.create_window(0, 30+r*351+(1+(counter-1)//6)*502, anchor="nw")

	
def close_matches(obj):
	"""when a matching shirt or short got selected, we have to update and return to mainframe"""

	global selected_shirt
	global selected_short
	
	if obj in shirts:
		selected_shirt = obj
		update_shirt()
	else:
		selected_short = obj
		update_short()
	
	canvas_matches.destroy()
	swap(f_matches,f)


def open_second_layer():
	"""display all second layers that match the selected outfit"""
	
	global canvas_seclayer
	global options
	
	swap(f,f_seclayer)
	
	#create scrollable canvas to display second layer-options
	canvas_seclayer = Canvas(f_seclayer, highlightthickness=0, width=root.maxsize()[0], height=root.maxsize()[1])
	create_canvas(canvas_seclayer,f_seclayer)
	
	counter = 0
	options = []

	for sec in second_layers:
		#if no outfit is selected, all second layers get displayed
		if (selected_shirt,selected_short) in sec.match or selected_shirt==None:
			if selected_shoe in sec.match_shoe or selected_shoe==placeholder_shoe:
				options.append(sec)
				button = Button(f_seclayer, image=sec.img, borderwidth=0, command=lambda sec=sec:close_second_layer(sec))
				canvas_seclayer.create_window(50+(counter%5)*300, 100+(counter//5)*410, anchor="nw", window=button)
				counter += 1
	canvas_seclayer.create_window(0, 100+(1+(counter-1)//5)*410, anchor="nw")


def close_second_layer(sec):
	
	global selected_layer
	
	canvas_seclayer.destroy()
	swap(f_seclayer,f)
	
	#update selected second layer
	selected_layer = sec
	Outfit_seclay.grid(row=0, column=2, rowspan=3, padx=(90,203), pady=(0,35))
	Outfit_seclay.configure(image=selected_layer.img_half)

	#change button to remove-second-layer-button
	Button_open_seclay.grid_remove()
	Button_remove_seclay.grid(row=2, column=4, padx=20, pady=0, rowspan=1)

	
def remove_second_layer():
	"""remove the optional second layer"""

	global selected_layer
	
	#remove second layer
	Outfit_seclay.grid_remove()
	selected_layer = placeholder_layer
	
	#change back the buttons
	Button_remove_seclay.grid_remove()
	Button_open_seclay.grid(row=2, column=4, padx=20, pady=0, rowspan=1)


def open_shoes():
	"""all shoe-functions are analog to the second-layer functions"""

	global options
	
	swap(f,f_shoes)
	
	counter = 0
	options = []
	matching_shoes = []

	for shoe in shoes:
		if (selected_shirt,selected_short) in shoe.match or selected_short==None:
			if shoe in selected_layer.match_shoe:
				options.append(shoe)
				matching_shoes.append(Button(f_shoes, image=shoe.img1, borderwidth=0, command=lambda shoe=shoe:close_shoes(shoe, matching_shoes)))
				matching_shoes[-1].grid(row=counter//5, column=counter%5, padx=(85,0), pady=100) 
				counter += 1


def close_shoes(shoe,matching_shoes):
	
	global selected_shoe
	
	for m in matching_shoes:
		m.destroy()
	
	swap(f_shoes,f)
	
	selected_shoe = shoe
	Outfit_shoe.grid(row=5, column=2, rowspan=2, padx=(223,203), pady=(70,0))
	Outfit_shoe.configure(image=selected_shoe.img)

	Button_open_shoes.grid_remove()
	Button_remove_shoes.grid(row=4, column=4, padx=20, pady=0, rowspan=1)
	

def remove_shoe():
	
	global selected_shoe
	
	Outfit_shoe.grid_remove()
	selected_shoe = placeholder_shoe
	
	Button_remove_shoes.grid_remove()
	Button_open_shoes.grid(row=4, column=4, padx=20, pady=0, rowspan=1)

def see_shirts():
	"""display all (matching) shirts on f_shirts"""

	global canvas_shirts
	
	swap(f,f_shirts)
	
	canvas_shirts = Canvas(f_shirts, highlightthickness=0, width=root.maxsize()[0], height=root.maxsize()[1])
	create_canvas(canvas_shirts,f_shirts)
	
	create_shirts_buttons(5)


def see_shorts():
	"""display all (matching) shorts on f_shorts"""

	global canvas_shorts
	
	swap(f,f_shorts)
	
	canvas_shorts = Canvas(f_shorts, highlightthickness=0, width=root.maxsize()[0], height=root.maxsize()[1])
	create_canvas(canvas_shorts,f_shorts)
	
	create_shorts_buttons(6)


def create_shirts_buttons(n):
	"""creation of the shirt-option-buttons when opening the frame of all shirts. n is number of columns"""

	global options

	counter = 0
	category = 1
	r = 0
	options = []

	for t in shirts:
		if t in selected_layer.match_shirt and t in selected_shoe.match_shirt:
			options.append(t)
			if t.category!=category:
				category = 2
				r = (counter-1)//n+1		#row of the element before + 1 for Zeilenumbruch
				counter = 0				#reset column
			button = Button(root, image=t.img, borderwidth=0, command=lambda t=t:open_matches_shorts(f_shirts,t))
			canvas_shirts.create_window(50+(counter%n)*300, 100+(r+counter//n)*410, anchor="nw", window=button)
			counter += 1
	canvas_shirts.create_window(0, 100+(r+1+(counter-1)//n)*410, anchor="nw")


def create_shorts_buttons(n):
	"""analog to create_shirts_buttons()"""
	
	global options

	counter = 0
	category = 1
	r = 0
	row_dis = 351				#row-distance for shorts
	options = []

	for s in shorts:
		if s in selected_layer.match_short and s in selected_shoe.match_short:
			options.append(s)
			if s.category!=category:
				category = 2
				r = (counter-1)//n+1		#row of the element before + 1 for Zeilenumbruch
				row_dis = 502				#row-distance for pants
				counter = 0				#reset column
			if s.category==1:
				button = Button(root, image=s.img1, borderwidth=0, command=lambda s=s:open_matches_shirts(f_shorts,s))
			else:
				button = Button(root, image=s.img, borderwidth=0, command=lambda s=s:open_matches_shirts(f_shorts,s))
			canvas_shorts.create_window(45+(counter%n)*250, 40+r*351+(counter//n)*row_dis, anchor="nw", window=button)
			counter += 1
	canvas_shorts.create_window(0, 30+r*351+(1+(counter-1)//n)*502, anchor="nw")


def choose_random_option(frame):
	"""pick a random object of the displayed options"""

	global options

	print("jooo")
	print (options)
	obj = random.choice(options)

	if frame == f_shirts:
		open_matches_shorts(f_shirts,obj)
	
	elif frame == f_shorts:
		open_matches_shirts(f_shorts,s)
	
	elif frame == f_matches:
		close_matches(obj)
	
	elif frame == f_seclayer:
		close_second_layer(obj)
	
	elif frame == f_shoes:
	
		matching_shoes = []
		for shoe in options:
			matching_shoes.append(Button(f_shoes, image=shoe.img1, borderwidth=0, command=lambda shoe=shoe:close_shoes(shoe, matching_shoes)))
		close_shoes(obj,matching_shoes)
f_shoes.bind("<Return>",lambda e: choose_random_option(f_shoes))							#the other frames are already binded by their canvas


#buttons
Button_random = Button(f, image=random_img, text="Choose Random Outfit", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=lambda: choose_randomly())
Button_shirts = Button(f, image=tshirt_img, text="See Tops", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=see_shirts)
Button_shorts = Button(f, image=pants_img, text="See Bottoms", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=see_shorts)

Button_open_seclay = Button(f, image=layer_img, text="Add Second Layer", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=lambda: open_second_layer())
Button_remove_seclay = Button(f, image=layer_remove_img, text="Remove Second Layer", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=lambda: remove_second_layer())

Button_open_shoes = Button(f, image=sneaker_img, text="Add Shoes", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=lambda: open_shoes())
Button_remove_shoes = Button(f, image=sneaker_remove_img, text="Remove Shoes", font=("System", 1, "bold"), fg="white", bg="black", width=380, height=90, command=lambda: remove_shoe())

Banner = Button(f, bg="#3a3b3d", width=35, height=58, state="disabled")
Outfit_shirt = Button(f, bg="#3a3b3d", activebackground="#3a3b3d", borderwidth=0, state="disabled", command=lambda: open_matches_shirts(f,selected_short))
Outfit_short = Button(f, bg="#3a3b3d", activebackground="#3a3b3d", borderwidth=0, state="disabled", command=lambda: open_matches_shorts(f,selected_shirt))
Outfit_seclay = Button(f, bg="#3a3b3d", activebackground="#3a3b3d", borderwidth=0, command=lambda: open_second_layer())
Outfit_shoe = Button(f, bg="#3a3b3d", activebackground="#3a3b3d", borderwidth=0, command=lambda: open_shoes())

#positions
Button_random.grid(row=1, column=0, padx=20, pady=(0,0), rowspan=1)
Button_shirts.grid(row=3, column=0, padx=20, pady=(0,0), rowspan=1)
Button_shorts.grid(row=5, column=0, padx=20, pady=(0,30), rowspan=1)

Button_open_seclay.grid(row=2, column=4, padx=20, pady=0, rowspan=1)
Button_open_shoes.grid(row=4, column=4, padx=20, pady=0, rowspan=1)

Banner.grid(row=0, column=2, rowspan=7, padx=(223,203), pady=(0,0))
Outfit_shirt.grid(row=0, column=2, rowspan=3, padx=(223,203), pady=(0,35))
Outfit_short.grid(row=2, column=2, rowspan=5, padx=(223,203), pady=(0,30))	


#update backgroundsong, then the entire root
while True:
	if pygame.mixer.music.get_busy() == 0:
		if len(playlist)>0:
			pygame.mixer.music.load("sound/" + playlist.pop())
			pygame.mixer.music.play()

	try:
		root.update()
	except:								#break loop if programm is closed
		break