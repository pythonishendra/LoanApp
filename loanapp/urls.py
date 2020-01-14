from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('loan_apply',LoanViewController.as_view()),
    path('loan_member',GetApprovedOrNotLoanView.as_view()),
    path('all_loan_member',GetAllLoanMemberView.as_view())
]
