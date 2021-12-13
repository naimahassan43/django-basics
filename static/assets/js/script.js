const toggleBtn = document.getElementsByClassName("navbar-toggle")[0];
const navbarItem = document.getElementsByClassName("navbar-item");

toggleBtn.addEventListener("click", function () {
  for (let i = 0; i < navbarItem.length; i++)
    navbarItem[i].classList.toggle("active");
});
// window.addEventListener("scroll", function () {
//   let header = document.querySelector("header");
//   header.classList.toggle("sticky", window.scrollY > 0);
// });
