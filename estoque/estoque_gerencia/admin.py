from django.contrib import admin
from .models import Estoque
from .forms import EstoqueCreateForm
# Register your models here.

class EstoqueCreateAdmin(admin.ModelAdmin):
    list_display = ['categoria','item_nome','quantidade']
    form = EstoqueCreateForm
    list_filter = ['categoria']
    search_fields = ['categoria','item_nome']

admin.site.register(Estoque, EstoqueCreateAdmin)
