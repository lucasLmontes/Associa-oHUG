from django.contrib.auth.forms import UserCreationForm
from aplic.models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['login']
