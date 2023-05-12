from django.urls import path
from WEBAPP import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('shoppage/<itemcatg>/', views.shoppage, name="shoppage"),
    path('singlepro/<int:dataid>/', views.singlepro, name="singlepro"),
    path('userlog', views.userlog, name="userlog"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('logout/', views.logout, name="logout"),

]