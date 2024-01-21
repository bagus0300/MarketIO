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
  stripe.confirmPayment({
    elements,
    confirmParams: {
      //   return_url: "https://laced.carlmurray.design/checkout/confirmation/",
      return_url: "http://localhost:8000/checkout/confirmation/",
      receipt_email: email,
    },
  });
}
