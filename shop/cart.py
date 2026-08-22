from .models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'id': product_id,
                'name': product.name,
                'price': float(product.price),
                'quantity': quantity,
                'image_url': product.image.url if product.image else '',
            }
        else:
            self.cart[product_id]['quantity'] += quantity
            if 'image_url' not in self.cart[product_id] or not self.cart[product_id]['image_url']:
                self.cart[product_id]['image_url'] = product.image.url if product.image else ''

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def items(self):
        items_list = []
        for item in self.cart.values():
            item_copy = dict(item)
            item_copy['total_price'] = item_copy['price'] * item_copy['quantity']
            items_list.append(item_copy)
        return items_list

    def total(self):
        return sum(
            item['price'] * item['quantity']
            for item in self.cart.values()
        )
    
    def clear(self):
        if 'cart' in self.session:
            del self.session['cart']
            self.save()