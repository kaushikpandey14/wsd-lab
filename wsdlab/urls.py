"""wsdlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pssr import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pssr/',include('pssr.urls')),
    path('',views.index,name='page1'),
    path('general/', views.general, name='general'),
    path('general_output/',views.general_output,name='general_output'),

    path('Machinerysafety/',views.Machinery_Safety_A,name='Machinerysafety'),
    path('Machinerysafety_output/',views.Machinery_Safety_output,name='Machinerysafety_output'),
   
   path('Managementofchange/',views.Management_of_change_A,name='Managementofchange'),
    path('Managementofchange_output/',views.Management_of_change_output,name='Managementofchange_output'),
   
   path('QualityAssurance/',views.Quality_Assurance_A,name='QualityAssurance'),
    path('QualityAssurance_output/',views.Quality_Assurance_output,name='QualityAssurance_output'),
   
   path('SOP/',views.SOP_A,name='SOP'),
    path('SOP_output/',views.SOP_output,name='SOP_output'),
   
   path('ENVIROMENT/',views.Enviroment_A,name='ENVIROMENT'),
    path('ENVIROMENT_output/',views.Enviroment_output,name='ENVIROMENT_output'),
   
   path('ELECTRICALS/',views.Electrical_Safety_A,name='ELECTRICALS'),
    path('ELECTRICALS_output/',views.Electrical_Safety_output,name='ELECTRICALS_output'),
   
   path('FIREPROTECTION/',views.Fire_Protection_A,name='FIREPROTECTION'),
    path('FIREPROTECTION_output/',views.Fire_Protection_output,name='FIREPROTECTION_output'),
   
   path('ENGINEERINGDESIGN/',views.Engineering_Design_A,name='ENGINEERINGDESIGN'),
    path('ENGINEERINGDESIGN_output/',views.Engineering_Design_output,name='ENGINEERINGDESIGN_output'),
   
   path('INDUSTRIALHYGIENE/',views.Industrial_Hygine_personal_Health_A,name='INDUSTRIALHYGIENE'),
    path('INDUSTRIALHYGIENE_output/',views.Industrial_Hygine_personal_Health_output,name='INDUSTRIALHYGIENE_output'),
   
   path('ERGONOMICS/',views.Ergonomics_A,name='ERGONOMICS'),
    path('ERGONOMICS_output/',views.Ergonomics_output,name='ERGONOMICS_output'),
   
   path('MECHANICALINTEGRITY/',views.Mechanical_Integrity_A,name='MECHANICALINTEGRITY'),
    path('MECHANICALINTEGRITY_output/',views.Mechanical_Integrity_output,name='MECHANICALINTEGRITY_output'),
   
   path('CONTRACTORSAFETY/',views.Contractor_Safety_A,name='CONTRACTORSAFETY'),
    path('CONTRACTORSAFETY_output/',views.Contractor_Safety_output,name='CONTRACTORSAFETY_output'),
   
   path('GENERALPROCESSSAFETY/',views.General_Process_Safety_A,name='GENERALPROCESSSAFETY'),
    path('GENERALPROCESSSAFETY_output/',views.General_Process_Safety_output,name='GENERALPROCESS SAFETY_output'),
   
   path('COMMUNITYAWARENESS/',views.Community_Awareness_Emergency_Response_A,name='COMMUNITYAWARENESS'),
    path('COMMUNITYAWARENESS_output/',views.Community_Awareness_Emergency_Response_output,name='COMMUNITYAWARENESS_output'),
   
   
]
