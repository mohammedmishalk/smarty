const cercle01 = document.getElementById('cs');
const cercle02 = document.getElementById('cs1');
const cercle03 = document.getElementById('cs2');
const formDiv = document.getElementById('row1');
const formDiv1 = document.getElementById('row2');
const formDiv2 = document.getElementById('row3');
const lineDiv = document.getElementById('line');
const lineDiv01 = document.getElementById('line2');
const lineDiv02 = document.getElementById('line3');

$(document).on('submit', '#form01', (e) => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "addcourse",
        data: {
            name: $('#cname').val(),
            time: $('#time').val(),
            dr: $('#dr').val(),
            dis: $('#discriptions').val(),
            skils: $('#values').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: () => {
            cercle01.classList.add("bg-success");
            formDiv.classList.add('hidden');
            document.getElementById('headder').classList.add("text-success")
            setTimeout(() => next_form(), 1000)

            function next_form() {
                formDiv1.classList.remove('hide')
                lineDiv01.classList.add('line')
                cercle02.classList.remove('bg-secondary')
                cercle02.classList.add('cs-bg')
            }
        },
        error: () => {
            alert("Somthing went wrong");
        },
    });

})
$(document).on('submit', '#form02', (e) => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "addcourse",
        data: {
            password: $('#password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: () => {
            
            cercle02.classList.add("bg-success");
            formDiv1.classList.add('hidden');
            document.getElementById('headder1').classList.remove("text-muted")
            document.getElementById('headder1').classList.add("text-success")
            setTimeout(() => next_form(), 1000)
            function next_form() {
                formDiv2.classList.remove('hide')
                lineDiv02.classList.add('line')
                cercle03.classList.remove('bg-secondary')
                cercle03.classList.add('cs-bg')
                document.getElementById("formFile01").disabled = false
                document.getElementById("formFile02").disabled = false;
            }
        },
        error: () => {
            alert("Somthing went wrong");
        },
    });
})

$(document).on('submit', '#form03', (e) => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "addcourse",
        data: {
            name: $('#cname').val(),
            time: $('#time').val(),
            dr: $('#dr').val(),
            dis: $('#discriptions').val(),
            skils: $('#values').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: () => {
            cercle03.classList.add("bg-success");
            formDiv1.classList.add('hidden');
            document.getElementById('headder1').classList.remove("text-muted")
            document.getElementById('headder1').classList.add("text-success")
        }
    });
})

function skilChange(){
    var b =document.getElementById('skils')
    var a=document.getElementById('values').value
    document.getElementById('values').value=a+b.value+",";
    b.value="";
    
}