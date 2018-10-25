var orders =SERVER_PATH+"orders/";
fetch(orders, {
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
            
            // alert(JSON.stringify(result.message[0]))
            // alert(result.message.length);
            // alert(JSON.stringify(result));
            if(result.message !="There are no orders yet"){
                var i = 0;
                
                var orders = '<table border="1" id="orderHistory">'+
                                 '<tr><th>#</th><th>Order Id</th><th>User Id</th><th>Item Id</th><th>Item Name</th><th>Quantity</th><th>Price</th><th>Order Status</th><th>Created At</th><th>Options</th></tr>';
                for(i=0; i < result.orders.length; i++){
                    orders +=  '<tr><td>'+String(i+1)+'</td><td>'+result.orders[i]["order_id"]+'</td><td>'+result.orders[i]["user_id"]+'<td>'+result.orders[i]["item_id"]+'</td><td>'+result.orders[i]["item_name"]+'</td><td>'+result.orders[i]["quantity"]+'</td><td>'+result.orders[i]["price"]+'</td><td>'+result.orders[i]["order_status"]+'</td><td>'+result.orders[i]["created_at"]+'</td><td><button onclick="update_order('+result.orders[i]["order_id"]+','+result.orders[i]["user_id"]+')" id="'+result.orders[i]["order_id"]+'">Update status</button></td></tr>';
                }
                document.getElementById("orderTable").innerHTML = orders+"</table>";
            //    +
            //     
            }
            else{
                document.getElementById("orderTable").innerHTML = "<tr colspan='3'><td><font color='red'><b>"+result.message+"<b></font><td><tr>";
            }
         

        }
        else{
            alert(result.status);
        }
        
    })


function update_order(order_id,user_id){
             
                // Get modal element
                var modal = document.getElementById('simpleModal');
                // Get open modal button
                var modalBtn = document.getElementById(order_id);
                document.getElementById('order_id').innerHTML = order_id;
                document.getElementById('user_id').innerHTML = user_id;
                document.getElementById('input_order_id').value = order_id;
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
        function saveChanges(){
            var order_id = document.getElementById('input_order_id').value;
            var order_status = document.getElementById('order_status').value;
            // alert(order_id)
            // alert(order_status)
            const data = {"order_status": order_status};

            var update_orders_url =SERVER_PATH+"orders/"+order_id;
            fetch(update_orders_url, {
            method: 'PUT',
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
                    
                    alert(result.message)
                    window.location.href="admin_viewOrder.html";

                }
                else{
                    alert(result.message)
                }
                
            })


        }

        function getSingleOrder(){
            var order_id = document.getElementById("single_id").value;
            // alert(order_id)
            var update_orders_url =SERVER_PATH+"orders/"+order_id;
            fetch(update_orders_url, {
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
                    // alert(JSON.stringify(result.item));
                    var header= '<table border="1" id="orderHistory">'+
                    '<tr><th>#</th><th>Order Id</th><th>User Id</th><th>Item Id</th><th>Item Name</th><th>Quantity</th><th>Price</th><th>Order Status</th><th>Created At</th><th>Options</th></tr>';
                    orders = header+'<tr><td>'+String(1)+'</td><td>'+result.item["order_id"]+'</td><td>'+result.item["user_id"]+'<td>'+result.item["item_id"]+'</td><td>'+result.item["item_name"]+'</td><td>'+result.item["quantity"]+'</td><td>'+result.item["price"]+'</td><td>'+result.item["order_status"]+'</td><td>'+result.item["created_at"]+'</td><td><button onclick="update_order('+result.item["order_id"]+','+result.item["user_id"]+')" id="'+result.item["order_id"]+'">Update status</button></td></tr></table>';
                        
                    document.getElementById("orderTable").innerHTML =orders;

                    } else {
                        alert(result.status);
                    }
            })

        }