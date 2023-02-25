from django.urls import path
from .views import TodosAPIView, TodoAPIView, DoneTodoAPIView, DonesTodoAPIView


urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:pk>/', TodoAPIView.as_view()),
    path('done/', DonesTodoAPIView.as_view()),
    path('done/<int:pk>', DoneTodoAPIView.as_view()),
]
