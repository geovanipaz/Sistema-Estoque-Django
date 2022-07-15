from django.db import models

# Create your models here.
class Estoque(models.Model):
    categoria = models.CharField(max_length=50, blank=True, null=True)
    item_nome = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.IntegerField(default='0', blank=True, null=True)
    quantidade_recebida = models.IntegerField(default='0', blank=True, null=True)
    recebida_por = models.CharField(max_length=50, blank=True, null=True)
    quantidade_emitida = models.IntegerField(default='0', blank=True, null=True)
    emitida_por = models.CharField(max_length=50, blank=True, null=True)
    emitida_para = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    criada_por = models.CharField(max_length=50, blank=True, null=True)
    nivel_reabastecimento = models.IntegerField(default='0', blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(auto_now_add=False, auto_now=True)
    exportar_para_CSV = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.item_nome +'-'+ str(self.quantidade)
    

"""
class Stock(models.Model):
    	category = models.CharField(max_length=50, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.item_name
"""
