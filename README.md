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








# Work in progress

# Bugs
- Poor performance - SQL query issue. Fixed with prefetch_related, 1600ms to 120ms improvement. Implement same fix site-wide to improve performance. 
- add address - duplicate form submission on refresh - fixed with redirect
- delete default address 
    - fixed by setting new default if current default address deleted. 
- Addresses being added every time order made
- Slow SQL queries
- Template inheritance from _head


Live site: https://flyux.carlmurray.design


### 👨‍💻 Development

<details>

- The development process was carried out using an Agile methodology with a focus on iterative development and continuous improvement.
- The project was managed using a GitHub Project board with user stories and tasks.
- User Stories were sized using T-shirt sizing (XS, S, M, L, XL) and prioritised based on the MoSCoW method (Must have, Should have, Could have, Won't have).

#### 📈 [Link to the GitHub Project board](https://github.com/users/CarlMurray/projects/4/views/2)

#### 👤 User Stories
1. As a customer, I want to be able to create a new account on the website so that I can save my shipping and billing information for future purchases. (Must have)
2. As a customer, I want to be able to browse products by categories (e.g., Men's Shoes, Women's Shoes) so that I can easily find what I'm looking for. (Should have)
3. As a customer, I want to be able to search for products by keywords so that I can quickly locate specific items. (Should have)
4. As a customer, I want to see detailed product information, including product descriptions, prices, available sizes, and customer reviews, so that I can make an informed purchasing decision. (Must have)
5. As a customer, I want to add products to my shopping cart and review the items in my cart before proceeding to checkout.
6. As a customer, I want to be able to select my preferred shipping method and enter my shipping address during the checkout process.
7. As a customer, I want to have multiple payment options (e.g., credit card, PayPal) when making a purchase. (Should have)
8. As a customer, I want to receive order confirmation emails with details of my purchase after completing a transaction. (Should have)
9. As a customer, I want to be able to view and track the status of my orders, including order history and estimated delivery dates. (Should have)
10. As a customer, I want to be able to leave reviews and ratings for products I've purchased to share my experiences with other users. (Could have)
11. As an admin, I want to be able to log in securely to the admin panel of the e-commerce platform to manage the website's content and functionality. (Must have)
12. As an admin, I want to add, edit, or remove product listings, including product details, images, and pricing, to keep the online store up-to-date. (Must have)
13. As an admin, I want to categorize products into different categories and subcategories to improve navigation for customers. (Should have)
14. As an admin, I want to review and moderate customer reviews and ratings to ensure the quality of user-generated content. (Must have - if reviews implemented)

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

---

<br>
<br>
<br>

---