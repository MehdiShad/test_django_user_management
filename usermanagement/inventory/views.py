from django.shortcuts import render
from rest_framework.views import APIView
from usermanagement.inventory.models import Product
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
# from rest_framework.permissions import BasePermission
# from usermanagement.inventory.apps import CAN_ADD_NEW_PRODUCT_API
# from rest_framework.response import Response



@login_required
@permission_required(
    {("product.add_product"), ("product.can_add_new_product")}
)
def create_product(request):
    if request.method == "POST":
        name = request.body.get('name')
        slug = request.body.get('slug')
        Product.objects.create(name=name, slug=slug)


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/books')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class CreateProduct(UserAccessMixin, APIView):
    create_product = Product.objects.create(name="test", slug='slug')



# class CanAddNewProductAPIPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.has_perm(CAN_ADD_NEW_PRODUCT_API)
#
# class YourAPIView(APIView):
#     permission_classes = [CanAddNewProductAPIPermission]
#
#     def post(self, request, *args, **kwargs):
#         # Your API logic for adding a new product
#         return Response({'message': 'Product added successfully!'})