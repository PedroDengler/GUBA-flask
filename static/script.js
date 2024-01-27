// Abre y cierra el Menu
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
  }
  
  // Cerrar el menú si se hace clic en cualquier parte de la página
  document.addEventListener('click', function (event) {
    const menu = document.querySelector('.menu');
    const menuIcon = document.querySelector('.menu-icon');
    
    if (!menu.contains(event.target) && event.target !== menuIcon) {
      menu.style.display = 'none';
    }
  });