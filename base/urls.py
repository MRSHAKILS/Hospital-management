from django.urls import path
from base import views

app_name = "base"

urlpatterns = [
    path("", views.index, name="index"),
    path("service/<service_id>", views.service_detail, name="service_detail"),
    path("book-appointment/<service_id>/<doctor_id>/",
         views.book_appointment, name="book_appointment"),
    path("checkout/<billing_id>/", views.checkout, name="checkout"),
    path('pay_now/<str:billing_id>/', views.pay_now, name='pay_now'),
    path('payment_status/<str:billing_id>/',
         views.payment_status, name='payment_status'),

]
