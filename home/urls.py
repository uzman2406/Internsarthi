from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('save/<int:internship_id>/', views.save_internship_view, name='save_internship'),
    path('saved/', views.saved_internships_view, name='saved'),
    path('apply/<int:internship_id>/', views.apply_internship_view, name='apply_internship'),
    path('applied/', views.applied_internships_view, name='applied'),

]
