// Script for controlling add to cart button state change
// Handles failed htmx requests and shows user feedback
// Controls button content and transitions

let cartCtaText = document.querySelector("#cta-text"); // Text span elt
let defaultCtaInnerText = cartCtaText.innerText; // Stores default text from CTA
let form = document.querySelector("form");
let submitBtn = document.querySelector("#submit"); // Add to cart btn
let errorMsg = document.querySelector("#errorMsg");
let errorMsgVisible = false;

// Listen for htmx request on add to cart CTA click
form.addEventListener("htmx:beforeRequest", handleRequest);

// Handles request
// Show success or error feedback
function handleRequest(e) {
  // Hide CTA text on click
  cartCtaText.classList.add("hidden");

  // Listen for request to finish and show appropriate feedback (success/error)
  form.addEventListener("htmx:afterRequest", function (e) {
    // If error previously shown, hide
    if (errorMsgVisible) {
      errorMsg.classList.add("invisible");
      errorMsgVisible = !errorMsgVisible;
    }
    // If request successful, show feedback
    if (e.detail.successful) {
      cartCtaText.innerHTML =
        '<svg width="25" height="25" viewBox="0 0 29 29" fill="none" xmlns="http://www.w3.org/2000/svg">' +
        '<circle cx="14.5" cy="14.5" r="13.5" stroke="#fff" stroke-width="2"/>' +
        '<path d="M7 15L11.5 19.5L22 9" stroke="#fff" stroke-width="2" /></svg >';
      cartCtaText.classList.remove("hidden");
      // Hide svg and transition back to default inner text
      setTimeout(function () {
        cartCtaText.classList.add("opacity-0");
        setTimeout(function () {
          cartCtaText.innerText = defaultCtaInnerText;
          cartCtaText.classList.remove("opacity-0");
        }, 500);
      }, 2000);
    }
    // If request failed, show error msg
    else {
      cartCtaText.innerText = "👎";
      cartCtaText.classList.remove("hidden");
      cartCtaText.classList.remove("opacity-0");
      errorMsg.innerText =
        "Something went wrong. Please refresh the page and try again.";
      errorMsg.classList.remove("invisible");
      errorMsgVisible = !errorMsgVisible;
    }
  });
}
