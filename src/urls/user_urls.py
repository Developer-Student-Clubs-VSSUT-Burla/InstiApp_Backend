from django.urls import path
from src import views

urlpatterns = [
    path('',views.getUsers,name='users'),
    path('login/',views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('register/',views.registerUser,name='register'),
]
