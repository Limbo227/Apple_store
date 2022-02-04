from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apple_store import settings
import braintree
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

class MainCategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainCategorySerializers
    queryset = Category.objects.all()


class MainProductView(viewsets.ModelViewSet):
    serializer_class = MainProductSerializers
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated,)


class MainCardView(viewsets.ModelViewSet):
    serializer_class = MainCardSerializers
    queryset = Card.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated,)



class CardCRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MainCardSerializers
    queryset = Card.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated,)



class ProductCRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MainProductSerializers
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated,)


@login_required
def checkout_page(request):
    # generate all other required data that you may need on the #checkout page and add them to context.

    if settings.BRAINTREE_PRODUCTION:
        braintree_env = braintree.Environment.Production
    else:
        braintree_env = braintree.Environment.Sandbox

    # Configure Braintree
    braintree.Configuration.configure(
        braintree_env,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY,
    )

    try:
        braintree_client_token = braintree.ClientToken.generate({"customer_id": User.id})
    except:
        braintree_client_token = braintree.ClientToken.generate({})

    context = {'braintree_client_token': braintree_client_token}
    return render(request, 'checkout.html', context)


@login_required
def payment(request):
    nonce_from_the_client = request.POST['paymentMethodNonce']
    customer_kwargs = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
    }
    customer_create = braintree.Customer.create(customer_kwargs)
    customer_id = customer_create.customer.id
    result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    print(result)
    return HttpResponse('Ok')