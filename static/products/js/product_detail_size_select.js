let sizeOptions = document.querySelectorAll("[data-variant]");

function handler(e) {
    classes = ["bg-primary", "text-white"];
  if (document.querySelector('[data-selected="true"]')) {
    prevSelection(classes);
  }
  let selection = e.target;
  selection.classList.add(...classes);
  selection.setAttribute("data-selected", true);
}

function prevSelection(classes) {
  let prevSelection = document.querySelector('[data-selected="true"]');
  prevSelection.setAttribute("data-selected", '');
  prevSelection.classList.remove(...classes)
}

sizeOptions.forEach((sizeOption) => {
  sizeOption.addEventListener("click", handler);
});
