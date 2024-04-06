
function imgUpload() {
    console.log('click')
    document.getElementById('id_image').click();
}

document.getElementById('id_image').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const mediaDisplay = document.createElement('img');
            mediaDisplay.src = event.target.result;
            document.getElementById('media').appendChild(mediaDisplay); 
            mediaDisplay.style.borderRadius = '15px';
            mediaDisplay.style.height = '170px';
        }
        reader.readAsDataURL(file);
    }
});

function docUpload() {
    console.log('click')
    document.getElementById('id_docm').click();
}

document.getElementById('id_docm').addEventListener('change', (event) => {
    const file = event.target.files[0];

    if (file) {
        const documentNameElement = document.getElementById('documentName');
        const documentSizeElement = document.getElementById('documentSize');
        const documentTypeElement = document.getElementById('documentType');

        const displayName = file.name.length > 25 ? file.name.substring(0, 25) + '...' : file.name;
        documentNameElement.textContent = displayName;
        documentSizeElement.textContent = formatBytes(file.size);
        documentTypeElement.textContent = getFileExtension(file.name).toUpperCase();

        document.getElementById('docm').style.display = 'flex';
    }

    function formatBytes(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    function getFileExtension(filename) {
        return filename.split('.').pop();
    }

});

document.addEventListener('DOMContentLoaded', function() {
    const documentLink = document.getElementById('documentLink');
    const documentInfoList = document.getElementById('documentInfoList');
    const documentNameElement = document.getElementById('documentpName');

    // Extract filename from URL and display in document info
    const url = documentLink.href;
    const urlParts = url.split('/');
    const filename = urlParts[urlParts.length - 1];
    const displayName = filename.length > 15 ? filename.substring(0, 15) + '...' : filename;
    documentNameElement.textContent = displayName;
});

function postPage() {};