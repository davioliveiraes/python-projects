import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product


def products_list(request):
   products = Product.objects.all()
   total_items = products.count()
   total_value = sum(p.total_price for p in products)
   purchased_items = products.filter(purchased=True).count()

   context = {
      'products': products,
      'total_items': total_items,
      'total_value': total_value,
      'purchased_items': purchased_items,
   }
   
   return render(request, 'products/list.html', context)

@csrf_exempt
@require_POST
def add_product(request):
   data = json.loads(request.body)
   product = Product.objects.create(
      name=data['name'],
      price=float(data['price']),
      quantity=int(data.get('quantity', 1))
   )
   return JsonResponse({
      'success': True,
      'product': {
         'id': product.id, # type: ignore
         'name': product.name,
         'price': float(product.price),
         'quantity': product.quantity,
         'total_price': float(product.total_price),
         'purchased': product.purchased
      }
   })

@csrf_exempt
@require_POST
def toggle_purchased(request, product_id):
   product = get_object_or_404(Product, id=product_id)
   product.purchased = not product.purchased
   product.save()
   return JsonResponse({
      'success': True,
      'purchased': product.purchased
   })

@csrf_exempt
@require_POST
def delete_product(request, product_id):
   product = get_object_or_404(Product, id=product_id)
   product.delete()
   return JsonResponse({'success': True})

@csrf_exempt
@require_POST
def update_quantity(request, product_id):
   data = json.loads(request.body)
   product = get_object_or_404(Product, id=product_id)
   product.quantity = int(data['quantity'])
   product.save()
   return JsonResponse({
      'success': True,
      'total_price': float(product.total_price)
   })