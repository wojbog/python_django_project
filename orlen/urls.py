from django.urls import path

from . import views

urlpatterns = [

    path('operations/', views.OperationListView.as_view()),

    path('operations/<int:pk>/', views.OperationDetailView.as_view()),


]
