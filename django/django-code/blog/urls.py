from django.conf.urls import url
from . import views

#Stiamo solo importando metodi che 
#appartengono a Django e tutte le nostre views dalla nostra app blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), 	#stiamo assegnando una view nominata post_list alla URL ^$
													# solo una stringa vuota può combaciare
													# Questo schema dirà a Django che views.post_list è il posto giusto dove andare se qualcuno entra nel tuo sito all'indirizzo 'http://127.0.0.1:8000/'.
]													# L'ultima parte name='post_list' è il nome dell'URL che verrà usata per identificare la view