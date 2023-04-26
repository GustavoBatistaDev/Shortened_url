from django.urls import path

from . import views


app_name = "reduce"

urlpatterns = [
    path('', views.generate_url, name="generate_url"),
    path('<uidb4>', views.redirect_client, name="redirect_client"),
    path('report/<uidb4>', views.report_url, name="report_url")
]