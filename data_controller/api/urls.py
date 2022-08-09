from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('fetch-category/', CategoryView.as_view()),
    path('fetch-product/', ProductView.as_view()),
    path('fetch-product-drinks/', DrinksView.as_view()),
    path('fetch-product-breakfasts/', BreakfastsView.as_view()),
    path('fetch-product-asians/', AsiansView.as_view()),
    path('fetch-product-kids/', KidsView.as_view()),
    path('fetch-product-snacks/', SnacksView.as_view()),
    path('fetch-product-desserts/', DessertsView.as_view()),
    path('fetch-variant/', VariantView.as_view()),
    path('fetch-option/', OptionView.as_view()),
    path('initdb/', InitDBView.as_view())
]