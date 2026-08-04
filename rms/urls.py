from django.urls import path
from .views import *
from rest_framework import routers

route = routers.SimpleRouter()
route.register("category", CategoryModelViewSet, basename="category")
route.register("tables",TableListModelViewSet,basename="table")


urlpatterns = [
    # path("category/", views.category_list),
    # path(
    #     "category/",
    #     CategoryModelViewSet.as_view({"get": "list", "post": "create"}),
    # ),
    # path("category/", views.CategoryView.as_view({"get": "list", "post": "create"})),
    # path(
    #     "category/<int:id>/",
    #     views.CategoryDetail.as_view(
    #         {"get": "retrieve", "put": "update", "delete": "delete"}
    #     ),
    # ),
    # path("tables/", views.TableList.as_view({"get": "list", "post": "create"})),
    # path(
    #     "tables/<int:id>/",
    #     views.TableDetail.as_view(
    #         {"get": "retrieve", "put": "update", "delete": "delete"}
    #     ),
    # ),
    # path("menus/", views.menu_list),
] + route.urls
