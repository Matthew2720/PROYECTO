const menu = document.querySelector(".menu");
if menu{
  
}
/*seleccione el elemente que tiene clase menu*/
const openMenuBtn = document.querySelector(".open-menu");
/*seleccione el elemente que tiene clase menu*/
const closeMenuBtn = document.querySelector(".close-menu");
/*seleccione el elemente que tiene clase menu*/

/* se crea una funcion con el toggle que genera la accion de  que si el menu esta abierto lo cierre  y si esta cerrado lo abra */
function toggleMenu() {
  menu.classList.toggle("menu_opened");
  /*se selecciona el elemento menu , luego se le dice que le aga toggle a la clase
  menu open*/
}

openMenuBtn.addEventListener("click", toggleMenu);
/* se le indica que escuche el evento cuando se haga click  y luego ejecute lo que hay en togglemenu */ 
closeMenuBtn.addEventListener("click", toggleMenu);

