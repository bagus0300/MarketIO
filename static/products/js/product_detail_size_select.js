let sizeOptions = document.querySelectorAll("[data-variant]");

// Handles click event. Adds classes and sets attribute.
function handler(e) {
  classes = ["bg-primary", "text-white"];
  if (document.querySelector('[data-selected="true"]')) {
    prevSelection(classes);
  }
  let selection = e.target;
  let variantInput = document.querySelector('[name="product_variant"]');
  selection.classList.add(...classes);
  selection.setAttribute("data-selected", true);
  variantInput.setAttribute("value", selection.getAttribute("data-variant"));
}

// Deslects previous selected variant and removes styles
function prevSelection(classes) {
  let prevSelection = document.querySelector('[data-selected="true"]');
  prevSelection.setAttribute("data-selected", "");
  prevSelection.classList.remove(...classes);
}

// Adds click listener to each variant button.
sizeOptions.forEach((sizeOption) => {
  sizeOption.addEventListener("click", handler);
});
