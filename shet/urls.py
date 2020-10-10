from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    path('',views.product_form,name="product_insert"), #get and post request for insert operation
    path('columns/',views.columns)
    
    
]

urlpatterns += staticfiles_urlpatterns()

