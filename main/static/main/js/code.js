
document.addEventListener("DOMContentLoaded", function() {
    let titulo = document.getElementById("titulo");
    let nombre = document.getElementById("nombre");
    let email = document.getElementById("email");
    let pass = document.getElementById("pass");
    let errorNombre = document.getElementById("error-nombre");
    let errorEmail = document.getElementById("error-email");
    let errorPass = document.getElementById("error-pass");
    let nombreField = document.getElementById("nombre-field");
    let emailField = document.getElementById("email-field");
    let passField = document.getElementById("pass-field");
    let regBtn = document.getElementById("regBtn");
    let inSeBtn = document.getElementById("inSeBtn");
    inSeBtn.onclick = function(){
        nombreField.style.maxHeight = "0";
        titulo.innerHTML = "Iniciar Sesión";
        regBtn.classList.add("disable");
        inSeBtn.classList.remove("disable");
    };
    regBtn.onclick = function(){
        nombreField.style.maxHeight = "65px";
        titulo.innerHTML = "Registrarme";
        regBtn.classList.remove("disable");
        inSeBtn.classList.add("disable");
    };
    email.onblur = validaEmail;
    pass.onblur = validaPass;
    nombre.onblur = validaNombre;
    function validaNombre(){
        if(!nombre.value.match(/^[A-Za-z]+$/)){
            errorNombre.innerHTML = "Sin números ni símbolos";
            nombreField.classList.add("input-error");
            return false;
        }
        errorNombre.innerHTML = "";
        nombreField.classList.remove("input-error");
        return true;
    }
    function validaEmail(){
        if(!email.value.match(/^[A-Za-z._\-0-9]+@[A-Za-z]+\.[a-z]{2,4}$/)){
            errorEmail.innerHTML = "Email inválido";
            emailField.classList.add("input-error");
            return false;
        }
        errorEmail.innerHTML = "";
        emailField.classList.remove("input-error");
        return true;
    }
    function validaPass(){
        if(!pass.value.match(/^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,16}$/)){
            errorPass.innerHTML = "Contraseña inválida";
            passField.classList.add("input-error");
            return false;
        }
        errorPass.innerHTML = "";
        passField.classList.remove("input-error");
        return true;
    }
});