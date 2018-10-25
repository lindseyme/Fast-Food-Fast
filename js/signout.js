
function signOut(){
fetch('https://fast-food-fast-api-ch3.herokuapp.com/auth/signout', {
    method: 'POST',
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
            localStorage.clear();
            alert(result.message);
            window.location.href = 'index.html';
        }
        else{
            alert(result.message);
        }
        
    })
}