from rest_framework.viewsets import ModelViewSet

from .categoria import Categoria
from .editora import Editora

from core.models import Livro
from core.serializers import LivroSerializer

...
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros", null=True, blank=True
    )
    
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
