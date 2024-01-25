# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger
import pandas as pd
# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다")

def main(request):
    return render(request, "main.html")

def burger_list(request):
    # burgers = Burger.objects.all()
    burgers = Burger.objects.all().values()
    data = pd.DataFrame(burgers)
    print(data)
    # print("전체 햄버거 목록:", burgers)

    context = {
        # "burgers": burgers,
        "burgers": data.to_html(classes="table table-dark table-striped", index=False, justify="match-parent")
    }

    return render(request, "burger_list.html", context)

def burger_search(request):
    keyword = request.GET.get("keyword")
    # print(keyword)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)

    else:
        burgers = Burger.objects.none()

    # print(burgers)
    context = {
        "burgers": burgers,
    }

    return render(request, "burger_search.html", context)
