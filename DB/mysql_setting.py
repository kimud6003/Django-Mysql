DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql', # 사용할 DBMS 
        'NAME' : 'KUD', # Mysql 데이터베이스 이름
        'USER' : 'root', # DB 접속 계정명
        'PASSWORD': '1q2w3e', # 해당 계정의 비밀번호
        'HOST' : '146.56.154.230', # IP
        'PORT' : '3306' # PORT
    }
}
SECRET_KEY = 'django-insecure-r-9u+%7ln=dl78q90xx+lkw0c1vlajxi*h^8n7j)!9p6k2&dh%'