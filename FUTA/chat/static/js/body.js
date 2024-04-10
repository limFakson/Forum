
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

let toggler = true;

function switchMode(){
    toggler = !toggler
    
    const darkmode = document.getElementById('dark');
    const lightmode = document.getElementById('light');
    const mode = document.getElementById("mode");

    if(toggler){
        lightmode.style.display = 'none';
        darkmode.style.display = 'block';
        mode.textContent = 'Dark Mode';
    }else{
        lightmode.style.display = 'block';   
        darkmode.style.display = 'none';
        mode.textContent = 'Light Mode';
    }
}   
