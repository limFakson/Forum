
function mediaUpload() {
    console.log('click')
    document.getElementById('id_post_media').click();
}

document.getElementById('id_post_media').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const mediaDisplay = document.createElement('img');
            mediaDisplay.src = event.target.result;
            document.getElementById('postInput').appendChild(mediaDisplay); 
        }
        reader.readAsDataURL(file);
    }
});
