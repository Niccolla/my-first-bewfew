from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)), # significa che per ogni URL 
											   # che comincia con admin/ Django troverà la corrispondente view
	
	url(r'', include('blog.urls')),	# Django reindirizzerà ora tutto ciò che viene da 'http://127.0.0.1:8000/' verso blog.urls e cercherà 
									# ulteriori istruzioni in questo file
]												
