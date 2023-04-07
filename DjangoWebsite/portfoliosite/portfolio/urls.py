from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

# favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # re_path(r'^favicon\.ico$', favicon_view),
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
]