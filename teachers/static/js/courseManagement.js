function choices(ch){
    if (ch==='U'){
        location.href="U";
    }else if(ch==='E'){
        location.href="E";
    }
    else if(ch==='P'){
        location.href="P";
    }else if(ch==='D'){
        location.href="D";
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