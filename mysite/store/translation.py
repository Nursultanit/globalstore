from .models import Product
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')