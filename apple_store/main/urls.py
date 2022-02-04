from django.urls import path
from .views import *


urlpatterns = [
    path('main/category', MainCategoryView.as_view({'get': 'list'})),
    path('main/product/create', MainProductView.as_view({'post':'create'})),
    path('main/product/list', MainProductView.as_view({'get':'list'})),
    path('main/product/crud/<int:pk>', ProductCRUDView.as_view()),
    path('main/card/crud/<int:pk>', CardCRUDView.as_view()),
    path('main/card/list', MainCardView.as_view({'get': 'list'})),
    path('main/card/create', MainCardView.as_view({'post':'create'})),
]
