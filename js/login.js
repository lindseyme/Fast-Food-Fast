function swap(referTo){//referTo refers to the current div where this function is defined
                    if(referTo.getAttribute("data-tab")=="login"){
                        document.getElementById("form-body").classList.remove("active");
                        referTo.parentNode.classList.remove("signup");//removes/hides the signup form
                    }
                    else{
                        document.getElementById("form-body").classList.add("active");
                        referTo.parentNode.classList.add("signup");//adds the signup form
                    }
                }

function loginUser(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    const data = {"email":email, "password":password};


    fetch('https://fast-food-fast-api-ch3.herokuapp.com/auth/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        cache: 'no-cache',
        body: JSON.stringify(data)
    })
        .then((res) => res.json())
        .then(result => {
            if(result.status === 'success'){
                if(email == "admin@admin.com"){
                    localStorage.setItem("auth-token",result.auth_token);
                    window.location.href = 'manageFastFood.html';
                }
                else{
                    localStorage.setItem("auth-token",result.auth_token);
                    window.location.href = 'makeOrder.html';
                }
            }
            else{

            }
            
        })
        
}

function RegisterUser(){
    var email = document.getElementById('r_email').value;
    var password = document.getElementById('r_password').value;
    const data = {"email":email, "password":password};

    fetch('https://fast-food-fast-api-ch3.herokuapp.com/auth/signup', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
       
        cache: 'no-cache',
        body: JSON.stringify(data)
    })
        .then((res) => res.json())
        .then(result => {
            if(result.status === 'success'){
               alert(result.message)
            }
            else{
                alert(result.message)
            }
            
        })
        
}
