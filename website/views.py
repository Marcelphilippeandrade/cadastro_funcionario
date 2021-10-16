from django.views.generic import TemplateView, ListView
from helloworld.models import Funcionario


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
