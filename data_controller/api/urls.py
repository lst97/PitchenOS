from django.urls import path
from .views import CategoryView, DrinksView, InitDBView, OptionView, ProductView, VariantView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('fetch-category/', CategoryView.as_view()),
    path('fetch-product/', ProductView.as_view()),
    path('fetch-product-drinks/', DrinksView.as_view()),
    path('fetch-variant/', VariantView.as_view()),
    path('fetch-option/', OptionView.as_view()),
    path('initdb/', InitDBView.as_view())
]