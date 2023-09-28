# laced-pp5
Django-based eCommerce site

# Work in progress

# Bugs
- Poor performance - SQL query issue. Fixed with prefetch_related, 1600ms to 120ms improvement. Implement same fix site-wide to improve performance. 
- add address - duplicate form submission on refresh - fixed with redirect