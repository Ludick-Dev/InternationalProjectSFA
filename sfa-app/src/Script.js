/*-----------JS Code for the camera operation-------------*/
let video = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (error) {
      console.log("Something went wrong!");
    });
} else {
  console.log("getUserMedia not supported!");
}

/*------Code for sticky navigation bar------*/

window.addEventListener("scroll", function () {
  var header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 0);
});
/*------------------------------------------*/

/*--------More code for Sticky Navbar---------*/

const navigationHeight = document.querySelector("header").offsetHeight;

document.documentElement.style.setProperty(
  "--scroll-padding",
  navigationHeight + "px"
);
