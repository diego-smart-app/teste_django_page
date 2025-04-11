from django.db import models

# Create your models here.

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text
    
class Entry(models.Model):
    """Algo específico aprendido sobre o assunto"""
    #Chave estrangeira, já o on_delete faz com que todas anotações sejam excluídas a partir do momento quese exclui o tópico relacionado.
    #Leia mais em: doc.djangoproject.com/en/2.2/ref/models/fields/#arguments
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    #Classe somente para resolver o problema do ingles da palavra entry, #caso não fosse feita, ao usar em plural ficaria entrys
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        #Apresenta até as 50 primeiros caracteres e a reticências
        return self.text[:50] + '...'
