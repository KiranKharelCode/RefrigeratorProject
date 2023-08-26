const button = document.getElementById("ADD_BUTTON");
button.addEventListener('click',function(){

    console.log("CLICKED");
    const para = document.createElement("p");
    const node = document.createTextNode("This is new.");
    para.appendChild(node);
    const element = document.getElementById("first_div");
    element.appendChild(para);


});