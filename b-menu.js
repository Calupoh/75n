const b_menu = document.querySelector('#b-menu');


function show_menu() {
    var pop_menu = document.querySelector('#pop-menu');
    x = pop_menu.style.display;
    if ( x == 'none' || x == '') {
        pop_menu.style.display = 'flex';
        pop_menu.style['flex-direction'] = 'column';
        b_menu.style.background = '#0e3296cb';
        b_menu.style.color = 'aliceblue';
    }
    else {
        pop_menu.style.display = 'none';
        b_menu.style.background = 'none';
        b_menu.style.color = 'black';
    }
}

b_menu.addEventListener('click', show_menu);