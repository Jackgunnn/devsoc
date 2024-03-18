from django.urls import path
from home import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('addquestion/', views.add_question, name='add_question'),
    path('viewanswer/<int:question_id>/', views.view_answer, name="view_answer" ),
    path('addanswer/<int:question_id>/', views.add_answer, name='add_answer'),
]