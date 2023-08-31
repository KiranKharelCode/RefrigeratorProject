const button = document.getElementById("add_button");
button.addEventListener('click',function(){
     event.preventDefault()

    console.log("CLICKED");
    const food_input = document.createElement("input");
    food_input.setAttribute("name","food_input");
    food_input.setAttribute('placeholder',"food")

    const quantity_input = document.createElement("input");
    quantity_input.setAttribute("name","quantity_input");
    quantity_input.setAttribute('placeholder',"quantity")

    quantity_input.style.width = "50px";
    quantity_input.style.margin = "0px 0px 0px 5px";
    food_input.style.margin = "5px 0px 0px 0px";



    const element = document.getElementById("items_div");
    element.appendChild(food_input);
    element.appendChild(quantity_input);


});