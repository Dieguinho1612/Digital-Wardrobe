"""Create the data of clothes. For this, the information is give by the name of the image of every clothing-piece.
The letters define the class: T for T-Shirts, S for Shorts (and Pants), sec for Second Layers (such as Shirts) and shoe for Shoes.
The first number is for the numeration and the second one is for the class. 
"1" stands for Good T-Shirts as well as for Shorts, "2" for Mediocre T-Shirts as well as for Pants.
In the case of Shorts, there are always two images, one the length of a pants image, the second one the original length, which is indicated with "_" at the end.
Second Layers also have a second image, showing only the left half of the shirt. This one is indicated with "_half" at the end.
Every image end with ".png". All important examples, where the numeration number is choosen as 7:
"T7_1.png" -> Good T-Shirt;
"T7_2.png" -> Mediocre T-Shirt; 
"S7_1.png" -> Short with long image; 
"S7_1_.png" -> Short with original image-size;
"S7_2.png" -> pants; 
"sec7.png" -> second layer(shirt or jacket); 
"sec7_half.png" -> left half of the second layer; 
"shoe7.png" -> a shoe."""

#the integers of the i-th list stand for the shorts matching the i-th shirt
list_of_shirt_matches=[	#0=blaue S, 1=dunkelblaue S, 2=schwarze S, 3=rote S, 4=zweifarbige S, 5=jeans H, 6=dunkelblaue H, 7=schwarze H, 8=grüne H
[0,1,2,4,5,6,7,8],		#0
[0,1,2,3,5,6,7,8],		#1
[0,1,2,3,4,5,7,8],		#2
[1,7],					#12
[1,2,4,5,6,7],			#13		
[0,2,5,6,7],			#14		
[0,1,2,3,4,5,6,7,8],	#15	
[0,1,2,4,5,7],			#3	
[0,1,2,3,5,6,7,8],		#4
[0,1,2,5],				#16
[0,1,2,5,6,7],			#17	
[0,1,2,3,4,5,7,8],		#5	
[0,1,3,5,7,8],			#6			
[0,1,3,4,5,7,8],		#7
[0,1,2,4,5,6,7,8],		#8
[0,3,5,7],				#18
[0,1,2,4,5,6,7,8],		#9
[0,1,6],				#19
[0,1,5,6,7,8],			#10
[0,1,5,6,7,8]]			#11


#sort list such that items of category come first in random order, then items of category 2
def categorize_list(liste):
	
	L1 = []
	L2 = []
	for a in liste:
		if a.category==1:
			L1.append(a)
		else:
			L2.append(a)
	random.shuffle(L1)
	random.shuffle(L2)
	liste[:] = L1+L2


#create shorts with empty matches, later update their matches using the shirts
shorts = []
for i in range(999):
	try:
		shorts.append(Shorts(i,[]))
	except FileNotFoundError:
		break


def read_in_shirts():
	"""quick method to create t-shirts, this way only "list_of_shirt_matches" has to be updated manually"""

	global shirts
	global list_of_shirt_matches
	
	counter = 0
	n = len(list_of_shirt_matches)
	
	for i in range(n):								#iterate over all t-shirts
		short_matches = []
		for j in list_of_shirt_matches[counter]:
			short_matches.append(shorts[j])			#erstellt Liste der Form [shorts[0].shorts[2],shorts[7]]
		categorize_list(short_matches)
		shirts.append(T_Shirts(counter, short_matches))
		counter += 1


#create t-shirts
shirts = []
read_in_shirts()

#update shorts-matching using the matching lists of the t-shirts
for s in shorts:
	for t in shirts:
		if s in t.match:
			s.match.append(t)
	categorize_list(s.match)


#create shoes the same way t-shirts were created. The first list in every tuple stands for the t-shirt-matches, the second one for the short-matches.
list_of_shoe_matches=[
([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19],[0,1,3,4]), 				#blau
([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[0,1,2,3,4,5,7,8]),	#grau
([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,17,18],[0,1,2,3,5,6,7,8]),			#weiß
([0,1,2,6,7,8,9,10,11,12,13,14,15,16,17,18],[0,1,2,3,5,6,7,8]),				#rot
([0,1,2,4,5,6,7,8,9,10,11,13,14,16,17,18,19],[0,1,2,5,6,7,8]),				#beige
([0,1,2,4,6,7,9,10,11,12,13,14,15,18],[2,3,5,7]),							#laufschuhe
([0,1,2,6,7,8,9,10,11,14,15,16,18,19],[5,6,7,8]),							#helle chelseaboots
([0,1,2,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19],[5,6,7,8])]					#dunkle chelseaboots


def read_in_shoes():

	global shoes
	global list_of_shoe_matches

	counter = 0
	n = len(list_of_shoe_matches)
	
	for i in range(n):								#iterate over all t-shirts
		shirt_matches = []
		short_matches = []
		for j in list_of_shoe_matches[counter][0]:
			shirt_matches.append(shirts[j])			#erstellt Liste der Form [shirts[0].shirts[2],shirts[7]]
		for j in list_of_shoe_matches[counter][1]:
			short_matches.append(shorts[j])			#erstellt Liste der Form [shorts[0].shorts[2],shorts[7]]
		categorize_list(shirt_matches)
		categorize_list(short_matches)
		shoes.append(Shoes(counter, shirt_matches, short_matches))
		counter += 1


shoes = []
read_in_shoes()


#create second layers the same way. The third list in every tuple stands for the shoe-matches
list_of_seclayer_matches=[
([1,5,7,9,10,11],[0,2,5,6,7,8],[0,1,2,3,4,6,7]),		#braunes Hemd
([0,1,4,7,9,10,11],[0,1,5,6,7,8],[0,1,4,6,7]),			#buntes Hemd
([0,1,4,7,9,10,11],[1,2,3,4,5,6,7,8],[0,1,2,3,4,6,7]),	#dunkelblaues Hemd
([1,11,17],[1,2,6,7],[0,1,2,6,7]),						#hellbalues hemd
([0,1,11,14],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7])		#grünes Hemd
]


def read_in_seclayer():

	global second_layers
	global list_of_seclayer_matches

	counter = 0
	n = len(list_of_seclayer_matches)
	
	for i in range(n):								#iterate over all t-shirts
		shirt_matches = []
		short_matches = []
		shoe_matches = []
		for j in list_of_seclayer_matches[counter][0]:
			shirt_matches.append(shirts[j])			#erstellt Liste der Form [shirts[0].shirts[2],shirts[7]]
		for j in list_of_seclayer_matches[counter][1]:
			short_matches.append(shorts[j])			#erstellt Liste der Form [shorts[0].shorts[2],shorts[7]]
		for j in list_of_seclayer_matches[counter][2]:
			shoe_matches.append(shoes[j])			#erstellt Liste der Form [shoes[0].shoes[2],shoes[7]]
		categorize_list(shirt_matches)
		categorize_list(short_matches)
		second_layers.append(Second_Layer(counter, shirt_matches, short_matches, shoe_matches))
		counter += 1


second_layers = []
read_in_seclayer()

random.shuffle(shoes)
random.shuffle(second_layers)

#order the shirts and shorts list by category and randomly inside each category
categorize_list(shirts)
categorize_list(shorts)