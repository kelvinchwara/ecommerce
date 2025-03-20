from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView

from .forms import ProductForm, CheckoutForm, ContactForm, OrderForm, UploadImageForm
from .models import Product, Category,Cart, CartItem,Order , OrderItem ,Contact# Import your models
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages




def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, f"You've successfully deleted the product '{product.name}'.")
    return redirect('manage_products')  # Redirect to avoid resubmission
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
    return render(request, 'admin_login.html')

@login_required
def admin_dashboard(request):
    orders = Order.objects.prefetch_related('items').all()
    order_items = OrderItem.objects.all()
    contacts = Contact.objects.all()  # Fetch all contacts
    products = Product.objects.all()  # Fetch all products

    if request.method == 'POST':
        upload_image_form = UploadImageForm(request.POST, request.FILES)
        if upload_image_form.is_valid():
            upload_image_form.save()
            return redirect('admin_dashboard')  # Redirect to avoid resubmission
    else:
        upload_image_form = UploadImageForm()

    return render(request, 'admin_dashboard.html', {
        'orders': orders,
        'order_items': order_items,
        'contacts': contacts,
        'products': products,  # Pass products to the template
        'upload_image_form': upload_image_form,
    })
def home(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'index.html', {'products': products})

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categorized_page')  # Redirect to the categorized page
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})
def categorized_page(request):
    categories = Category.objects.all()
    return render(request, 'categorized_page.html', {'categories': categories})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart_view.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
@login_required

def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)


    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the order here
            order = Order.objects.create(
                user=request.user,
                name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                status='pending'
            )
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price_at_order=item.product.price,
                    cart_item=f"{item.quantity} of {item.product.name}"
                )
            # Clear the user's cart after processing the order
            user_cart.cartitem_set.all().delete()
            return redirect('/checkout_success')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form, 'cart_items': cart_items})
@login_required
def checkout_success(request):
    return render(request, 'checkout_success.html')


def upload_product_images(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # Add a success message
            messages.success(request, f"You've successfully uploaded a product to the '{product.category}' category.")
            return redirect('upload_product_images')  # Redirect to avoid resubmission
    else:
        form = ProductForm()

    return render(request, 'upload_product_images.html', {'form': form})
def customer_orders(request):
    orders = Order.objects.all()
    return render(request, 'customer_orders.html', {'orders': orders})

def contact_messages(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_messages.html', {'contacts': contacts})
def delete_contact_messages(request, contact_id):
    contact = get_object_or_404(id=contact_id)
    contact.delete()
    return redirect('contact_messages')  # Redirect to avoid resubmission


def manage_products(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_products')  # Redirect to avoid resubmission
    else:
        form = ProductForm()

    return render(request, 'manage_products.html', {'form': form, 'products': products})


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})


def contact(request):
    form= ContactForm(request.POST or None)
    success_message="Successfully sent your details. " if request.method == 'POST' and form.is_valid() else None
    if request.method == 'POST':
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        messages.success(request, "Your contact details have been submitted successfully.")
        return redirect('contact')  # Redirect to the same page or a success page

    else:

        return render(request, 'contact.html')






def services(request):
    return render( request, 'services.html')
def starter(request):
    return render(request, 'starter_page.html')
def electronics_view(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'electronics.html', {'products': products})

def clothing_view(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'clothing.html', {'products': products})
def order_detail(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=Order.objects.create(name=form.cleaned_data['full_name'])
            cart_items=request.session.get('cart_items', [])
            for item in cart_items:
                product = Product.objects.get(id=item.product.id)
                quantity=item.quantity
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

                request.session['cart_items']=[]
                return redirect('/checkout_success')
            else:
                form=OrderForm()
                return render(request,'checkout_success.html', {'form': form})
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, 'Order deleted successfully.')
    return redirect('admin_dashboard')  # Replace 'order_list' with the name of your order list view

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully.')
    return redirect('admin_dashboard')  # Replace 'contact_list' with the name of your contact list view

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')  # Redirect to the product list after deletion
    template_name = 'product_confirm_delete.html'
