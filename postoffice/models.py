from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    post_box_number = models.IntegerField(primary_key=True)

class MoneyOrder(models.Model):
    pbno = models.ForeignKey(Admin, on_delete=models.CASCADE)
    sname = models.CharField(max_length=25)
    s_add = models.TextField(max_length=100)
    s_pin = models.IntegerField()
    s_state = models.CharField(max_length=25)
    s_phon = models.BigIntegerField()
    s_city = models.CharField(max_length=25)
    rname = models.CharField(max_length=25)
    r_add = models.TextField(max_length=100)
    r_pin = models.IntegerField()
    r_state = models.CharField(max_length=25)
    r_phon = models.BigIntegerField()
    r_city = models.CharField(max_length=25)
    t_amount = models.IntegerField()
    amount = models.IntegerField()
    m_id = models.IntegerField(primary_key=True)


Items = (
    ('L','Letter'),
    ('P','Parcel')
)

class Letter_Percel(models.Model):
    pbno = models.ForeignKey(Admin, on_delete=models.CASCADE)
    category = models.CharField(choices=Items, max_length=20)
    sname = models.CharField(max_length=25)
    s_add = models.TextField(max_length=100)
    s_pin = models.IntegerField()
    s_state = models.CharField(max_length=25)
    s_phon = models.BigIntegerField()
    s_city = models.CharField(max_length=25)
    rname = models.CharField(max_length=25)
    r_add = models.TextField(max_length=100)
    r_pin = models.IntegerField()
    r_state = models.CharField(max_length=25)
    r_phon = models.BigIntegerField()
    r_city = models.CharField(max_length=25)
    weight = models.IntegerField()
    amount = models.IntegerField()
    id = models.AutoField(primary_key=True )

sts = (
    ('D','Delivered'),
    ('N','Not delivered')
)
class Status(models.Model):
    id = models.OneToOneField(Letter_Percel, on_delete=models.CASCADE,primary_key=True)
    status = models.CharField(choices=sts, max_length=25)

class Add_account(models.Model):
    pbno = models.ForeignKey(Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    add = models.TextField(max_length=100)
    pincode = models.IntegerField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    phno = models.BigIntegerField()
    dob = models.DateField()
    ration = models.CharField(max_length=25,null=True)
    pancard = models.CharField(max_length=25)
    adhar_no = models.BigIntegerField()
    ifsc_code = models.CharField(max_length=20)
    account_number = models.BigIntegerField(primary_key=True)
    nominee_acc_no = models.BigIntegerField()
    balance = models.IntegerField(null=True)

class Add_money(models.Model):
    account_number = models.ForeignKey(Add_account, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    amount = models.IntegerField()

class Withdraw(models.Model):
    account_number = models.ForeignKey(Add_account, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    date = models.DateField()
    amount = models.IntegerField()

gen = (
    ('M', 'Male'),
    ('F', 'Female')
)
class CreateInsurance(models.Model):
    account_number = models.ForeignKey(Add_account, on_delete=models.CASCADE)
    insurance_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    gender = models.CharField(choices=gen, max_length=20)
    amount = models.IntegerField()
    pancard = models.CharField(max_length=25)
    age = models.IntegerField()

class claim(models.Model):
    insurance_id = models.ForeignKey(CreateInsurance, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    amount = models.IntegerField()

class E_bill(models.Model):
    account_number = models.ForeignKey(Add_account, on_delete=models.CASCADE)
    b_id = models.IntegerField()
    b_name = models.CharField(max_length=25)
    b_address = models.TextField()
    l_usedunit = models.IntegerField()
    c_unit = models.IntegerField()
    amount = models.IntegerField()
    c_date = models.DateField()
    recipt_no = models.IntegerField(primary_key=True)