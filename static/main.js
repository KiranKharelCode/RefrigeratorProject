const button = document.getElementById("ADD_BUTTON");
button.addEventListener('click',function(){

    console.log("CLICKED");
    const para = document.createElement("input");
    para.setAttribute("name","INPUT2")

    const element = document.getElementById("first_div");
    element.appendChild(para);


});