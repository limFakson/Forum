 
// Function for change of profile picture and upload of profile picture
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
