from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('delete-member/<pk>/', views.DeleteMember.as_view(),name='delete-member'),
    path('delete-vehicle/<pk>/', views.DeleteVehicle.as_view(),name='delete-vehicle'),
    path('delete-pet/<pk>/', views.DeletePet.as_view(),name='delete-pet'),
    path('delete-harper/<pk>/', views.DeleteHarper.as_view(),name='delete-harper'),
    path('cancel/', views.CancelView.as_view(),name='cancel'),
]