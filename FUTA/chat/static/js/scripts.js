
function uploadImage() {
    document.getElementById('id_profile_picture').click();
}

document.getElementById('id_profile_picture').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(event) {
        document.getElementById('profile').src = event.target.result;
      }
      reader.readAsDataURL(file);
    }
  });

const form = document.getElementById('form');
const error = document.getElementById('error');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    
    const password = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;

    
    const passwordRegex = /^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;
    if (!passwordRegex.test(password)) {
        const regexMessage = 'Password must be at least 6 characters, contain 1 number, and a special character';
        console.log(regexMessage);
        error.textContent = regexMessage;
        return;
    }

    
    if (password !== password2) {
        const message = 'Passwords do not match';
        console.log(message);
        error.textContent = message;
        return;
    }

    
    form.submit();
});


document.getElementById('id_password1').addEventListener('input', () => {
    const password = document.getElementById('id_password1').value;
    const passwordRegex = /^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;
    
    
    if (!passwordRegex.test(password)) {
        const regexMessage = 'Password must be at least 6 characters, contain 1 number, and a special character';
        console.log(regexMessage);
        error.textContent = regexMessage;
    } else {
        error.textContent = '';
    }
});