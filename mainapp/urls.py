from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('sobrenosotros/',views.aboutus,name="about"),
    path('subcomision/<int:subcom_id>', views.subcom, name="subcomision"),
    path('feriadellibro/', views.feriadelibro, name="feria"),
    path('osvaldobayer/', views.osvaldbayer, name="ob")
    ]