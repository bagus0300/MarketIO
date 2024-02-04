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

## Shop Page
- The Shop page, accessed from the top navigation, shows all products.

## Product Detail Page
- Each product has a product detail page with the product image, price and description.
- Users can select a product variant, choose a quantity and add to cart.
- Only variants which are in stock are shown on the page. 
- When the Add to Cart button is pressed, an AJAX request is sent to a Django view which updates the user's cart.





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


## Roadmap
The site has been delivered in its current state as an MVP and there is still much work to do to improve the UX and functionality of the site, including:
- Product search and filters
- Discount code functionality
- Choice of shipping methods
- Contact page

# Business Model
- Laced is an online eCommerce store where customers can purchase footware online and have it delivered to them.
- All footware designs are AI generated using Leonardo.ai image generation, offering unique and differentiated footware designs.


# Marketing

## SEO
- Keywords such as "performance", "agility" and speed were included in the product descriptions to boost search engine ranking.
- A meta description was added to all products and main pages of the site for SEO purposes.
- There is a significant amount of work involved in renaming all product images and adding alt text to improve SEO, and these items were considered outside of the scope of this project.







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