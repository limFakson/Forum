
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

let toggler = false;

function switchMode(){
    toggler = !toggler

    const darkmode = document.getElementById('dark');
    const lightmode = document.getElementById('light');
    const mode = document.getElementById("mode");

    function changeModeCss(cssFilePath) {
        const linkElement = document.getElementById('modeCss');
        if (linkElement) {
            // Change the href attribute to the new CSS file path
            linkElement.href = cssFilePath;
        }
    }

    if(toggler){
        lightmode.style.display = 'none';
        darkmode.style.display = 'block';
        mode.textContent = 'Dark Mode';
        const newCssFilePath = "/static/css/mode.css";
        changeModeCss(newCssFilePath);
    }else{
        lightmode.style.display = 'block';   
        darkmode.style.display = 'none';
        mode.textContent = 'Light Mode';
        const newCssFilePath = ' ';
        changeModeCss(newCssFilePath)
    }
}   
