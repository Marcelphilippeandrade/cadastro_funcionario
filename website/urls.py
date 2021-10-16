from django.urls import path
from website.views import IndexTemplateView, FuncionarioListView

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),
]
