var delayInMilliseconds = 1000;

window.addEventListener('load', () => {
    setTimeout(function() {
        const loader_bg = document.querySelector(".loader_bg");
        loader_bg.classList.add("preload-finish")
        const loader = document.querySelector(".loader");
        loader.classList.add("preload-finish1")
      }, delayInMilliseconds);
})