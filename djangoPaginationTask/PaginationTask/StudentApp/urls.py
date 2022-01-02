from django.urls import path
from .views import addStudentView,showStudentView,updateStudentView,deleteStudentView

urlpatterns = [
    path('add/',addStudentView,name='add_student'),
    path('show/',showStudentView,name='show_student'),
    path('update/<int:i>/',updateStudentView,name='update_data'),
    path('delete/<int:i>/',deleteStudentView,name='delete_data'),
]