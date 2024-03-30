
document.addEventListener("DOMContentLoaded", function() {
    //Fade in animation for webpage
    var bodyElements = document.querySelectorAll('body *');
    for (var i = 0; i < bodyElements.length; i++){
        var isHeaderOrInsideHeader = false;
        var element = bodyElements[i];
        while (element) {
            if (element.tagName === 'HEADER') {
                isHeaderOrInsideHeader = true;
                break;
            }
            element = element.parentElement;
        }
        if (!isHeaderOrInsideHeader) {
            bodyElements[i].classList.add('fadeIn');
        }
    }
});
