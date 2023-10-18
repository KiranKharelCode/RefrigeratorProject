const search = () =>{
    const searchbox = document.getElementById("food-search").value.toUpperCase();
    const food_list = document.getElementById("food-list")
    const product = document.querySelectorAll(".products")
    const product_table_name = food_list.querySelectorAll("#table-name")

    for (var i=0; i < product_table_name.length; i++){
        let match = product[i].querySelectorAll('#table-name')[0]

        if (match){
            let textvalue = match.textContent || match.innerHTML

            if(textvalue.toUpperCase().indexOf(searchbox) > -1){

                product[i].style.display = "";


            }else{
                product[i].style.display = "none";



            }

        }

    }


}