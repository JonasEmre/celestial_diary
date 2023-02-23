document.addEventListener("DOMContentLoaded", function() {
  var navbarToggle = document.getElementById("navbar-toggle");
  var navbarLinks = document.getElementById("navbar-links");

  navbarToggle.addEventListener("click", function() {
    if (navbarLinks.style.display === "block") {
      navbarLinks.style.display = "none";
    } else {
      navbarLinks.style.display = "block";
    }
  });
});
