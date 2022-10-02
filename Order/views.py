from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.generic import View

from .forms import OrderForm
from .models import Menu, Order, Category


class CreateOrderView(View):

    def get(self, request):
        form = OrderForm
        return render(request, 'order.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            menu = Menu.objects.all()
            table = form.cleaned_data.get("table")
            for obj in menu:
                count = form.cleaned_data.get(f"{obj}")
                des = form.cleaned_data.get(f"_{obj}_")
                if count == '0' or count == '' or not count:
                    pass
                elif count > 0:
                    for i in range(count):
                        Order.objects.create(product=obj.name, table=table, description=des)
            return HttpResponse('done')
        else:
            return render(request, "order.html", {"form": form})
