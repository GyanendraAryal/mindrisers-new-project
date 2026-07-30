from django.urls import path
from . import views

urlpatterns = [
    # path("category/", views.category_list),
    path("category/", views.CategoryView.as_view()),
    path("category/<int:id>/", views.CategoryDetail.as_view()),
    path("tables/", views.TableList.as_view()),
    path("tables/<int:id>/", views.TableDetail.as_view()),
    # path("menus/", views.menu_list),
]
