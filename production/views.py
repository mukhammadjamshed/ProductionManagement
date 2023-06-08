from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, WarehouseQuantity


class ProductMaterialAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = []

        for product in products:
            product_data = {
                'product_name': product.name,
                'product_qty': product.quantity,
                'product_materials': []
            }

            for product_material in product.productmaterial_set.all():
                material_data = {
                    'material_name': product_material.raw_material.name,
                    'qty': 0,
                    'price': None,  # Set initial price as None
                    'warehouse_quantities': []
                }

                warehouse_quantities = WarehouseQuantity.objects.filter(raw_material=product_material.raw_material).order_by('price')
                remaining_qty = product_data['product_qty']
                for warehouse_quantity in warehouse_quantities:
                    if remaining_qty <= 0:
                        break
                    if warehouse_quantity.remainder > 0:
                        if warehouse_quantity.remainder >= remaining_qty:
                            material_data['qty'] += remaining_qty
                            remaining_qty = 0
                        else:
                            material_data['qty'] += warehouse_quantity.remainder
                            remaining_qty -= warehouse_quantity.remainder
                        warehouse_data = {
                            'warehouse_id': warehouse_quantity.warehouse.id,
                            'price': warehouse_quantity.price,
                            'qty': warehouse_quantity.remainder
                        }
                        material_data['warehouse_quantities'].append(warehouse_data)

                        # Update price if it exists in the database
                        if warehouse_quantity.price is not None:
                            material_data['price'] = warehouse_quantity.price

                product_data['product_materials'].append(material_data)

            data.append(product_data)

        return Response({'result': data})