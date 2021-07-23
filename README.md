# Digital-Wardrobe
<p>This is a graphical digital wardrobe created with Tkinter.<br>
It is possible to select outfits based on the clothes I actually do own in real life.<br>
The program will only mount matching outfits.<br>
This was meant as a tool to help me when I did not know what to wear.<br>
All fotos were taken and edited by me, as well as all the code was written by myself.</p>

<p>Starting the program is going to take the user to the main interface, where he can choose between 5 buttons while listening to some moody background music, randomly selected out of a created playlist. The selected outfit will later be displayed in the dark gray central stripe.<br>
The idea is that throughout the entire selection process there is no moment in which an outfit is displayed that does not completely match. It should also never be possible to choose an option for any part of the outfit that would not match with what have been selected so far.
</p>

![Screenshot0](https://user-images.githubusercontent.com/53007033/126713530-84b8373d-bb3f-40ce-b57c-6634ac3a1efc.jpg)

<p> The buttons have the following functions:

1. Select a random matching outfit. This can also be triggered by pressing the "Enter" key.
2. Show all options for T-Shirts. The T-Shirts are divided into two classes:<br> 
  The first class are the better ones, recommended for more special occassions.<br> 
  The second class are the ones rather recommended for less important events.<br>
  The first class will always be displayed first, while the order within the classes is random to avoid a selection bias.
3. Show all options for Pants and Shorts. The Shorts are displayed first, the Pants second, while the order within every type is always random.
4. Show all options for Shirts that match with the currently selected outfit in a random order. If nothing is selected yet, show all Shirts.<br>
  This Shirts are meant to be like a second layer and to be worn openly above the T-Shirt so that it can still be seen.
5. Show all options for Shoes that match with the currently selected outfit in a random order. If nothing is selected yet, show all Shoes.

One can use the "Backspace" key to return to the main interface and the "Delete" key to remove the selected outfit.<br>
Also pressing the "Escape" key is going to terminate the program.</p>
<br>

Using the random outfit button:

https://user-images.githubusercontent.com/53007033/126719631-721a4a9a-edbe-4f37-9ebd-c27eebd9e671.mp4

<br>
<br>
<p>Using the buttons for T-Shirts and Pants/Shorts:</p>

https://user-images.githubusercontent.com/53007033/126720237-205af54d-f4ac-41ca-87fd-98487e5efd2b.mp4

<br>
<br>
<p>Using the buttons for Shirts and Shoes:</p>

https://user-images.githubusercontent.com/53007033/126720282-47d2155a-78d6-402c-8651-a573ff2e6f23.mp4

<br>
<br>
<p> When the options for the T-Shirts are displayed, one can select one by clicking on it. 
  A window showing all the options of pants and shorts that match with this selected T-Shirt is going to open then.
  By clicking on one of these options the user can then also select the pants/shorts.
  One can also do it the other way around and first select Pants/Shorts and then one T-Shirt of the matching options. </p>
  
https://user-images.githubusercontent.com/53007033/126721337-5a9b00c8-8dc6-4e69-9d74-b5d279c8ca8c.mp4

<br>
<br>
<p> The user can then, if wanted, select a overlaying Shirt and Shoes matching with the outfit.
  Since this is not necessary (not every outfit does have a second layer and sometimes one wants to use an outfit inside ones house and there need no shoes), the user can deselect them again, clicking on the corresponding button that just turned red. </p>
  
https://user-images.githubusercontent.com/53007033/126721519-31b947fe-a82e-4906-a7dd-d6d0e959a2fc.mp4

<br>
<br>
<p> It is also possible to first select the Shirt and/or Shoes and afterwards a T-Shirt and Pants/Shorts that match with them. </p>

https://user-images.githubusercontent.com/53007033/126722189-1dc9391d-75fe-4213-9b96-cb20aa4ab9f9.mp4

<br>
<br>
<p> When an outfit is selected, one can click on any part of it to see all the other options of that type that would match and select them.
  It is also possible to use the "Left" key and the "Right" key to scroll directly through the matching options for T-Shirts.
  Using the "Up" key and "Down" key the same is possible for the matching options of pants/shorts. </p>
  
https://user-images.githubusercontent.com/53007033/126723335-fc7d60c3-1be2-46fe-b3b5-37debde2de52.mp4
