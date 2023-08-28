const button = document.getElementById("ADD_BUTTON");
button.addEventListener('click',function(){

    console.log("CLICKED");
    const food_input = document.createElement("input");
    food_input.setAttribute("name","food_input")

    const quantity = document.createElement("input");
    quantity.setAttribute("name","quantity")

    const element = document.getElementById("first_div");
    element.appendChild(food_input);
    element.appendChild(quantity);


});