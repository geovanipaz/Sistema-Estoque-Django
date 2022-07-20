from multiprocessing import context

from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

from .models import Estoque
from .forms import EstoqueCreateForm, EstoqueSearchForm, EstoqueUpdateForm
from .forms import EmitirForm, ReceberForm, NivelReabastecimentoForm
from django.contrib import messages
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
            #categoria__icontains=form['categoria'].value(),
            item_nome__icontains=form['item_nome'].value()
        )
        
        if form['exportar_para_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORIA', 'ITEM NOME', 'QUANTIDADE'])
            instance = estoques
            for stock in instance:
                writer.writerow([stock.categoria, stock.item_nome, stock.quantidade])
			
            return response
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
        messages.success(request, 'Salvo com Sucesso')
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
        messages.success(request, 'Deletado com Sucesso')
        return redirect('/list_item')
    return render(request, 'delete_item.html')

def estoque_detail(request, pk):
    estoque = Estoque.objects.get(id=pk)
    context = {
        'title':estoque.item_nome,
        'estoque':estoque,
    }
    return render(request,'estoque_detail.html', context)

def emitir_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    form = EmitirForm(request.POST or None, instance=estoque)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantidade -= instance.quantidade_emitida
        instance.emitida_por = str(request.user)
        messages.success(request, "Emitido Com Sucesso. "
                         + str(instance.quantidade) + " " +
                         str(instance.item_nome) + "agora restam no Estoque")
        instance.save()

		
        return redirect('/estoque_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
        
    context = {
		"title": 'Emitir ' + str(estoque.item_nome),
		"estoque": estoque,
		"form": form,
		"username": 'Emitir por: ' + str(request.user),
	}
    return render(request,'add_item.html', context)

def receber_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    form = ReceberForm(request.POST or None, instance=estoque)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantidade += instance.quantidade_recebida
        instance.save()
        messages.success(request, "Recebida Com Sucesso. "
                         + str(instance.quantidade) + " " +
                         str(instance.item_nome) + "agora tem no Estoque")
        

		
        return redirect('/estoque_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
        
    context = {
		"title": 'Receber ' + str(estoque.item_nome),
		"estoque": estoque,
		"form": form,
		"username": 'Receber por: ' + str(request.user),
	}
    return render(request,'add_item.html', context)   
	
def nivel_reabastecimento(request, pk):
    estoque = Estoque.objects.get(id=pk)
    form = NivelReabastecimentoForm(request.POST or None, instance=estoque)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Nivel de reabastecimento para " +
                         str(instance.item_nome) + " é atualizdo para " +
                         str(instance.nivel_reabastecimento))
        return redirect('/list_item')
    context = {
        'estoque':estoque,
        'form':form
    }
    return render(request,'add_item.html', context)