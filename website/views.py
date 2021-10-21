from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from helloworld.models import Funcionario
from website.forms import InsereFuncionarioForm


# PÁGINA PRINCIPAL
# ----------------------------------------------
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------
class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------
class FuncionarioCreateView(CreateView):
    template_name = "website/cadastra.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")
