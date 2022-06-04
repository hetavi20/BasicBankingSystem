console.log("hello")

function checkAmount() {
    var myField = document.getElementById("amount")
    var message = document.getElementById("message")
    var reg = /^\d{0,4}(\.\d{0,2})?$/;
    if (!reg.test(myField.value)) {
        // message.innerHTML = "not"
        alert("Please Enter a Valid Amount!");
    }
}