from rest_framework import status,mixins
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics


#Loan View controller
class LoanViewController(generics.GenericAPIView, mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=LoanSerializer
    queryset=Loan.objects.all()

    def post(self,request):
        return self.create(request)

#Get applied loan member based on approval True or False
class GetApprovedOrNotLoanView(generics.ListAPIView):
    serializer_class=LoanSerializer
    def get_queryset(self):
        return Loan.objects.filter(approve_status=self.request.query_params.get('status'))

#all appied loan member
class GetAllLoanMemberView(generics.ListAPIView):
    serializer_class=LoanSerializer
    def get_queryset(self):
        return Loan.objects.all()





