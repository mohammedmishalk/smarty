function choices(ch){
    if (ch==='U'){
        location.href=1;
    }else if(ch==='E'){
        location.href="2";
    }
    else if(ch==='P'){
        location.href=3;
    }else if(ch==='D'){
        location.href=4;
    }else{
        alert("something wrong.refresh page to load")
    }
}

window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");

var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}