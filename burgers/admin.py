from django.contrib import admin
from burgers.models import Burger

# 기초문법 정리, 함수 데코레이터 검색
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass
