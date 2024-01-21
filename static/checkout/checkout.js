// TEST API KEY
const stripe = Stripe(
  "pk_test_51NbLmNBTGDhz14YGUPhmxtehPHbzVTepagoF5lU9EbqpuD0iUVhidmmf3S4OgLecGecnj3w1VPSG8LNS8PJ0VUq600srgN4uDP"
);

let elements;
let email;

initialise();

// Creates Stripe PaymentIntent and mounts Stripe Elements
async function initialise() {
  let clientSecret = await createPaymentIntent();
  let elements = createStripeElements();
  const paymentForm = document.querySelector("#payment-form");
  paymentForm.addEventListener("submit", handleSubmit);
}

// Gets CSRF token from cookie to send with PaymentIntent fetch request
function getCsrfToken() {
  const csrfToken = document.cookie
    .split("; ")
    .find((row) => row.startsWith("csrftoken="))
    .split("=")[1];
  return csrfToken;
}

//
async function createPaymentIntent() {
  // Get CSRF token
  const csrfToken = getCsrfToken();
  // Fetch PaymentIntent from Django endpoint
  const response = await fetch("/create_payment_intent/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken, // Add CSRF token here
    },
  });
  const paymentIntent = await response.json();
  // Capture client secret from PaymentIntent to use in Stripe Elements
  clientSecret = paymentIntent.intent.client_secret;
  email = paymentIntent.intent.metadata.email;
  return clientSecret;
}

// Create and mount Stripe Elements
function createStripeElements() {
  elements = stripe.elements({ clientSecret });
  let paymentElement = elements.create("payment");
  paymentElement.mount("#payment-elements");
}

function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);
  stripe.confirmPayment({
    elements,
    confirmParams: {
      //   return_url: "https://laced.carlmurray.design/checkout/confirmation/",
      return_url: "http://localhost:8000/checkout/confirmation/",
      receipt_email: email,
    },
  });

  if (error.type === "card_error" || error.type === "validation_error") {
    showMessage(error.message);
  } else {
    showMessage("An unexpected error occurred.");
  }

  setLoading(false);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}
