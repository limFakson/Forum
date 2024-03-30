
// Script for homepage mobile menu slides
const openMenu = document.getElementsByClassName('open-menu')[0];
const closeMenu = document.getElementsByClassName('close-menu')[0];

openMenu.addEventListener('click', () =>{
    const nav = document.getElementsByClassName('side_nav')[0];
    console.log('clicked')
    nav.style.left = '0';
});
closeMenu.addEventListener('click', () =>{
    const nav = document.getElementsByClassName('side_nav')[0];
    console.log('clicked')
    nav.style.left = '-100%';
});
