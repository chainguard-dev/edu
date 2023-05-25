document.addEventListener("DOMContentLoaded", function(event){
  moveRumble();
});

function moveRumble() {
    let getIt = document.querySelector('#get-it');
    let rumble = document.querySelector('#rumble');
    let newRumble = rumble.cloneNode(true);
    rumble.remove();
    getIt.insertAdjacentElement('beforebegin', newRumble);
};
