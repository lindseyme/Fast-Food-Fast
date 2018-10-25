var menu_url = SERVER_PATH+"menu";
fetch(menu_url, {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        "x-access-token":  localStorage.getItem("auth-token")
    },
    cache: 'no-cache'
    
})
    .then((res) => res.json())
    .then(result => {
        if(result.status === 'success'){
            
            // alert(JSON.stringify(result.message))
            // alert(result.message.length);
            var food_items = '<h1>Menu</h1><table border="1" id="orderHistory">'+
                                 '<tr><th>#</th><th>Item</th><th>Price</th></tr>';
            if(result.message != "Menu is empty!"){
                var i = 0;
                for(i=0; i < result.message.length; i++){
                    food_items +=  '<tr><td>'+String(i+1)+'</td><td>'+result.message[i]["item_name"]+'</td><td>'+result.message[i]["price"]+'</td></tr>';
                }
                document.getElementById("menu").innerHTML = food_items+"</table>";
            //    +
            //     
            }
            else{
                document.getElementById("menu").innerHTML = food_items +"<tr><td colspan='3'><center><font color='red'><b>menu is empty, please click on 'add fast food' to add food items</font><b></center></td></tr></table";
            }
         

        }
        else{
            alert(result.status);
        }
        
    })



function addFoodItem(){
        // Get modal element
                var modal = document.getElementById('addFoodModal');
                // Get open modal button
                var modalBtn = document.getElementById('addFood');

                // Get close button
                var closeBtn = document.getElementsByClassName('closeBtn')[0];

                // Listen for open click
                modalBtn.addEventListener('click', openModal);
                // Listen for close click
                closeBtn.addEventListener('click', closeModal);
                // Listen for outside click
                window.addEventListener('click', outsideClick);

                // Function to open modal
                function openModal(){
                modal.style.display = 'block';
                }

                // Function to close modal
                function closeModal(){
                modal.style.display = 'none';
                }

                // Function to close modal if outside click
                function outsideClick(e){
                if(e.target == modal){
                    modal.style.display = 'none';
                }
                }
    }
    
        
    function add_item(){
    let item_name = document.getElementById('item_name').value;
    let price= document.getElementById('price').value;

    if (/\s/.test(item_name)) {
        alert("Food Item should not contain space");
    }else{
        const data = {"item_name":item_name.toLowerCase(), "price":price};
 
        // alert( localStorage.getItem("auth-token"));
        var menu_url = SERVER_PATH+"menu";
        fetch(menu_url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-type': 'application/json',
                "x-access-token":  localStorage.getItem("auth-token")
            },
            cache: 'no-cache',
            body: JSON.stringify(data)
        })
            .then((res) => res.json())
            .then(result => {
                if(result.status === 'success'){
                    // myCookie.setCookie('auth_token', result.auth_token, 2);
                    // window.location.href = 'index.html';
                    alert(result.message);
                    window.location.href = 'manageFastFood.html';
                    
                }
                else{
                    alert(result.message);
                }
                
            })
            
        }

    }
  
