from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [ 

    path('students',views.students,name='students'),
    path('form',views.form,name='form'),
    path('retrieve',views.retrieve,name='retrieve'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]