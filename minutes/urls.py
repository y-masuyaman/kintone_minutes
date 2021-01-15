from django.urls import path
from . import views

app_name = 'minutes'

urlpatterns = [
    path('list/', views.MinutesListView.as_view(), name='list'), 
    path('detail/<int:pk>/', views.MinutesDetailView.as_view(), name='detail'), 
    path('create/', views.MinutesCreateView.as_view(), name='create'), 
    path('update/<int:pk>/', views.MinutesUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>/', views.MinutesDeleteView.as_view(), name='delete'), 
]
