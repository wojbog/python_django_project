from django.urls import path

from . import views

urlpatterns = [

    path('getListOperations/', views.OperationListView.as_view()),

    path('detailOperation/<int:pk>/', views.OperationDetailView.as_view()),

]
