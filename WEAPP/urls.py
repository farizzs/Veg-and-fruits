from django.urls import path
from WEAPP import views

urlpatterns = [
    path('indpage/', views.indpage, name="indpage"),
    path('addpage/', views.addpage, name="addpage"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaypage/', views.displaypage, name="displaypage"),
    path('editpage/<int:dataid>', views.editpage, name="editpage"),
    path('updatepage/<int:dataid>', views.updatepage, name="updatepage"),
    path('deletepage/<int:dataid>', views.deletepage, name="deletepage"),
    path('addpro/', views.addpro, name = "addpro"),
    path('savepro/', views.savepro, name="savepro"),
    path('displaypro/', views.displaypro, name="displaypro"),
    path('editpro/<int:dataid>', views.editpro, name="editpro"),
    path('deletepro/<int:dataid>', views.deletepro, name="deletepro"),
    path('updatepro/<int:dataid>', views.updatepro, name="updatepro"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('displaycon/', views.displaycon, name="displaycon"),
    path('deletecontact//<int:dataid>', views.deletecontact, name="deletecontact"),



]