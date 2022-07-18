from multiprocessing import context

from django.shortcuts import render, redirect


from .models import Estoque
from .forms import EstoqueCreateForm, EstoqueSearchForm, EstoqueUpdateForm
# Create your views here.

def home(request):
    title = "bem vindo"
    context = {'title':title}
    return render(request, 'home.html', context)

def list_item(request):
    title = 'Lista de Item'
    
    form = EstoqueSearchForm(request.POST or None)
    estoques = Estoque.objects.all()
    context = {
        'form':form,
        'title':title,
        'estoques':estoques
    }
    if request.method == 'POST':
        estoques = Estoque.objects.filter(
            categoria__icontains=form['categoria'].value(),
            item_nome__icontains=form['item_nome'].value()
        )
        context = {
            'form':form,
            'title':title,
            'estoques':estoques
        }
    return render(request, 'list_item.html', context)

def add_item(request):
    form = EstoqueCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        'title':'Add Estoque',
        'form':form,
    }
    return render(request, 'add_item.html', context)

def update_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    form = EstoqueUpdateForm(instance=estoque)
    if request.method == 'POST':
        form = EstoqueUpdateForm(request.POST, instance=estoque)
        if form.is_valid():
            form.save()
            return redirect('/list_item')
    context = {
        'form':form
    }
    return render(request, 'add_item.html', context)
    
def delete_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    if request.method == 'POST':
        estoque.delete()
        return redirect('/list_item')
    return render(request, 'delete_item.html')