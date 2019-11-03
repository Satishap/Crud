from django import forms
from .import views
from .models import Hello,Customer,Navbar

class Hello_form(forms.ModelForm):
    Name = forms.CharField(max_length=100)
    email = forms.EmailField()
    Mobile= forms.CharField(max_length=50)


    class Meta:
        model = Hello
        fields=['Name','email','Mobile']



class Customer_form(forms.ModelForm):
    Customer_Name=forms.CharField(max_length=100, required=True)
    Customer_Mobile_no=forms.CharField(max_length=100, required=True)
    Address=forms.CharField(max_length=100, required=True)
    Salary=forms.CharField(max_length=100, required=True)

    class Meta:
        model=Customer
        fields=['Customer_Name','Customer_Mobile_no','Address','Salary']


class Navbar_form(forms.ModelForm):
    Product_type=forms.CharField(max_length=100, required=True)
    First_Name=forms.CharField(max_length=100, required=True)
    Last_Name=forms.CharField(max_length=100, required=True)
    Email=forms.EmailField()
   

    class Meta:
        model = Navbar
        fields=['Product_type','First_Name','Last_Name','Email']        

        