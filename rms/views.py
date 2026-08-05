from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Table, Menu, OrderMenu, Order
from rest_framework.generics import GenericAPIView
from rest_framework import generics, mixins
from .serializers import CategorySerializer, TableSerializer, MenuSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CategoryPagination
from .filter import MenuFilter

# ModelViewset
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def destroy(self, request, id):
        category = get_object_or_404(Category, id=id)
        item = OrderMenu.objects.filter(menu_category=category).count()
        if item > 0:
            return Response({"message": "Data cannot be deleted"})
        category.delete()
        return Response({"message": "Data has been deleted"})


class TableListModelViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class MenuModelViewSet(ModelViewSet):
    queryset = Menu.objects.all().prefetch_related("category")
    serializer_class = MenuSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = MenuFilter
    # filterset_fields = ["category"]
    search_fields = ["name", "category__name"]


# class CategoryDetailModelViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
# # Viewset
# class CategoryView(ViewSet):
#     def list(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Category created successfully", "data": serializer.data}
#             )
#         return Response({"message": "Couldn't create category"})


# class CategoryDetail(ViewSet):
#     def retrieve(self, request, id):
#         category = get_object_or_404(Category, id=id)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def update(self, request, id):
#         category = get_object_or_404(Category, id=id)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Category updated successfully", "data": serializer.data}
#             )
#         return Response(
#             {"message": "Data cannot be updated", "errors": serializer.errors},
#         )

#     def destroy(self, request, id):
#         category = get_object_or_404(Category, id=id)
#         item = OrderMenu.objects.filter(menu__category=category).count()
#         if item > 0:
#             return Response(
#                 {"message": "Cannot be deleted because this category is in use."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#             category.delete()

#         return Response(
#             {"message": "Category deleted successfully"},
#         )


# class TableList(ViewSet):
#     def list(self, request):
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = TableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Table created successfully", "data": serializer.data}
#             )
#         return Response({"message": "Cannot create Table"})


# class TableDetail(ViewSet):
#     def retrieve(self, request, id):
#         table = get_object_or_404(Table, id=id)
#         serializer = TableSerializer(table)
#         return Response(serializer.data)

#     def update(self, request, id):
#         serializer = TableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Table updated successfully", "data": serializer.data}
#             )
#         return Response({"message": "Couldn't update the table"})

#     def delete(self, request, id):
#         table = get_object_or_404(Table, id=id)
#         table.delete()
#         return Response({"message": "Table deleted successfully"})


# Create your views here.
# Serialize: converting queryset to json format
# Manual Serializer
# data = Category.objects.all()
#     category = list(data.values())
#     # print(category)


# @api_view(["GET", "POST"])
# def category_list(request):
#     category = Category.objects.all()
#     if request.method == "GET":
#         serializer = CategorySerializer(category, many=True)  # serialization
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = CategorySerializer(data=request.data)  # deserialization
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({"message": "List Created.", "data": serializer.data})
#         return Response(serializer.errors, status=400)


# @api_view(["GET", "DELETE", "PUT", "PATCH"])
# def category_detail(request, id):
#     category = get_object_or_404(Category, id=id)
#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         item = OrderMenu.objects.filter(menu__category=category).count()
#         if item > 0:
#             return Response(
#                 {
#                     "message": "Data cannot be deleted. Protected Foreign key in OrderMenu"
#                 }
#             )
#         category.delete()
#         return Response({"message": "Data has been deleted"})
#     elif request.method == "PATCH":
#         serializer = CategorySerializer(category, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"data": serializer.data, "message": "Items updated successfully"}
#             )
#         return Response(serializer.errors, status=400)


# @api_view(["GET", "POST"])
# def table_list(request):
#     tables = Table.objects.all()
#     if request.method == "GET":
#         serializer = TableSerializer(tables, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = TableSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(
#                 {"message": "Table created successfully", "data": serializer.data}
#             )
#         return Response(serializer.errors, status=400)


# @api_view(["GET", "PATCH", "DELETE"])
# def table_detail(request, id):
#     table = get_object_or_404(Table, id=id)
#     if request.method == "GET":
#         serializer = TableSerializer(table)
#         return Response(serializer.data)
#     elif request.method == "PATCH":
#         serializer = TableSerializer(table, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Table updated successfully", "data": serializer.data}
#             )
#         return Response(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         table.delete()
#         return Response(
#             {"message": "Table deleted successfully", "data": serializer.data}
#         )


@api_view(["GET", "POST"])
def menu_list(request):
    if request.method == "GET":
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MenuSerializer(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class based
# class CategoryView(APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Created successfully", "data": serializer.data})


# class CategoryDetail(APIView):
#     def get_object(self, id):
#         return get_object_or_404(Category, id=id)

#     def get(self, request, id):
#         category = self.get_object(id)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def delete(self, request, id):
#         category = self.get_object(id)
#         item = OrderMenu.objects.filter(menu__category=category).count()
#         if item > 0:
#             return Response(
#                 {
#                     "message": "Category cannot be deletec, Protected foreign key in ordermenu"
#                 }
#             )
#         category.delete()
#         return Response({"message": "Category deleted successfully"})

#     def put(self, request, id):
#         category = self.get_object(id)
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Updated successfully", "data": serializer.data})


# class TableList(APIView):
#     def get(self, request):
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TableSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             {"message": "Table Created successfully", "data": serializer.data}
#         )


# class TableDetail(APIView):
#     def get_object(self, id):
#         return get_object_or_404(Table, id=id)

#     def get(self, request, id):
#         table = self.get_object(id)
#         serializer = TableSerializer(table)
#         return Response(serializer.data)

#     def delete(self, request, id):
#         table = self.get_object(id)
#         table.delete()
#         return Response({"message": "Table deleted successfully"})

#     def patch(self, request, id):
#         table = self.get_object(id)
#         serializer = TableSerializer(table, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             {"message": "Table updated successfully", "data": serializer.data}
#         )


# Generic Class
# class CategoryView(GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get(self, request):
#         category = self.get_queryset()
#         serializer = self.serializer_class(category, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         seralizer = self.serializer_class(data=request.data)
#         seralizer.is_valid(raise_exception=True)
#         seralizer.save()
#         return Response(
#             {"message": "Category created successfully", "data": seralizer.data}
#         )


# class CategoryDetail(GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = "id"

#     def get(self, request, id):
#         category = self.get_object()
#         serializer = self.serializer_class(category)
#         return Response(serializer.data)

#     def delete(self, request, id):
#         category = self.get_object()
#         category.delete()
#         return Response({"message": "Deleted ✅"})

#     def put(self, request, id):
#         category = self.get_object()
#         serializer = self.serializer_class(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Updated successfully ✅"})


# Mixins
# class CategoryView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get(self, request):
#         return self.list(self, request)

#     def post(self, request):
#         return self.create(self, request)


# class CategoryDetail(
#     GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = "id"

#     def get(self, request, id):
#         return self.list(self, request, id)

#     def put(self, request, id):
#         return self.update(self, request, id)

#     def delete(self, request, id):
#         category = self.get_object()
#         item = OrderMenu.objects.filter(menu__category=category).count()
#         if item > 0:
#             return Response(
#                 {"message": "Cannot be deleted"}, status=status.HTTP_404_BAD_REQUEST
#             )
#         return self.destroy(self, request, id,{"message":"Category deleted successfully"})


# class TableList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class TableDetail(GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
#     lookup_field ="id"
#     def get(self, request, id):
#         return self.list(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)

#     def patch(self, request, id):
#         return self.partial_update(request, id)
