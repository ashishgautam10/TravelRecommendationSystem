var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("tip-bar").style.top = "0";
  } else {
    document.getElementById("top-bar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}