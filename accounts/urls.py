from django.urls import path

from .views import (
    register_jobseeker,
    register_employer,
    user_login,
    user_logout
)

urlpatterns = [

    path(
        'register/jobseeker/',
        register_jobseeker,
        name='register_jobseeker'
    ),

    path(
        'register/employer/',
        register_employer,
        name='register_employer'
    ),

    path(
        'login/',
        user_login,
        name='login'
    ),

    path(
        'logout/',
        user_logout,
        name='logout'
    ),
]