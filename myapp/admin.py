from django.contrib import admin
from .models import Product, Comment, ProductImage

from django.contrib import admin
from .models import Product, Category, Review


from django.contrib import admin
from .models import Product, Comment, ProductImage, Category

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty rows

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price', 'status', 'update_status')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    inlines = [OrderItemInline]

    def update_status(self, obj):
        # Add a dropdown to update the status directly from the list view
        return f"{obj.get_status_display()}"
    update_status.short_description = 'Order Status'

    actions = ['mark_as_dispatched', 'mark_as_out_for_delivery', 'mark_as_delivered']

    def mark_as_dispatched(self, request, queryset):
        queryset.update(status='Dispatched')
    mark_as_dispatched.short_description = 'Mark selected orders as Dispatched'

    def mark_as_out_for_delivery(self, request, queryset):
        queryset.update(status='Out for Delivery')
    mark_as_out_for_delivery.short_description = 'Mark selected orders as Out for Delivery'

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='Delivered')
    mark_as_delivered.short_description = 'Mark selected orders as Delivered'

admin.site.register(Order, OrderAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Shows one extra blank image field for adding a new image

# Inline class for managing comments
"""class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Shows one extra blank comment field for adding a new comment
    readonly_fields = ['created_at']  # Make created_at read-only"""

# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category'] 
    search_fields = ['name', 'description']  # Enable search functionality
    list_filter = ['category']  # Enable filtering by category
    inlines = [ProductImageInline]  # Add the inlines for images and comments , , [CommentInline]

# Register your models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)  # Register the Category model to manage categories in the admin panel
admin.site.register(Review)


