from django.shortcuts import render
import mysql.connector as sql

# aa nichena globle variable chhe
fn = ''
ln = ''
sex = ''
em = ''
pwd = ''


# Create your views here.

def signupnow(request):
    global fn, ln, sex, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="20312661999", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                sex = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fn, ln, sex, em, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')


def loginnow(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="20312661999", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from users where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, 'welcome.html')

    return render(request, 'login_page.html')