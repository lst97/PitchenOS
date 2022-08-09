from rest_framework import status
from .serializers import CreateCategorySerializer, CategorySerializer, ProductSerializer, VariantSerializer, OptionSerializer
from .models import Category, Product, Variant, Option, init_db
from rest_framework.views import APIView
from rest_framework.response import Response

class InitDBView(APIView):
    def get(self, request, format=None):
        try:
            return Response(init_db(), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class DrinksView(APIView):
    def get(self, request, format=None):
        return Response(Product.objects.filter(category_id=1).values(), status=status.HTTP_200_OK)

class CategoryView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, format=None):
        return Response(Category.objects.all().values(), status=status.HTTP_200_OK)

class ProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        return Response(Product.objects.all().values(), status=status.HTTP_200_OK)

class VariantView(APIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

    def get(self, request, format=None):
        return Response(Variant.objects.all().values(), status=status.HTTP_200_OK)
    
class OptionView(APIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get(self, request, format=None):
        return Response(Option.objects.all().values(), status=status.HTTP_200_OK)
      

class CreateCategoryView(APIView):
    serializer_class = CreateCategorySerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        name = serializer.data.get('name')
        queryset = Category.objects.filter(name=name)

        if queryset.exists():
            return Response({'Bad Request': 'Name Already Exist'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            category = Category(name = name)
            category.save()
            return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)