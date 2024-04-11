
  


    document.addEventListener("DOMContentLoaded", function () {
        id="";
        var editLinks = document.querySelectorAll('.editLink');
        editLinks.forEach(function (link) {
            link.addEventListener('click', function (event) {
                event.preventDefault();
                var empId = this.getAttribute('data-emp-id');
                

                $.ajax({
                    type: 'GET',
                    url: '/update/' + empId,
                    
                    success: function(response) {
                        
                        console.log(response.emp.des);
                        id=response.emp.id;
                        $('#updateemp').modal('show');
                        document.getElementById('vname').value = response.emp.name;
        document.getElementById('vage').value =response.emp.age;
        document.getElementById('vgender').value = response.emp.gender;
        document.getElementById('vdesignation').value =response.emp.des;
        document.getElementById('updateform').action = '/upd/' + response.emp.id;
                    },
                    error: function(xhr, status, error) {
                      
                        console.error(xhr.responseText);
                    }
                });



            });
        });
          document.getElementById('submitButton').addEventListener('click', function (event) {
        // Prevent the default form submission behavior
        event.preventDefault();
        console.log("form in ");

        document.getElementById('updateform').action = '/update/' + id;

        document.getElementById('updateform').submit();
    });
    });