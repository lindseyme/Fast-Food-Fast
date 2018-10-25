var menu_url=SERVER_PATH+"menu";
fetch(menu_url, {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        "x-access-token": localStorage.getItem("auth-token")
    },
    cache: 'no-cache'
    
})
    .then((res) => res.json())
    .then(result => {
        if(result.status === 'success'){
            
            // alert(JSON.stringify(result.message))
            // alert(result.message.length);

            if(result.message != "Menu is empty!"){
                var i = 0;
                var menu = '';
                // alert(result.message.length)
                for(i = 0; i< result.message.length; i++){
                    var x = Math.floor((Math.random() * 9) + 1);
                    menu += '<div id="item"><img src="images/'+String(x)+'.jpg"><h3>'+result.message[i]["item_name"]+'</h3><p>Our price: '+result.message[i]["price"]+'</p><button type="button" id="'+result.message[i]["item_name"]+'" onclick='+'order("'+result.message[i]["item_name"]+'",'+result.message[i]["price"]+',"images/'+String(x)+'.jpg")>Order Now</button></div>';
                }
                document.getElementById("items-list").innerHTML = menu;
                
            }
            else{
                document.getElementById("items-list").innerHTML = "<font color='red'><b>Menu is empty, Please consult the caterer.</b></font>";
            }
         

        }
        else{
            alert(result.status);
        }
        
    })


   