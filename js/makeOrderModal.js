function order(item_name,price,image){
                    // Get modal element
                var modal = document.getElementById('simpleModal');
                // Get open modal button
                
                var modalBtn = document.getElementById(item_name);
                document.getElementById('item_name').value = item_name;
                document.getElementById('header_name').innerHTML = item_name;
                document.getElementById('price').innerHTML = price;
                document.getElementById('part1').innerHTML = '<img src='+image+' width="350px" height="300px"alt="FastFood"/>';
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
              function submitOrder(){
                var item_name = document.getElementById('item_name').value
                var quantity = document.getElementById('quantity').value
                // alert(item_name)
                // alert(quantity)
                const data = {"item_name":item_name, "quantity":quantity};

                  // alert( localStorage.getItem("auth-token"));
                  var orders_url=SERVER_PATH+"users/orders";
                  fetch(orders_url, {
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
                              alert(result.message); 
                              window.location.href="makeOrder.html";
                          }
                          else{
                              alert(result.message);
                          }
                          
                      })
                      
                  }