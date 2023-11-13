const button = document.getElementById("add_button");

button.addEventListener('click',function(){
     event.preventDefault()

    console.log("CLICKED");
    const food_input = document.createElement("input");
    food_input.setAttribute("name","food_input");
    food_input.setAttribute('placeholder',"food")
    food_input.setAttribute("required", "");

    const quantity_input = document.createElement("input");
    quantity_input.setAttribute("name","quantity_input");
    quantity_input.setAttribute('placeholder',"quantity")
    quantity_input.setAttribute("required", "");

    const expire_input = document.createElement("input");
    expire_input.setAttribute("name","expire_input");
    expire_input.setAttribute('placeholder',"expire_date Y-M-D")
    expire_input.setAttribute("required", "");
    const line_break = document.createElement("hr")

    quantity_input.style.width = "50px";
    quantity_input.style.margin = "0px 0px 0px 5px";
    food_input.style.margin = "5px 0px 0px 0px";
    line_break.style.backgroundColor = '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6, '0');
    line_break.style.height = '2px';



    const element = document.getElementById("items_div");
    element.appendChild(food_input);
    element.appendChild(quantity_input);
    element.appendChild(expire_input);
    element.appendChild(line_break);


});