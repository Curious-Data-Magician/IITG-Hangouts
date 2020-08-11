from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.home, name='home'),
    path(r'complete/', views.complete, name='complete'),
    # path('add', views.add, name='add'),
    # path('mcq', views.home_view, name='mcq')
    # path('', views.nextpage, name='nextpage')
]
