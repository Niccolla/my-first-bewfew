from django.db import models
from django.utils import timezone

#la classe Post è figlia di models.Model

class Post(models.Model): #significa che il Post è un modello Django, quindi Django sa che dovrebbe essere salvato nel database
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #models.ForeignKey - questo è un link a un altro modello.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
# ForeignKey.on_delete
# When an object referenced by a ForeignKey is deleted, Django by default also deletes the 
# object containing the ForeignKey.