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
// Password eye
const loginPassword = document.getElementById("login-password");
const loginToggle = document.getElementById("login-toggle-password");

if (loginToggle && loginPassword) {
    loginToggle.addEventListener("click", function() {
        if (loginPassword.type === "password") {
            loginPassword.type = "text";
            loginToggle.classList.remove("bi-eye");
            loginToggle.classList.add("bi-eye-slash");
        } else {
            loginPassword.type = "password";
            loginToggle.classList.remove("bi-eye-slash");
            loginToggle.classList.add("bi-eye");
        }
    });
}

const signupPassword = document.getElementById("signup-password");
const signupConfirm = document.getElementById("signup-confirmPassword");
const signupToggles = document.querySelectorAll(".signup-form .toggle-password");

for (let i = 0; i < signupToggles.length; i++) {
    const icon = signupToggles[i];
    let input = null;

    if (icon.previousElementSibling && icon.previousElementSibling.tagName === "INPUT") {
        input = icon.previousElementSibling;
    }

    if (input) {
        icon.addEventListener("click", function() {
            if (input.type === "password") {
                input.type = "text";
                icon.classList.remove("bi-eye");
                icon.classList.add("bi-eye-slash");
            } else {
                input.type = "password";
                icon.classList.remove("bi-eye-slash");
                icon.classList.add("bi-eye");
            }
        });
    }
}

// General functions
function showError(input, message) {
    const existingError = input.parentElement.querySelector("small");
    if (existingError) existingError.remove();

    input.style.borderColor = "#e74c3c";

    const error = document.createElement("small");
    error.textContent = message;
    input.parentElement.appendChild(error);

    setTimeout(function() {
        if (error && error.remove) {
            error.remove();
            input.style.borderColor = "#e8e0d5";
        }
    }, 3000);
}

function removeAllErrors() {
    const errors = document.querySelectorAll("small");
    for (let i = 0; i < errors.length; i++) {
        errors[i].remove();
    }

    const inputs = document.querySelectorAll("input");
    for (let i = 0; i < inputs.length; i++) {
        inputs[i].style.borderColor = "#e8e0d5";
    }
}

function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Control login form
const loginEmail = document.getElementById("login-email");
const loginPasswordInput = document.getElementById("login-password");
const loginForm = document.querySelector(".login-form");

if (loginForm) {
    loginForm.addEventListener("submit", function(e) {
        e.preventDefault();
        removeAllErrors();

        let isValid = true;
        const email = loginEmail.value.trim();
        const password = loginPasswordInput.value.trim();

        if (email === "") {
            showError(loginEmail, "Email cannot be empty");
            isValid = false;
        } else if (!isValidEmail(email)) {
            showError(loginEmail, "Please enter a valid email address");
            isValid = false;
        }

        if (password === "") {
            showError(loginPasswordInput, "Password cannot be empty");
            isValid = false;
        } else if (password.length < 6) {
            showError(loginPasswordInput, "Password must be at least 6 characters");
            isValid = false;
        }

        if (isValid) {
            alert("Login successful!");
        }
    });
}

// Control signup form
const signupName = document.getElementById("signup-name");
const signupEmail = document.getElementById("signup-email");
const signupPasswordInput = document.getElementById("signup-password");
const signupConfirmInput = document.getElementById("signup-confirmPassword");
const signupForm = document.querySelector(".signup-form");

if (signupForm) {
    signupForm.addEventListener("submit", function(e) {
        e.preventDefault();
        removeAllErrors();

        let isValid = true;
        const name = signupName.value.trim();
        const email = signupEmail.value.trim();
        const password = signupPasswordInput.value.trim();
        const confirm = signupConfirmInput.value.trim();

        if (name === "") {
            showError(signupName, "Name cannot be empty");
            isValid = false;
        } else if (name.length < 2) {
            showError(signupName, "Name must be at least 2 characters");
            isValid = false;
        }

        if (email === "") {
            showError(signupEmail, "Email cannot be empty");
            isValid = false;
        } else if (!isValidEmail(email)) {
            showError(signupEmail, "Please enter a valid email address");
            isValid = false;
        }

        if (password === "") {
            showError(signupPasswordInput, "Password cannot be empty");
            isValid = false;
        } else if (password.length < 6) {
            showError(signupPasswordInput, "Password must be at least 6 characters");
            isValid = false;
        }

        if (confirm === "") {
            showError(signupConfirmInput, "Please confirm your password");
            isValid = false;
        } else if (password !== confirm) {
            showError(signupConfirmInput, "Passwords do not match");
            isValid = false;
        }

        if (isValid) {
            alert("Signup successful! Please login.");
            signupForm.reset();
            showLogin();
        }
    });
}

showLogin();