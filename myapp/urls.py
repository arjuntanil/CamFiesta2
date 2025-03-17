from django.urls import path
from . import views
from .views import index
from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views 
from django.urls import path
from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),


  

   

    path('profile/', views.profile, name='profile'),  # Profile URL

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    path('product/<int:pk>/', views.product, name='product'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),  # Add this line for the search functionality
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart_item/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
    path('delete_cart_item/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    # path('order/<int:order_id>/', views.order_detail, name='order_detail'),

    path('order/<int:order_id>/', views.order_details, name='order_details'),

    path('order-history/', views.order_history, name='order_history'),

    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('download_invoice/<int:order_id>/', views.download_invoice, name='download_invoice'),

    path('profile/reset-password/', views.password_profile_reset, name='password_profile_reset'),
   
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

