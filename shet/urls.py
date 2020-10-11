from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    path('',views.get_sheet_link,), #get and post request for link
    path('columns/',views.columns)  #get and post request for columns selection
    
    
]

urlpatterns += staticfiles_urlpatterns()

