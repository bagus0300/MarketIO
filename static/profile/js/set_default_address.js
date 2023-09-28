let setDefaultBtns = document.querySelectorAll(".setDefaultBtn");

setDefaultBtns.forEach((btn) => {
  btn.addEventListener("htmx:afterSettle", setDefault);
});

function setDefault(e) {
  let setDefaultBtns = document.querySelectorAll(".setDefaultBtn");
  // unsets previous default address
  let previousDefault = document.querySelector('[data-default="true"]');
  previousDefault.removeAttribute("data-default");

  // sets new default address
  let newDefault = e.target;
  newDefault.setAttribute("data-default", "true");
  setDefaultBtns = document.querySelectorAll(".setDefaultBtn");
}
