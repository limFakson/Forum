document.addEventListener('DOMContentLoaded', function() {
  function uploadImage() {
      document.getElementById('file-input').click();
  }

  document.getElementById('file-input').addEventListener('change', function() {
      var file = this.files[0];
      var reader = new FileReader();
      reader.onload = function(e) {
          document.getElementById('profile-pic').src = e.target.result;
      };
      reader.readAsDataURL(file);
  });

  // Optional: Add click event listener to the profile picture
  document.getElementById('profile-pic').addEventListener('click', uploadImage);
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