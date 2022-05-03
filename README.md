## sql 프로젝트 세팅

- `DataBase`의 `sql`을 만져보기 위해 `Django`의 프로젝트를 다시 생성 해보도록 하겠습니다.

- 그럼 가상 환경을 위해 `virtual environment`를 위해 `venv` 설정을 해보도록 하겠습니다.

```console
# myvenv를 설정

python -m venv myvenv
```

- `pip`를 업그레이드를 진행하고, `django`를 설치하겠습니다.

```console
# venv Start
.\myvenv\Scripts\activate

# pip upgrade
python -m pip install --upgrade pip

# django install
pip install django
```

- `django-admin`을 통해 `django` 프로젝트 생성하겠습니다.

```console
# django Project DB
django-admin startproject DB

# Entry DB folder
cd DB

```

- `project`를 생성했으니 sql이라는 이름의 `APP`을 만들어보도록 하겠습니다.

```console
# django App create
python ./manage.py startapp sql
```

## sql 프로젝트 세팅

- 이제 우리의 본 프로젝트인 `mysql`를 `djnago`에서 사용하는 프로젝트를 진행하도록 하겠습니다!

- `mysql`과 `django`를 연결하는 `Databaser Connector`를 설치 하겠습니다.

```py
# Mysql Install Databser Connector
pip install mysqlclient
```

- 이제 `manage.py`가 있는 폴더에 `mysql_setting.py`를 만들어주시고 아래 내용을 쳐주시면 됩니다.

```py
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql', # 사용할 DBMS
        'NAME' : 'test', # Mysql 데이터베이스 이름
        'USER' : 'root', # DB 접속 계정명
        'password': '1q2w3e', # 해당 계정의 비밀번호
        'HOST' : '146.56.154.230', # IP
        'PORT' : '3306' # PORT
    }
}
SECRET_KEY = 'django-insecure-r-9u+%7ln=dl78q90xx+lkw0c1vlajxi*h^8n7j)!9p6k2&dh%' # 시크릿 key
```

- 해당 내용들은 `DB`폴더에 있는 `settings.py`의 `DATABASES`와 `SECRET_KEY`를 설정합니다.

- 그럼 설정을 했기 때문에 필요없어진 `settings.py`에 있는 `DATABASES`와 `SECRET_KEY`를 지우고 `mysql_setting.py`에 있는 내용으로 바꾸겠습니다.

```py
# settings.py
import mysql_setting

SECRET_KEY = mysql_setting.SECRET_KEY # 기존에 있던 SECRET_KEY를 분리

DATABASES = mysql_setting.DATABASES  # 기존에 있던 DATABASES를 mysql_setting에 SECRET_KEY

```

- 이제 `mysql`과 `Django`를 연결이 되는지 보겠습니다.

```console
python manage.py insepctdb
```

<p align="center"><img src="./IMG/1.png "></p>

-
