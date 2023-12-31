from rest_framework import serializers
from .models import Student,Transaction,Fees

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        
class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = "__all__"
        
