from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

first_name = "Artem" 
last_name = "Zhilkin"
Email = "matriza1996@gmail.com"
Patronymic = "Aleksandrovich"
Phone = "8 978 577 51 55"


item = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = """<h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Правка номер один Жилкин А.А </i>"""
    return HttpResponse(text)
def about(request):
    text = f"""<h1>"Изучаем django"</h1> 
                <div>"Имя:{first_name} "<div>
                <div>"Отчество: {Patronymic}"</div>
                <div>"Фамилия: {last_name}"</div>
                <div>"Телефон:{Phone}"</div>
                <div>"Email:{Email}"</div>"""
    return HttpResponse(text)
def startItems(request):
    x = []
    text1 = []
    for i in item:
        GetIdForUrl = i.get("id")
        text1.append("<div>")
        text1.append(f"<a href=http://127.0.0.1:8000/items/{GetIdForUrl}>")
        text1.append(i)
        text1.append("</a>")
        text1.append("</div>")
    return HttpResponse(text1)
def get_items(request,value):
    counter = 0
    for i in item:
        if i.get("id") == value:
            idobject,nameobject,quantity = i.values()
            text = f"<div>Айди Обьекта:{idobject}</div><div>Имя товара:{nameobject}</div><div>Количество на складе:{quantity}</div><a href='http://127.0.0.1:8000/items/'>Назад к списку товаров</a>" 
            break
        #elif counter+1 == len(item):
            #text = f"""Предмета с id:{value} нет в списке"""
        #counter += 1
        else:
            return HttpResponseNotFound(f"item:{value} not found")

    return HttpResponse(text)