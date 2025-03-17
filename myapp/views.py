from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from django.shortcuts import render
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from .models import Product, Category 
from .models import Product, Review

from .models import Product, Review
from .forms import ReviewForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from django.shortcuts import render, redirect

from .models import Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Review

from django.db.models import Q
from functools import reduce
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, CartItem, Order, OrderItem
from django.shortcuts import get_object_or_404, redirect

from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, CartItem, Order, OrderItem
import re
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Cart, Order, OrderItem, Profile
from django.shortcuts import get_object_or_404, redirect, render

from .models import Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from myapp.models import Cart, Order, OrderItem, Product
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from .models import Order

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors


from reportlab.lib.units import inch

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

from django.shortcuts import render, redirect
from django.http import Http404
from .models import Product, Review

from django.shortcuts import render, redirect
from django.http import Http404
from .models import Product, Review

from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required


from django.shortcuts import redirect

# .......................................

def product(request, pk):
    
    product = Product.objects.filter(id=pk).first()

    if not product:
        
        return redirect('product_list')  
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            review = form.save(commit=False)
            review.product = product 
            review.user = request.user 
            review.save()
            return redirect('product', pk=product.id)  
    else:
        form = ReviewForm()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
        'form': form,  
    })


def index(request):
    return render(request, 'register.html')

def home(request):
    selected_category = request.GET.get('category')
    
    if selected_category and selected_category != 'all':
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    })




def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        # Password validation: At least 4 characters, and at least 2 digits
        if len(password) < 4:
            messages.error(request, "Password must be at least 4 characters long.")
            return render(request, 'register.html')

        if len(re.findall(r'\d', password)) < 2:  # Count digits in password
            messages.error(request, "Password must contain at least 2 digits.")
            return render(request, 'register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'register.html') 

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return render(request, 'register.html')  

        # Create the user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')  

    return render(request, 'register.html')




def login_view(request):
    next_url = request.GET.get('next')  # Capture the 'next' parameter
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")

            if user.is_staff:
                return redirect('/admin/')
            else:
                return redirect(next_url) if next_url else redirect('home')
        else:
            messages.error(request, "Incorrect username or password")

    return render(request, 'login.html', {'next': next_url})




def logout_view(request):

    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
    




@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    # Get the product object
    product = get_object_or_404(Product, id=product_id)
    
    # Get or create a cart for the logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    # Get or create a cart item for the product in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        cart_item.quantity = 1
        messages.success(request, f"{product.name} added to your cart.")
    else:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            messages.success(request, f"Quantity of {product.name} increased in your cart.")
        else:
            messages.warning(request, f"Cannot add more than {product.stock} of {product.name}.")
    
    cart_item.save()
    return redirect('view_cart')



@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user, completed=False).first()
    
  
    if not cart:
        return render(request, 'cart.html', {'message': "Your cart is empty."})

    cart_items = cart.items.all()
    total_price = 0
    
    
    cart_items_with_total = []
    for item in cart_items:
        item_total = item.quantity * item.product.price
        cart_items_with_total.append({
            'item': item,
            'item_total': item_total
        })
        total_price += item_total

    return render(request, 'cart.html', {
        'cart_items_with_total': cart_items_with_total,
        'total_price': total_price
    })


@login_required
def update_cart_item(request, product_id):
    if request.method == "POST":
        
        quantity = int(request.POST.get("quantity", 1))
        cart = Cart.objects.filter(user=request.user, completed=False).first()

        if not cart:
            messages.info(request, "Your cart is empty.")
            return redirect('home')

        
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

        if cart_item:
            product = cart_item.product
           
            if quantity <= 0:
                cart_item.delete()  
                messages.success(request, f"{product.name} removed from your cart.")
            elif quantity <= product.stock:
                cart_item.quantity = quantity
                cart_item.save()
                messages.success(request, f"Quantity of {product.name} updated to {quantity}.")
            else:
                messages.warning(request, f"Cannot add more than {product.stock} of {product.name}.")
        else:
            messages.warning(request, "Product not found in your cart.")

    return redirect('view_cart')



@login_required
def delete_cart_item(request, product_id):
    cart = Cart.objects.filter(user=request.user, completed=False).first()

    if not cart:
        messages.info(request, "Your cart is empty.")
        return redirect('home')

    cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

    if cart_item:
        cart_item.delete()
        messages.success(request, f"{cart_item.product.name} has been removed from your cart.")
    else:
        messages.warning(request, "Product not found in your cart.")

    return redirect('view_cart')

def search(request):
    query = request.GET.get('query', '')
    products = []
    similar_products = []

    if query:
       
        query_words = query.split()
        filter_conditions = [Q(name__icontains=word) | Q(description__icontains=word) for word in query_words]
        final_query = reduce(lambda x, y: x | y, filter_conditions)
        products = Product.objects.filter(final_query)
        similar_products = Product.objects.filter(final_query).exclude(id__in=[product.id for product in products])

    return render(request, 'search_results.html', {
        'query': query,
        'products': products,
        'similar_products': similar_products
    })
   
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user:
        review.delete()  
        return redirect('product_detail', product_id=review.product.id)  
    else:
        return redirect('product_detail', product_id=review.product.id) 

@login_required
def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Automatically set the user
            review = form.save(user=request.user)
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {'form': form, 'product': product})

@login_required
def profile(request):
    if request.method == 'POST':
        # Get the submitted form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        # Update the user's basic information
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()  # Save the basic user info

        # Update or create the user's profile fields (phone number and address)
        profile = user.profile
        profile.phone_number = phone_number
        profile.address = address
        profile.save()  # Save the updated profile info

        # Flash a success message to be used by the JavaScript alert
        messages.success(request, 'Your profile has been updated successfully!')

        # Redirect to the home page after successful profile update
        return redirect('home')  # Change this to redirect to 'home' instead of 'profile'

    return render(request, 'profile.html')





@login_required
def confirm_order(request):
    cart = Cart.objects.filter(user=request.user, completed=False).first()

    if not cart or not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    for item in cart.items.all():
        if item.quantity > item.product.stock:
            messages.error(
                request,
                f"Insufficient stock for {item.product.name}. Available stock: {item.product.stock}."
            )
            return redirect('view_cart')

    total_price = sum(item.quantity * item.product.price for item in cart.items.all())
    address = request.user.profile.address if hasattr(request.user, 'profile') else None

    if not address:
        messages.error(request, "Address is required to place an order.")
        return redirect('profile')

    order = Order.objects.create(user=request.user, total_price=total_price, address=address)

    for item in cart.items.all():
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        item.product.stock -= item.quantity
        item.product.save()

    cart.completed = True
    cart.save()

    messages.success(request, "Order has been successfully placed!")
    
    # Redirecting to the correct order details page
    return redirect('order_details', order_id=order.id)





@login_required
def order_details(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    total_amount = sum(item.price * item.quantity for item in order.items.all())

    profile = request.user.profile


    return render(request, 'order_detail.html', {
    'order': order,
    'total_amount': total_amount,
    'profile': profile,
})




@login_required
def order_history(request):
    # Fetch all orders of the logged-in user, ordered by the date of creation
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Structure data to include details for each order item
    order_details = []
    for order in orders:
        items = order.items.all()
        item_details = []
        order_total_price = 0  # Initialize total price for the order
        
        for item in items:
            # Calculate total price for the item (price * quantity)
            item_total = item.price * item.quantity
            item_details.append({
                'name': item.product.name,
                'quantity': item.quantity,
                'price': item.price,
                'total_price': item_total  # Add total price for this item
            })
            
            # Add item total price to order total price
            order_total_price += item_total
        
        order_details.append({
            'order_id': order.id,
            'total_price': order_total_price,  # Update with the calculated order total price
            'order_date': order.created_at,
            'status': order.status,  # You can add the status of the order if it's implemented
            'items': item_details
        })

    return render(request, 'order_history.html', {'order_details': order_details})





def product_detail(request, product_id):
    try:
        # Fetch the product object directly
        product = Product.objects.get(id=product_id)

        # Fetch reviews for the product
        reviews = Review.objects.filter(product=product)

    except Product.DoesNotExist:
        # If the product doesn't exist, raise a 404 error
        raise Http404("Product not found.")

    # Handle POST request to submit a review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Automatically set the user and product when saving the review
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)  # Redirect to the same product detail page

    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })



def product_detail(request, product_id):
    try:
        # Fetch the product object directly
        product = Product.objects.get(id=product_id)

        # Fetch reviews for the product
        reviews = Review.objects.filter(product=product)

    except Product.DoesNotExist:
        # If the product doesn't exist, raise a 404 error
        raise Http404("Product not found.")

    # Handle POST request to submit a review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Automatically set the user and product when saving the review
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)  # Redirect to the same product detail page

    else:
        form = ReviewForm()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })




def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        try:
            user = User.objects.get(username=username, email=email)
            if user.profile.phone_number == phone_number:
                # Store user ID in session for verification in the reset_password view
                request.session['reset_user_id'] = user.id
                return redirect('reset_password')
            else:
                messages.error(request, "Incorrect entered datas. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "Incorrect entered datas. Please try again.")
    
    return render(request, 'forgot_password.html')




def reset_password(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        messages.error(request, "Session expired. Please try again.")
        return redirect('forgot_password')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            try:
                user = User.objects.get(id=user_id)
                user.password = make_password(new_password)
                user.save()
                
                update_session_auth_hash(request, user)  # Keeps the user logged in
                messages.success(request, "Password reset successfully. Please log in.")
                del request.session['reset_user_id']  # Clear session after success
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, "User not found.")
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'reset_password.html')





def sanitize_text(text):
    # Ensure only ASCII characters are allowed
    return re.sub(r'[^\x00-\x7F]+', '', text)

def download_invoice(request, order_id):
    # Retrieve the order by ID
    order = Order.objects.get(id=order_id)

    # Sanitize data to avoid non-ASCII characters
    customer_name = sanitize_text(f"{order.user.first_name} {order.user.last_name}")
    order_address = sanitize_text(order.address)
    order_status = sanitize_text(order.status)

    # Create the HTTP response with PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Invoice_Order_{order_id}.pdf"'

    # Set up canvas for PDF
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # Add CamFiesta header
    p.setFont("Helvetica-Bold", 26)
    p.setFillColor(colors.black)
    p.drawCentredString(width / 2, height - 50, "CamFiesta")

    # Invoice title
    p.setFont("Helvetica-Bold", 20)
    p.setFillColor(colors.black)
    p.drawCentredString(width / 2, height - 90, "Invoice")

    # Order Details
    p.setFont("Helvetica", 12)
    y_position = height - 130
    details = [
        f"Order ID: {order.id}",
        f"Customer Name: {customer_name}",
        f"Order Date: {order.created_at.strftime('%Y-%m-%d')}",
        f"Total Price: ${order.total_price:.2f}",
        f"Status: {order_status}"
    ]
    for detail in details:
        p.drawString(100, y_position, detail)
        y_position -= 20

    # Shipping Address
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y_position - 20, "Shipping Address:")
    p.setFont("Helvetica", 12)
    y_position -= 40
    p.drawString(120, y_position, order_address)

    # Order Items
    y_position -= 40
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y_position, "Items:")
    p.setFont("Helvetica", 12)
    y_position -= 20
    for item in order.items.all():
        # Sanitize item data
        item_name = sanitize_text(item.product.name)
        item_text = f"{item.quantity} x {item_name} - ${item.price:.2f} each"
        p.drawString(120, y_position, item_text)
        y_position -= 20

    # Footer message
    p.setFont("Helvetica-Oblique", 12)
    p.drawCentredString(width / 2, 40, "Thank you for choosing us.")

    # Save and return the PDF
    p.showPage()
    p.save()

    return response


from django.contrib.auth import update_session_auth_hash

@login_required
def password_profile_reset(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password and new_password == confirm_password:
            # Update the password for the logged-in user
            user = request.user
            user.set_password(new_password)  # Securely set the new password
            user.save()

            # Keep the user logged in after password change
            update_session_auth_hash(request, user)

            # Display a success message
            messages.success(request, "Your password has been updated successfully.")

            # Redirect to the profile page
            return redirect('profile')  # Replace 'profile' with your actual profile page URL name
        else:
            messages.error(request, "Passwords do not match. Please try again.")

    return render(request, 'password_profile_reset.html')
