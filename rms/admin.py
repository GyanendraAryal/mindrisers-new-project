from django.contrib import admin
from .models import Category, Menu, Table, Order, OrderMenu


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("id",)


admin.site.register(Category, CategoryAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    search_fields = ("name",)
    list_filter = ("category", "price")

admin.site.register(Menu, MenuAdmin)



class TableAdmin(admin.ModelAdmin):
    list_display =('id',)
    search_fields = ('id',)
admin.site.register(Table,TableAdmin)

class OrderMenuInline(admin.TabularInline):
    model = OrderMenu
    # exclude = 0

class OrderAdmin(admin.ModelAdmin):
    list_display =('id','user','total_price','status')
    inlines = [OrderMenuInline]
    ordering = ('id',)
admin.site.register(Order,OrderAdmin)

admin.site.register(OrderMenu)
