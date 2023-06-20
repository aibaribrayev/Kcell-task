from django.contrib import admin
from django.utils.text import slugify

from .models import (
    Product,
    OrderItem,
    Order,
    ColourVariation,
    SizeVariation,
    Address,
    Payment,
    Category,
    StripePayment,
)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)  # Make slug field read-only

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            slug = slugify(obj.title)
            num = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f'{slug}-{num}'
                num += 1
            obj.slug = slug
        super().save_model(request, obj, form, change)


admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(SizeVariation)
admin.site.register(StripePayment)
admin.site.register(ColourVariation)
