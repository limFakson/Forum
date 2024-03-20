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

