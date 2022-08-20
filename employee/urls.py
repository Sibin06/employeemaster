from django.urls import path
from employee import views

urlpatterns=[
    path('add',views.EmployeeCreateView.as_view(),name="emp-create"),
    path("all",views.EmployeeListView.as_view(),name="emp-list"),
    path("details/<str:emp_id>",views.EmployeeDetailView.as_view(),name="emp-detail"),
    path("change/<str:e_id>",views.EmployeeEditView.as_view(),name="emp-edit"),
    path("remove/<str:e_id>",views.remove_employee,name="emp-remove"),
    path("",views.index,name="index"),
    path("accounts/signup",views.SignUpView.as_view(),name="sign-up"),
    path("accounts/signin",views.LoginView.as_view(),name="sign-in"),
    path("accounts/signout",views.sign_out,name="signout")

]
