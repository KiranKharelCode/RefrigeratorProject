# RefrigeratorProject
 A project to help me keep track of the items in my fridge

The problem:
I waste alot of food, because I forget it's in my fridge. Or I forget to use it all
after using it for 1 or 2 recipes. In order to save me money in the future and to 
limit my waste, I have coded this simple program to keep track of my food. 
With the help of Twillio API and an AI API, I can get all the data of my 
refrigerator. 
Data like; how many of an item I have, when I had bought it, how long it's been on my fridge,
and the data on how long that item can be stored in the fridge. 

UPDATE 08/21/23 12:00 AM:
DUE TO RESTRICTIONS AND NEW LAW REGUALTIONS I CANNOT USE TWILLIO ANYMORE, THEREFORE IM CURRENTLY LOOKING FOR 
A NEW APPROACH TO MY PROJECT

UPDATE 08/21/23 1:00AM:
ENDED UP FIGURING OUT HOW TO MAKE TWILLIO WORK, SO PROJECT IS BACK ON TRACK. 

UPDATE 08/23/23 11:00PM:
I NEED TO LEARN JAVASCRIPT FOR ME TO IMPLIMENT THE UI INTERFACE I WANT TO HAVE, WHERE THE USER CAN HIT 
"ADD ITEM" AND A NEW FIELD WILL APPEAR FOR THEM TO ENTER DATA. 

UPDATE 08/24/23 10:00PM:
I LEARNED THE BASIS OF JS, AND WITH THIS SIMPLE CODE I CAN NOW ADD NEW ITEMS INTO MY PROGRAM

"

   const button = document.getElementById("ADD_BUTTON");
   button.addEventListener('click',function(){
   console.log("CLICKED");
   const para = document.createElement("p");
   const node = document.createTextNode("This is new.");
   para.appendChild(node);
   const element = document.getElementById("first_div");
   element.appendChild(para);


});"
