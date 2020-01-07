from django.contrib import admin
from django.urls import path, include
from task import views
from django.views.generic import RedirectView
from django.contrib.auth import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', RedirectView.as_view(pattern_name='person_changelist'), name='home'),
]
admin.site.site_header="simar1"
admin.site.site_title="simar2"
admin.site.index_title= "simar3"
