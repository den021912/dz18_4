from django.shortcuts import render


def class_template(request):
    return render(request, 'fourth_task/class_template.html')
def func_template(request):
    return render(request, 'fourth_task/func_template.html')
def basket(request):
    return render(request, 'fourth_task/basket.html')
def menu(request):
    return render(request, 'fourth_task/menu.html')
