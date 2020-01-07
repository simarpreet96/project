from django.urls import path
from .views import image_view, success

app_name='task'

urlpatterns = [
	#path('', views.doc_list, name='doc_list'),
	path('', image_view, name = 'image_upload'), 
    path('success', success, name = 'success'),
]