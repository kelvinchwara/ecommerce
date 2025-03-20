from django.contrib import admin
from django.template.defaulttags import csrf_token
from .models import Product, Cart, CartItem, Order, OrderItem, Contact
from django.utils.html import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'category', 'price', 'delete_button')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px;" />')
        return '-'
    image_tag.short_description = 'Image'

    def delete_button(self, obj):
        return mark_safe(f'<form action="{obj.id}/delete/" method="post" style="display:inline;">'
                         f'<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">'
                         f'<button type="submit" class="button">Delete</button>'
                         f'</form>')
    delete_button.short_description = 'Delete'

# Register the Product model with the ProductAdmin class
admin.site.register(Product, ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty forms

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username',)
    inlines = [OrderItemInline]  # Add inline editing for OrderItems

# Register other models
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)  # Register OrderItem if you want to manage it separately