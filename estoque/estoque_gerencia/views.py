from multiprocessing import context
from multiprocessing.sharedctypes import Value

from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

from django.contrib.auth.decorators import login_required
from .models import Estoque, HistoricoEstoque
from .forms import EstoqueCreateForm, EstoqueSearchForm, EstoqueUpdateForm
from .forms import EmitirForm, ReceberForm, NivelReabastecimentoForm, HistoricoEstoqueSearchForm
from django.contrib import messages
# Create your views here.

@login_required
def home(request):
    title = "bem vindo"
    context = {'title':title}
    return redirect('/list_item')
    #return render(request, 'home.html', context)

@login_required
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
    return render(request, 'estoque_gerencia/list_item1.html', context)

@login_required
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


@login_required
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


@login_required    
def delete_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    if request.method == 'POST':
        estoque.delete()
        messages.success(request, 'Deletado com Sucesso')
        return redirect('/list_item')
    return render(request, 'delete_item.html')



@login_required
def estoque_detail(request, pk):
    estoque = Estoque.objects.get(id=pk)
    context = {
        'title':estoque.item_nome,
        'estoque':estoque,
    }
    return render(request,'estoque_detail.html', context)


@login_required
def emitir_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    form = EmitirForm(request.POST or None, instance=estoque)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantidade_recebida = 0
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
@login_required
def receber_item(request, pk):
    estoque = Estoque.objects.get(id=pk)
    form = ReceberForm(request.POST or None, instance=estoque)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantidade_emitida = 0
        instance.quantidade += instance.quantidade_recebida
        instance.recebida_por = str(request.user)
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


@login_required	
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






@login_required
def list_history(request):
    cabeca = 'LISTA DE ITENS'
    historico = HistoricoEstoque.objects.all()
    form  = HistoricoEstoqueSearchForm(request.POST or None)
    context = {
        'form':form,
        'cabeca':cabeca,
        'historico':historico
    }
    
    if request.method == 'POST':
        categoria = form['categoria'].value()
        '''
        historico = HistoricoEstoque.objects.filter(
            item_nome__icontains=form['item_nome'].value()
        )
        '''
        historico = HistoricoEstoque.objects.filter(
            item_nome__icontains=form['item_nome'].value(),
            ultima_atualizacao__range=[
                form['data_inicio'].value(),
                form['data_fim'].value()
            ]
        )
        
        if (categoria != ''):
            historico = historico.filter(categoria_id=categoria)
            
        if form['exportar_para_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(
				['CATEGORY', 
				'ITEM NAME',
				'QUANTITY', 
				'ISSUE QUANTITY', 
				'RECEIVE QUANTITY', 
				'RECEIVE BY', 
				'ISSUE BY', 
				'LAST UPDATED'])
            instance = historico
            
            for stock in instance:
                writer.writerow(
                [stock.categoria, 
                stock.item_nome, 
                stock.quantidade, 
                stock.quantidade_emitida, 
                stock.quantidade_recebida, 
                stock.recebida_por, 
                stock.emitida_por, 
                stock.ultima_atualizacao])
            return response
        context = {
            'form':form,
            'cabeca':cabeca,
            'historico': historico
        }
    return render(request, "estoque_gerencia/list_history1.html",context)