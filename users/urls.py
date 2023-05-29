from django.urls import path,include
from .views import *

urlpatterns = [
    path('get-all-student',GetStudentViews.as_view()),
    path('delete-student/<int:pk>',DeleteStudentsView.as_view()),
    path('student-address/<int:pk',StudentDetailsAddressViews.as_view()),

]





