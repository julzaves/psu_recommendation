from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/', views.recommend_form, name='recommend_form'),
    path('college/<slug:college_slug>/', views.college_programs, name='college_programs'),
    path('program/<uuid:program_id>/', views.program_detail, name='program_detail'),
]