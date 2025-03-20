from django.urls import path

from . import views
from .views import home, clothing_view, services, electronics_view, contact, upload_product, categorized_page, \
    add_to_cart, cart_view, checkout, checkout_success, \
    order_detail, starter, admin_login, admin_dashboard, delete_order, delete_contact, delete_product, manage_products, \
    customer_orders, contact_messages, upload_product_images, delete_contact_messages

# Import the categorized_page view

urlpatterns = [

    path('', home, name='home'),
    path('services/', services, name='services'),
    path('starter/', starter, name='starter'),
    path('clothing/', clothing_view, name='clothing'),
    path('electronics/',electronics_view , name='electronics'),
    path('contact/',contact , name='contact'),
    path('upload/', upload_product, name='upload_product'),
    path('categorized/', categorized_page, name='categorized_page'),  # Ensure this view exists
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout, name='checkout'),
    path('manage_products', manage_products, name='manage_products'),
    path('customer_orders', customer_orders, name='customer_orders'),
    path('contact_messages', contact_messages, name='contact_messages'),
    path('upload_product_images', upload_product_images, name='upload_product_images'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('checkout_success/', checkout_success, name='checkout_success'),  # Success page
    path('admin_login/', admin_login, name='admin_login'),  # Admin login URL
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
    path('delete_contact/<int:contact_id>/',delete_contact, name='delete_contact'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),  # Admin dashboard URL
    path('admin/product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),  # URL for deleting a product
    path('admin/delete-contact-message/<int:contact_id>/', delete_contact_messages, name='delete_contact_message'),

]