from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def sqlExcuter(sql):
    try:
        cursor = connection.cursor()
        result = cursor.execute(sql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()
        return datas
    except:
        connection.rollback()
        print("Fail to sql, the string is" + sql)
        return datas


def select(request):
    mysql = "select * from tmp"
    sqlExcuter(mysql)
    return HttpResponse("Fail")