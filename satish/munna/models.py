from django.db import models

class tudent(models.Model):
    Name=models.CharField(max_length=500)
    image=models.ImageField(upload_to="image", default=True)
    dateTime=models.DateTimeField(auto_now=True)
    dec=models.TextField(default=True)
    
    
    def __str__(self):
        return self.Name    




class Satish(models.Model):
    IMag=models.ImageField()
    
class Hello(models.Model):
    Name = models.CharField(max_length=100)
    email=models.EmailField()
    Mobile=models.CharField(max_length=50)


    def __str__(self):
        return self.Name

   





 
class Customer(models.Model):
    Customer_Name=models.CharField(max_length=100)
    Customer_Mobile_no=models.CharField(max_length=100) 
    Address=models.CharField(max_length=500)
    Salary=models.CharField(max_length=100)

    def __str__(self):
        return self.Customer_Name


class Navbar(models.Model):
    Product_type=models.CharField(max_length=100)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Email=models.EmailField()
    


    def __str__(self):
        return self.First_Name

