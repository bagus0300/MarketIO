# laced-pp5

Django-based eCommerce site

# Project Background

- Laced is a fictional eCommerce store selling AI-generated shoes.
- The project was my fifth and final project submitted as part of my Diploma in Full Stack Web Development with Code Institute and aims to combine the skills learned throughout the course from front-end development, UX design, databases testing and full-stack frameworks, APIs and payment services.

# Process

## Design

- Mockups were designed in Figma to explore layout options which would then serve as a guide for development.

## Agile Development

- The development process was carried out using an Agile methodology with a focus on iterative development and continuous improvement.
- The project was managed using a GitHub Project board with user stories and tasks.
- User Stories were sized using T-shirt sizing (XS, S, M, L, XL) and prioritised based on the MoSCoW method (Must have, Should have, Could have, Won't have).

### User Stories

1. As a customer, I want to be able to create a new account on the website so that I can save my shipping and billing information for future purchases. (Must have)
2. As a customer, I want to be able to browse products by categories (e.g., Men's Shoes, Women's Shoes) so that I can easily find what I'm looking for.
3. As a customer, I want to be able to search for products by keywords so that I can quickly locate specific items.
4. As a customer, I want to see detailed product information, including product descriptions, prices, available sizes, and customer reviews, so that I can make an informed purchasing decision. (Must have)
5. As a customer, I want to add products to my shopping cart and review the items in my cart before proceeding to checkout. (Must have)
6. As a customer, I want to be able to select my preferred shipping method and enter my shipping address during the checkout process. (Must have)
7. As a customer, I want to have multiple payment options (e.g., credit card, PayPal) when making a purchase.
8. As a customer, I want to receive order confirmation emails with details of my purchase after completing a transaction.
9. As a customer, I want to be able to view and track the status of my orders, including order history and estimated delivery dates.
10. As a customer, I want to be able to leave reviews and ratings for products I've purchased to share my experiences with other users.
11. As an admin, I want to review and moderate customer reviews and ratings to ensure the quality of user-generated content.
12. As an admin, I want to be able to log in securely to the admin panel of the e-commerce platform to manage the website's content and functionality. (Must have)
13. As an admin, I want to add, edit, or remove product listings, including product details, images, and pricing, to keep the online store up-to-date. (Must have)
14. As an admin, I want to categorise products into different categories and subcategories to improve navigation for customers.

# Features

## CRUD Functionality

- User CRUD functionality on the front-end was implemented primarily relates to the `UserAddress` model.
  - Create: Users can add a new address from their profile.
  - Read: Users can view all of their saved addresses.
  - Update: Users can edit a saved address.
  - Delete: Users can delete addresses from their profile.
- Admin CRUD functionality exists for all Models and is done from the Django Admin dashboard.

## Authentication & Authorisation

- Users can create an account from the Signup page.
- Users can login from the Login page.
- Authorisation is required to reach certain pages such as Account and Checkout. Requesting these pages while unauthprised will redirect users to the Login page.

## Homepage

- The homepage shows Featured products and Sale products.
- Six Featured/Sale products shown are chosen at random each time the page is loaded.

## Footer

- The footer features social links and a newsletter signup form.

## Shop Page

- The Shop page, accessed from the top navigation, shows all products.

## Product Detail Page

- Each product has a product detail page with the product image, price and description.
- Users can select a product variant, choose a quantity and add to cart.
- Only variants which are in stock are shown on the page.
- When the Add to Cart button is pressed, an AJAX request is sent to a Django view which updates the user's cart.

## Account

The Account page contains the following pages:

### Orders
- The user can view all of their order history.

### Addresses
- CRUD functionality is implemented in this page.
- The user can create, edit or delete a shipping address which can then be selected during checkout.

### Favourites
- The user can add a product as a "favourite" from the product detail page.
- The Favourites page lets the user review their favourited products to make purchasing at a later date easier.


## Cart
- If a user is not logged in, the cart is associated with the current session ID. It can then be converted to a user's cart if they decide to login, so that they don't lose their items.
- A badge beside the cart shows the quantity of items in the current cart, and is updated via `htmx` when a product is added/removed to/from the cart.


## Checkout
- The checkout page features an address selection widget that uses `htmx` to update the chosen address.
- The payment form utilises Stripe Elements to ensure the secure and PCI compliant processing of payments.
- An order summary is shown so the user can review their order before payment.

## Roadmap

The site has been delivered in its current state as an MVP and there is still much work to do to improve the UX and functionality of the site, including:

- Product search and filters
- Discount code functionality
- Choice of shipping methods
- Contact page


# Technologies

- htmx was used to implement functionality throughout the site, including "Add to Cart" functionality and the "Change address" feature on the Checkout page.
- Alpine.js was used to implement the item quantity selectors on the product detail and cart pages.
- Stripe Elements was used to implement a PCI compliant checkout.
- The project is built on top of the Django framework.
- The database technology used is postgreSQL.
- Leonardo.ai was used to generate product images.
- Tailwind CSS was used to style front-end elements.

# ⚙️ Technologies Used

This section outlines the various technologies used throughout the project and the purpose each serves.

## 💾 Core Development Technologies

<details>

- [Django](https://www.djangoproject.com/) used as a full-stack framwork for developing the app.
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/) used for client-side interaction and validation.
- [HTML](https://html.spec.whatwg.org/)/[CSS](https://www.w3.org/Style/CSS/Overview.en.html) + [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/) used for building out site pages.

</details>

## 📚 Libraries, Frameworks and Packages

<details>

- [Tailwind CSS](https://tailwindcss.com/) - used to style elements throughout the site.
- [htmx](https://htmx.org/) - an open-source lightweight library used to fetch and load content dynamically via AJAX requests. Utilised specifically for the "Add to Cart" functionality and the "Change address" feature on the Checkout page.
- [Alpine JS](https://alpinejs.dev/) - Used to implement the item quantity selectors on the product detail and cart pages.

</details>

## Python/Django Packages

<details>

- [Gunicorn](https://pypi.org/project/gunicorn/) - provides HTTP server.
- [psycopg2](https://pypi.org/project/psycopg2/) - provides PostgreSQL connection.
- [Pillow](https://pypi.org/project/Pillow/) - used for image processing (Model ImageField).
- [Whitenoise](https://pypi.org/project/whitenoise/) - used for serving static files.
- [Django Markdown Field](https://pypi.org/project/django-markdownfield/) - adds a markdown-compatible text field to admin panel (for BlogPost model).
- [Black](https://pypi.org/project/black/) - A PEP8 compliant code formatter.
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - used for debugging.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) and [Boto3](https://pypi.org/project/boto3/) - used for storing static files and media files on AWS S3.

</details>

## Infrastructural Technologies

<details>

- [PostgreSQL](https://www.postgresql.org/) (via Digital Ocean) - used for database.
- [Heroku](https://www.heroku.com/) - used for hosting the application.
- [AWS S3](https://aws.amazon.com/s3/) - used for storing static files and media files.
- [AWS CloudFront](https://aws.amazon.com/cloudfront/) - used to cache static and media files.

</details>

## Integrations

<details>

- [Stripe Elements](https://stripe.com/docs/payments/elements) - used for PCI compliant payments processing

</details>

## Content

<details>

- [Leonardo.ai](https://leonardo.ai) - used to generate product images

</details>



# Business Model

- Laced is an online eCommerce store where customers can purchase footware online and have it delivered to them.
- All footware designs are AI generated using Leonardo.ai image generation, offering unique and differentiated footware designs.

## Marketing

### SEO

- Keywords such as "performance", "agility" and speed were included in the product descriptions to boost search engine ranking.
- A meta description was added to all products and main pages of the site for SEO purposes.
- There is a significant amount of work involved in renaming all product images and adding alt text to improve SEO, and these items were considered outside of the scope of this project.

### Social

- A fictional Facebook business page was set up for the eCommerce store which offers several advantages:

  - Increased Visibility: Facebook is one of the most popular social media platforms globally, with billions of active users. By having a presence on Facebook, the eCommerce store can increase its visibility and reach a wider audience.

  - Customer Engagement: Facebook provides a platform for direct interaction with customers. Users can like, comment, and share posts, allowing for real-time engagement and feedback. This interaction fosters a sense of community around the brand and helps build relationships with customers.

  - Marketing Opportunities: Facebook offers various marketing tools, such as targeted advertising and sponsored posts, that enable the store to reach specific demographics and target audiences. These tools can help drive traffic to the website and increase sales.

  - Brand Building: A Facebook business page allows the store to showcase its brand personality, values, and story. Consistent branding across social media channels helps establish brand identity and recognition.

  - Customer Support: Facebook can serve as a customer support channel, allowing customers to ask questions, seek assistance, and provide feedback. Timely responses to inquiries demonstrate excellent customer service and can help build trust and loyalty.

## Newsletter

- A newletter form is present on the footer of every page, which offers a variety of benefits:

  - Lead Generation: The newsletter form serves as a lead generation tool, allowing visitors to subscribe to receive updates, promotions, and other relevant content from the store. By capturing email addresses, the store can build a valuable database of potential customers.

  - Direct Communication: Newsletters provide a direct line of communication with subscribers. The store can use newsletters to share product announcements, special offers, industry news, and other information directly with customers, without relying on third-party platforms.

  - Customer Retention: Regular newsletters help keep the store top-of-mind for subscribers, increasing the likelihood of repeat purchases. By providing valuable content and exclusive offers, newsletters can help foster customer loyalty and retention.

  - Traffic and Engagement: Newsletters can drive traffic to the website by promoting new products, blog posts, or other content. Additionally, newsletters can encourage engagement by including calls-to-action that prompt subscribers to visit the website or follow the store on social media.

  - Analytics and Insights: Newsletter platforms typically provide analytics tools that allow the store to track open rates, click-through rates, and other metrics. These insights can help optimize future campaigns and improve overall marketing effectiveness


# Bugs

## Resolved

- A bug was identified where an address could be added multiple times by refreshing the page after submitting the address form. This was resolved by adding a redirect on submission.
- During development, when a user deleted their default address, it caused issues in the checkout and profile as no new default address was being set. This was resolved by including logic to set a new default address every time the current default is deleted.
- During testing of the payments integration, it was found that a new address was being added every time a payment/order was processed. This was due to incorrectly configured model inheritance where the `OrderAddress` was inherting from `UserAddress`, which meant every time an `OrderAddress` was created, it was also reflected in the `UserAddress` table. This was corrected by using an abstract `Address` class which both `UserAddress` and `OrderAddress` would inherit from, each now having their own tables in the database.

## Unresolved

- Slow SQL queries are present throughout the site, particularly in the Admin site when browsing models. Attempts to fix this using `prefetch_related` have not been successful and further investigation is required which is planned for future development.


### 🧮 Data Models

<details>

The data models for the project are shown below:

![Database schema](/readme/dbdiagram.png)

- Users app:
  - `User` - custom user model which extends the Django `AbstractUser` model. Default username field is replaced with email field.
  - `UserAddress` - a user's shipping/billing address.
  - `UserFavourite` - products a user has added to 'Favourites'

<br>

- Core app:
  - `Product` - represents a product. Contains name, SKU, description, category, price, sale_price and is_featured.
  - `ProductCategory` - represents a category of products Contains name.
  - `ProductImage` - represents Passengers associated with a Booking. Contains image and product.
  - `ProductVariant` - represents a product variant such as different sizes. Contains product, size and quantity.
  - `Cart` - represents a user's or session cart. Contains user and/or session ID if user not logged in.
  - `CartItem` - represents an item in a cart. Contains item, cart and quantity.

<br>

</details>
</details>
</details>

---

<br>
<br>
<br>

---

# 🧪 Testing

## ⚒️ Manual Testing

### 🛰️ Overview

<details>

- Responsiveness was tested as per below table (go to section: [Responsiveness](#-responsiveness-testing))
- All HTML files were passed through the W3C validator with no errors
- All JavaScript files were passed through JSHint with no errors present.
- The website was tested on major browsers including Chrome, Safari, Firefox and Edge.
- All user flows were tested in depth including navigating through the purchase flow, clicking CTAs and links, and form submission.
- All forms were tested to ensure validation was present and that forms could be submitted without error
- Lighthouse was used to test for Performance, Accessibility, Best Practices and SEO and adjustments were made to improve test results.
- WAVE was used to test for accessibility issues and adjustments were made to improve test results.

</details>

---

### 🧪 General Testing

<details>
<summary>Expand test detail</summary>

| Test                  | Action                                                                                                                                                                                         | Success Criteria                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Homepage loads        | Navigate to website URL                                                                                                                                                                        | Page loads < 3s, no errors                                                    |
| Links                 | Click on each Navigation link, CTA, button, logo, footer link                                                                                                                                  | Correct page is loaded/correct action performed, new tab opened if applicable |
| Form validation       | Enter data into each input field, ensure only valid data is accepted                                                                                                                           | Form doesn't submit until correct data entered, error message shown           |
| Responsiveness        | Resize viewport window from 320px upwards with Chrome Dev Tools. Test devices as detailed in [Responsiveness Testing](#-responsiveness-testing)                                                | Page layout remains intact and adapts to screen size as intended              |
| Lighthouse            | Perform Lighthouse test on each page for the primary user flow (Booking process)                                                                                                               | Score of > 89 on Performance, Accessibility, Best Practices                   |
| Browser compatibility | Test links, layout, appearance, functionality and above Tests on Chrome, Safari, Firefox and Edge. BrowserStack used to test various mobile/large format devices with recent browser versions. | Website looks and functions as intended and passes all tests above            |

</details>

---

### 🏠 Homepage Testing

<details>
<summary>Expand test detail</summary>

| Test                       | Action                                                                 | Success Criteria                                                  |
| -------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------- |
| CTA Clickability           | - Click on the Call to Action (CTA) button                             | - Button redirects to the appropriate page or section of the site |
| Featured Products Display  | - Verify if the featured products section is displayed                 | - 6 featured products are visible on the homepage                 |
| Sale Products Display      | - Verify if the sale products section is displayed                     | - 6 sale products are visible on the homepage                     |
| Featured Product Links     | - Click on each of the featured product images or titles               | - Each click redirects to the corresponding product page          |
| Sale Product Links         | - Click on each of the sale product images or titles                   | - Each click redirects to the corresponding product page          |
| CTA Visibility             | - Ensure that the CTA is visible without scrolling                     | - CTA is displayed within the viewport of the user's screen       |
| Featured Products Accuracy | - Compare the displayed featured products with the backend data        | - Ensure that the correct products are being displayed            |
| Sale Products Accuracy     | - Compare the displayed sale products with the backend data            | - Ensure that the correct products are being displayed            |

</details>

---

### Product Detail Page Testing

<details>
<summary>Expand test detail</summary>

| Test                        | Action                                                                                                             | Success Criteria                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image Display               | - Verify if the product image is displayed                                                                         | - The product image is prominently displayed and clearly shows the details of the product                                                                                     |
| Product Information         | - Check if product details such as price, name, SKU, and description are visible                                   | - Price, name, SKU, and description are accurately displayed for the selected product                                                                                         |
| Quantity Selector           | - Use the plus and minus buttons to adjust the quantity of the product                                             | - The quantity of the product can be adjusted using the plus and minus buttons                                                                                                |
| Add to Cart                 | - Click the "Add to Cart" button                                                                                   | - The product is added to the cart successfully                                                                                                                               |
| Cart Quantity Update        | - Add multiple quantities of the same product to the cart                                                          | - The cart updates with the correct quantity of the product                                                                                                                   |
| Product Variant Display     | - Verify if the product variants (sizes) are displayed                                                             | - Only the available sizes in stock are displayed as options for the product variant selector                                                                                 |
| Variant Selection           | - Select a different size from the product variants                                                                | - The product details (price, SKU, etc.) update to reflect the selected size                                                                                                  |
| Out of Stock Variant        | - Ensure that out-of-stock sizes are not selectable                                                                | - Out-of-stock sizes are either grayed out or not displayed in the product variant selector, preventing selection                                                             |
| Add to Cart from Variant    | - Select a size from the product variants and click "Add to Cart"                                                  | - The selected size is added to the cart with the correct quantity                                                                                                            |
| Cart Update from Variant    | - Add a product to the cart from the product detail page and verify cart contents after selecting a different size | - The product is correctly added to the cart, and the cart reflects the updated quantity or variant selection                                                                 |

</details>

---

### 💵 Payment & Confirmation Testing

<details>
<summary>Expand test detail</summary>

| Test                                           | Action                                                                                                           | Success Criteria                                                                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Delivery Address Display                       | - Verify if the selected delivery address is displayed                                                           | - The user's selected delivery address is shown on the checkout page                                                             |
| Change Address Button                          | - Click on the "Change Address" button                                                                           | - The user is able to select another address saved to their account                                                              |
| Card Details Input Fields                      | - Fill in the card number, expiry date, cardholder name, and security code fields                                | - User is able to input their card details correctly                                                                             |
| Order Summary Display                          | - Check if the order summary displays the product name, size, quantity, and price of the user's cart products    | - The order summary accurately reflects the items in the user's cart                                                             |
| Stripe PaymentIntent Creation                  | - Load the checkout page                                                                                         | - A PaymentIntent is created by Stripe when the checkout page is loaded                                                          |
| PaymentIntent Status Change                    | - Submit payment on the checkout page                                                                            | - The PaymentIntent status changes accordingly (e.g., from 'requires_payment_method' to 'processing' or 'succeeded')             |
| Webhook Reception                              | - Simulate a webhook sent by Stripe to the server                                                                | - The Django view receives the webhook successfully                                                                              |
| Order Creation in Database                     | - Confirm the user is redirected to the confirmation page after successful payment                               | - The confirmation page displays the order number                                                                                |
| Verify Order in Database                       | - Check the database to ensure the user's order has been created correctly based on the payment and cart details | - The user's order is stored accurately in the database, including product details, delivery address, payment status, etc.       |
| Error Handling for Card Decline                | - Attempt to submit payment with an invalid card                                                                 | - User receives an appropriate error message indicating the card was declined, and payment is not processed                      |
| Redirection to Login for Unauthenticated Users | - Attempt to access the checkout page without being logged in                                                    | - Unauthenticated users are redirected to the login page with a message prompting them to log in before proceeding with checkout |

</details>

---

### 🔒 Authorisation Testing

<details>
<summary>Expand test detail</summary>

| Test                                      | Action                                                                                                                            | Success Criteria                                                                                                                                                    |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account Page Access                       | - Attempt to access the account page without logging in                                                                           | - User is redirected to the login page with a message indicating the need to log in                                                                                 |
| Orders Page Access                        | - Attempt to access the orders page without logging in                                                                            | - User is redirected to the login page with a message indicating the need to log in                                                                                 |
| Addresses Page Access                     | - Attempt to access the addresses page without logging in                                                                         | - User is redirected to the login page with a message indicating the need to log in                                                                                 |
| Favorites Page Access                     | - Attempt to access the favorites page without logging in                                                                         | - User is redirected to the login page with a message indicating the need to log in                                                                                 |
| Unauthorized User Access                  | - Log in as a user and attempt to access another user's account page, orders page, addresses page, or favorites page              | - User is redirected to their own corresponding page with a message indicating they are not authorized to access another user's data                                |
| User-Specific Data Access                 | - Log in as a user and attempt to access another user's addresses, orders, or favorites data                                      | - User is able to access and view only their own addresses, orders, and favorites data; attempting to access another user's data results in an error or redirection |
| Checkout Page Access                      | - Attempt to proceed to checkout without being logged in                                                                          | - User is redirected to the login page with a message indicating the need to log in                                                                                 |
| Logged In User Checkout Access            | - Log in as a user and attempt to access the checkout page                                                                        | - User is able to proceed to the checkout page                                                                                                                      |
| Redirect to Previous Page After Login     | - Attempt to access a restricted page, then log in                                                                                | - User is redirected to the page they originally attempted to access after successfully logging in                                                                  |
| Logout and Session Clearing               | - Log out from the account                                                                                                        | - User's session is cleared, and attempts to access restricted pages or proceed to checkout result in redirection to the login page                                 |


</details>

---

### 🚦 Lighthouse Testing

<details>

- All pages were tested using Lighthouse with the primary goals of identifying performance and accessibility issues and ensuring adherance to best practices.
- The Lighthouse test results for each step of the `core` user flow are shown below:
<details>
<summary>Homepage</summary>

![Homepage Lighthouse test](/readme/Lighthouse-homepage.png)

</details>
<details>
<summary>Product Detail</summary>

![Flights Lighthouse test](/readme/Lighthouse-flights.png)

</details>
<details>
<summary>Shop Page</summary>

![Passengers Lighthouse test](/readme/Lighthouse-passengers.png)

</details>
<details>
<summary>Checkout</summary>

![Checkout Lighthouse test](/readme/Lighthouse-summary.png)

</details>

</details>

---

### 📱 Responsiveness Testing

<details>

- Testing for responsiveness was conducted using Chrome Dev Tools and ResponsivelyApp.
- The website was tested extensively on a range of emulated mobile, tablet and large format screen sizes in both portrait and landscape orientations.
<details>
<summary>Responsiveness test results</summary>

![Responsiveness testing with ResponsivelyApp](/readme/responsive-testing.png)

</details>

| Device             | iPhone SE   | iPhone X    | iPhone 12 Pro | iPhone 13 Pro Max | iPhone 14 Pro Max | iPad         | iPad Air     | iPad Pro      | Macbook Pro  |
| ------------------ | ----------- | ----------- | ------------- | ----------------- | ----------------- | ------------ | ------------ | ------------- | ------------ |
| **Resolution**     | **375x667** | **375x812** | **390x844**   | **414x76**        | **414x896**       | **768x1024** | **820x1180** | **1024x1366** | **1440x900** |
| Render             | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Layout             | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Functionality      | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Links              | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Images             | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Portrait/Landscape | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |

</details>

---

### ✅ Code Validation

<details>

- All HTML pages were checked with the [W3C Markup Validation Service](https://validator.w3.org/) with no major errors present. Errors were present for `htmx` and `alpine.js` related attributes, however these are valid and necessary for the functionality of the site.
- All JavaScript files were passed through [JSHint](https://jshint.com/) with no errors present.
- All custom coded Python files were formatted with a PEP8 complaint formatter - [Black](https://pypi.org/project/black/).

</details>

<br>
<br>
<br>
