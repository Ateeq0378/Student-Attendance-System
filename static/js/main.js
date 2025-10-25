var error = new Array();

function timeOut() {
    document.getElementById("alert-box").style.display = "none";
}

function validateForm(event) {

    var x = document.getElementById("type");
    var i = x.selectedIndex;
    var type = x.options[i].text;
    var gmail = document.getElementById("email").value;
    var password = document.getElementById("pwd").value;

    if (type == "Select Log In Type") {
        error = "Please Selecet Log In Type";
        document.getElementById("alert-box").innerHTML = error;
        document.getElementById("alert-box").style.display = "block";
        // setTimeout(timeOut, 3000);
        event.preventDefault();
    }

    else if (gmail == null || gmail == "") {
        error = "Please Enter Gmail Id";
        document.getElementById("alert-box").innerHTML = error;
        document.getElementById("alert-box").style.display = "block";
        // setTimeout(timeOut, 3000);
        event.preventDefault();
    }

    else if (password == null || password == "") {
        error = "Please Enter Password";
        document.getElementById("alert-box").innerHTML = error;
        document.getElementById("alert-box").style.display = "block";
        // setTimeout(timeOut, 3000);
        event.preventDefault();
    }
}


const table = document.getElementById("attendance");
const check = table.querySelectorAll("input[type=checkbox]");
Array.from(check).forEach((item) => {
    
    item.addEventListener("change", function () {
        const present = this.parentElement.parentElement.querySelector("input[id=p]");
        const absent = this.parentElement.parentElement.querySelector("input[id=a]");

        if (this.checked && this.id=="p") {
            absent.checked = false;
            present.checked = true;
        }
        else {
            absent.checked = true;
            present.checked = false;
        }
    })
})