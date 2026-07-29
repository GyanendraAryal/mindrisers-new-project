from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Table, Menu, OrderMenu
from .serializers import CategorySerializer, TableSerializer, MenuSerializer

# Create your views here.
# Serialize: converting queryset to json format
# Manual Serializer
# data = Category.objects.all()
#     category = list(data.values())
#     # print(category)


@api_view(["GET", "POST"])
def category_list(request):
    category = Category.objects.all()
    if request.method == "GET":
        serializer = CategorySerializer(category, many=True)  # serialization
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)  # deserialization
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "List Created.", "data": serializer.data})


@api_view(["GET", "DELETE", "PUT", "PATCH"])
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "DELETE":
        item = OrderMenu.objects.filter(menu__category=category).count()
        if item > 0:
            return Response(
                {
                    "message": "Data cannot be deleted. Protected Foreign key in OrderMenu"
                }
            )
        category.delete()
        return Response({"message": "Data has been deleted"})
    elif request.method == "PATCH":
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data, "message": "Items updated successfully"}
            )
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def table_list(request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def menu_list(request):
    if request.method == "GET":
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
