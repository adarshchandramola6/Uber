from django.urls import path,include
from .views import *

urlpatterns = [
    path('get-all-student',GetStudentViews.as_view()),
]



