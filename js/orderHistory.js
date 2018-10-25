var history_url=SERVER_PATH+"users/orders";
fetch(history_url, {
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
            // alert(JSON.stringify(result));
            var orders = '<table border="1" id="orderHistory">'+
                                 '<tr><th>#</th><th>Order Id</th><th>Item Name</th><th>Quantity</th><th>Price</th><th>Order Status</th><th>Placed At</th></tr>';
            if(result.message != "No order history"){
                var i = 0;
                // alert(JSON.stringify(result.message.length))
                for(i=0; i < result.message.length; i++){
                    orders +=  '<tr><td>'+String(i+1)+'</td><td>'+result.message[i]["order_id"]+'</td><td>'+result.message[i]["item_name"]+'<td>'+result.message[i]["quantity"]+'</td><td>'+result.message[i]["price"]+'</td><td>'+result.message[i]["order_status"]+'</td><td>'+result.message[i]["created_at"]+'</td></tr>';
                }
                document.getElementById("orderTable").innerHTML = orders+"</table>";
                
            }
            else{
                orders += "<tr ><td colspan='6'><center>"+result.message+"</center><td><tr></tr>";
                // alert(orders)
                document.getElementById("orderTable").innerHTML = orders+"</table>";
            }
         

        }
        else{
            alert(result.status);
        }
        
    })