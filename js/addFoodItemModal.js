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
    function editModal1(){
        // Get modal element
                var modal = document.getElementById('editModal');
                // Get open modal button
                var modalBtn = document.getElementById('edit1');

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
    function editModal2(){
        // Get modal element
                var modal = document.getElementById('editModal');
                // Get open modal button
                var modalBtn = document.getElementById('edit2');

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
            
