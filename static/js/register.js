console.log("register");
// Script nd Function for form submission and password validation
const form = document.getElementById("form");
const error = document.getElementById("error");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const password = document.getElementById("id_password1").value;
  const password2 = document.getElementById("id_password2").value;

  const passwordRegex = /^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;
  //  if (!passwordRegex.test(password)) {
  //      const regexMessage = 'Password must be at least 6 characters, contain 1 number, and a special character';
  //      console.log(regexMessage);
  //      error.textContent = regexMessage;
  //      return;
  //  }

  if (password !== password2) {
    const message = "Passwords do not match";
    console.log(message);
    error.textContent = message;
    return;
  }

  form.submit();
});

document.getElementById("id_password1").addEventListener("input", () => {
  const password = document.getElementById("id_password1").value;
  const passwordRegex = /^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;

  if (!passwordRegex.test(password)) {
    const regexMessage =
      "Password must be at least 6 characters, contain 1 number, and a special character";
    console.log(regexMessage);
    error.textContent = regexMessage;
  } else {
    error.textContent = "";
  }
});
