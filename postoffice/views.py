from django.contrib import messages
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def choice(request):
    if 'savingAccount' in request.POST:
        return render(request,'CreateAccount.html')
    elif 'status' in request.POST:
        return render(request, 'Status.html')
    elif 'moneyOrder' in request.POST:
        return render(request, 'MoneyOrder.html')
    elif 'insurance' in request.POST:
        return render(request, 'LifeInsurance.html')
    elif 'letter' in request.POST:
        return render(request, 'Letter.html')
    elif 'e-bill' in request.POST:
        return render(request, 'E-bill.html')
    elif 'addMoney' in request.POST:
        return render(request, 'AddMoney.html')
    elif 'withdraw' in request.POST:
        return render(request, 'Withdraw.html')

def create(request):
    if request.method == 'POST':
        acc = Add_account()
        if Admin.objects.get(post_box_number=request.POST['pbno']):
            acc.pbno_id = request.POST['pbno']
            acc.name = request.POST['name']
            acc.add = request.POST['address']
            acc.pincode = request.POST['pincode']
            acc.city = request.POST['city']
            acc.state = request.POST['state']
            acc.phno = request.POST['phno']
            acc.dob = request.POST['dob']
            acc.ration = request.POST['rcard']
            acc.pancard = request.POST['pancard']
            acc.adhar_no = request.POST['aadhar']
            acc.ifsc_code = request.POST['ifsc']
            acc.account_number = request.POST['anumber']
            acc.nominee_acc_no = request.POST['nanumber']
            acc.balance = 0
            acc.save()
        else:
            messages.info(request, 'Post Box Number Not Found!!')
            return render(request, 'CreateAccount.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'CreateAccount.html')

def moneyOrder(request):
    if request.method == 'POST':
        mo = MoneyOrder()
        if Admin.objects.get(post_box_number=request.POST['pbno']):
            mo.pbno_id = request.POST['pbno']
            mo.sname = request.POST['sname']
            mo.s_add = request.POST['saddress']
            mo.s_pin = request.POST['spincode']
            mo.s_city = request.POST['scity']
            mo.s_state = request.POST['sstate']
            mo.s_phon = request.POST['sphno']
            mo.amount = request.POST['amt']
            mo.t_amount = request.POST['tamt']
            mo.sname = request.POST['rname']
            mo.r_add = request.POST['raddress']
            mo.r_pin = request.POST['rpincode']
            mo.r_city = request.POST['rcity']
            mo.r_state = request.POST['rstate']
            mo.r_phon = request.POST['rphno']
            mo.save()
        else:
            messages.info(request, 'Post Box Number Not Found!!')
            return render(request, 'MoneyOrder.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'MoneyOrder.html')

def admin(request):
    if request.method == 'POST':
        if Admin.objects.get(post_box_number=request.POST['pbno']):
            user = Admin.objects.filter(post_box_number=request.POST['pbno'])
            if user[0].username == request.POST['username']:
                if user[0].password == request.POST['password']:
                    return render(request, 'PostOffice.html')
                else:
                    messages.info(request, 'Password Does not match!!')
            else:
                messages.info(request, 'Username Does not match!!')
        else:
            messages.info(request, 'Post Box Number Not Found!!')
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def insurance(request):
    if request.method == 'POST':
        ins = CreateInsurance()
        if Add_account.objects.get(account_number=request.POST['anumber']):
            ins.account_number_id = request.POST['anumber']
            ins.insurance_id = request.POST['insuranceid']
            ins.name = request.POST['name']
            ins.gender = request.POST['gender']
            ins.amount = request.POST['amt']
            ins.pancard = request.POST['pancard']
            ins.age = request.POST['age']
            ins.save()
        else:
            messages.info(request, 'Account Number Not Found!!')
            return render(request, 'LifeInsurance.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'LifeInsurance.html')

def letter(request):
    if request.method == 'POST':
        l = Letter_Percel()
        s = Status()
        if Admin.objects.get(post_box_number=request.POST['pbno']):
            l.category = request.POST['category']
            l.pbno_id = request.POST['pbno']
            l.id = request.POST['id']
            l.sname = request.POST['sname']
            l.s_add = request.POST['saddress']
            l.s_pin = request.POST['spincode']
            l.s_state = request.POST['sstate']
            l.s_city = request.POST['scity']
            l.s_phon = request.POST['sphno']
            l.weight = request.POST['weight']
            l.amount = request.POST['amt']
            l.rname = request.POST['rname']
            l.r_add = request.POST['raddress']
            l.r_pin = request.POST['rpincode']
            l.r_state = request.POST['rstate']
            l.r_city = request.POST['rcity']
            l.r_phon = request.POST['rphno']
            l.save()
            s.id_id = request.POST['id']
            s.status = 'Not delivered'
            s.save()
        else:
            messages.info(request, 'Post Box Number Not Found!!')
            return render(request, 'Letter.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'Letter.html')

def e_bill(request):
    if request.method == 'POST':
        bill = E_bill()
        if Add_account.objects.get(account_number=request.POST['anumber']):
            bill.account_number_id = request.POST['anumber']
            bill.b_id = request.POST['id']
            bill.b_name = request.POST['name']
            bill.b_address = request.POST['address']
            bill.l_usedunit = request.POST['lunits']
            bill.c_unit = request.POST['cunits']
            bill.amount = request.POST['amt']
            bill.c_date = request.POST['date']
            bill.recipt_no = request.POST['recepitNo']
            bill.save()
        else:
            messages.info(request, 'Account Number Not Found!!')
            return render(request, 'E-bill.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'E-bill.html')

def addMoney(request):
    if request.method == 'POST':
        adm = Add_money()
        if Add_account.objects.get(account_number=request.POST['anumber']):
            adm.account_number_id = request.POST['anumber']
            adm.name = request.POST['name']
            adm.amount = request.POST['amt']
            acc = Add_account.objects.get(account_number=request.POST['anumber'])
            acc.balance += int(request.POST['amt'])
            acc.save()
            adm.save()
        else:
            messages.info(request, 'Account Number Not Found!!')
            return render(request, 'AddMoney.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'AddMoney.html')

def withdraw(request):
    if request.method == 'POST':
        wd = Withdraw()
        if Add_account.objects.get(account_number=request.POST['anumber']):
            acc = Add_account.objects.get(account_number=request.POST['anumber'])
            if acc.balance >= int(request.POST['amt']):
                wd.account_number_id = request.POST['anumber']
                wd.name = request.POST['name']
                wd.date = request.POST['date']
                wd.amount = request.POST['amt']
                acc.balance -= int(request.POST['amt'])
                acc.save()
                wd.save()
            else:
                messages.info(request, 'Insufficient Account Balance!!')
        else:
            messages.info(request, 'Account Number Not Found!!')
            return render(request, 'Withdraw.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'Withdraw.html')

def status(request):
    if request.method == 'POST':
        if Status.objects.get(id=request.POST['id']):
            s = Status.objects.get(id=request.POST['id'])
            s.status = request.POST['status']
            s.save()
        else:
            messages.info(request, 'Id Not Found!!')
            return render(request, 'Status.html')
        return render(request, 'PostOffice.html')
    else:
        return render(request, 'Status.html')