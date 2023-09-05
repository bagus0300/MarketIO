import os
from core.models import ProductImage
from django.core.files import File


def run():
    """
    For bulk uploading product images.
    Specify local directory where images to be uploaded 
    are stored in product_imgs_dir.
    """
    product_imgs_dir = "product_imgs/"
    for img in os.listdir(product_imgs_dir):
        img_path = os.path.join(product_imgs_dir, img)

        with open(img_path, "rb") as f:
            django_file = File(f)
            product_img = ProductImage(image=django_file)
            product_img.save()
            print(f"ProductImage {product_img.id} saved.")

