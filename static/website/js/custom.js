//Animation.
$(document).ready(function() {
    $(".telegram-popup").delay(300).show(0);
});

function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
(function() {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.async = true;
    script.src = "//telegram.im/widget-button/index.php?id=@IPTVIntel";
    document.getElementsByTagName("head")[0].appendChild(script);
})();

var password = document.getElementById("password"),
    confirm_password = document.getElementById("confirm_password");

function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;