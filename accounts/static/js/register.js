const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const root_div = document.querySelector(".root_div");

sign_up_btn.addEventListener("click", () => {
  root_div.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  root_div.classList.remove("sign-up-mode");
  console.log("clicked")
});


(function () {
  'use strict'

  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

function message_loder(){
  var x = document.getElementById('alert') == null
  if (x == false){
    document.getElementById('sign-up-btn').click();
  }
  
}

window.onload = message_loder;