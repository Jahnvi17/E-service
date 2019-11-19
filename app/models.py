from django.db import models

# Create your models here.

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length = 10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

    def __str__(self):
        return self.role

class Admin(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    
    fname = models.CharField(max_length=50,default="abc")
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=20)
    #birthdate = models.DateField()

    #Personal-Information
    
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    maritalstatus = models.CharField(max_length=50)

    # #Emergency-Contact
    # ename = models.CharField(max_length=50)
    # relationship = models.CharField(max_length=50)
    # ephone = models.IntegerField(max_length=50)

    # #Education-Info
    # course_name = models.CharField(max_length=50)
    # degree = models.CharField(max_length=50)
    # duration = models.CharField(max_length=50)

class employee(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=20)
    #birthdate = models.DateField()

    #Personal-Information
    tel_phone= models.BigIntegerField()
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    maritalstatus = models.CharField(max_length=50)

    #Emergency-Contact
    ename = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    ephone = models.BigIntegerField()

    #Education-Info
    course_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)



    
