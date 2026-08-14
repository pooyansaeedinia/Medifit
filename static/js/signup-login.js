// Switch between login and signup
const switchLogin = document.querySelector(".switch-login");
const switchSignup = document.querySelector(".switch-signup");
const loginSection = document.querySelector(".login-section");
const signupSection = document.querySelector(".signup-section");
const loginLink = document.getElementById("signup-link");
const signupLink = document.getElementById("login-link");

function showLogin() {
    switchLogin.classList.add("active");
    switchSignup.classList.remove("active");
    loginSection.style.display = "block";
    signupSection.style.display = "none";
}

function showSignup() {
    switchSignup.classList.add("active");
    switchLogin.classList.remove("active");
    signupSection.style.display = "block";
    loginSection.style.display = "none";
}

switchLogin.addEventListener("click", showLogin);
switchSignup.addEventListener("click", showSignup);

if (loginLink) {
    loginLink.addEventListener("click", function(e) {
        e.preventDefault();
        showSignup();
    });
}

if (signupLink) {
    signupLink.addEventListener("click", function(e) {
        e.preventDefault();
        showLogin();
    });
}