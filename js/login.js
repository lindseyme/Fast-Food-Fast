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
function getCredentials(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    
        if(email == "admin@admin.com" && password=="admin1234"){
           window.location= "manageFastFood.html";
           alert(window.location);
        }
        else if(email == "user@user.com" && password=="user1234"){
            window.location= "menu.html";
           alert(window.location);
        }
        else{
        alert("Wrong credentials");
         }
    }
    
