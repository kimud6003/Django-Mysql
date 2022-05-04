# Django에서 SQL 사용기

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

- `App`을 프로젝트에서 인식할수 있도록 `setting.py`애 `INSTALLED_APPS`부분의 `App`이름을 적어 주도록 하겠습니다.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'sql', #App 이름
]
```

## sql 프로젝트 세팅

- 이제 우리의 본 프로젝트인 `mysql`를 `djnago`에서 사용하는 프로젝트를 진행하도록 하겠습니다!

- `mysql`과 `django`를 연결하는 `Databaser Connector`를 설치 하겠습니다.

```py
# Mysql Install Databser Connector
pip install mysqlclient

# MAC Install MysqlClient
brew install mysql-client
echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
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

- `mysql`에 있는 `table`을 python코드로 올려줍니다.

- 나온 코드를 복사해서 `App(sql)`의 `model.py` 넣어주시면 됩니다.

- 왜 넣어주는지는 나중에 설명하도록 하겠습니다.

## Django에서 sql 사용하기

- 그전에 `create`를 통해 테이블을 만들필요가 있습니다.

```sql
CREATE TABLE tmp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT);
```

- `views.py`에서 `create`라는 함수를 만들고 `url(127.0.0.1:8000)`을 들어갈때 `views.py`에 우리가 정의한 함수를 실행 시켜 `table`을 생성하겠습니다.

```py
def sqlExcuter(sql):
    try:
        cursor = connection.cursor() # mysql에 접속을 위한 객체 생성
        result = cursor.execute(sql) # sql을 수행
        datas = cursor.fetchall() # DB에서 수행하고 나온 결과물을 반환

        connection.commit() # DB에 대한 변경사항 확정 및 갱신
        connection.close() # DB 연결 닫음
        return datas

    except Exception as ex:
        connection.rollback()
        return ("Fail to sql, the string is" + sql + "error: " + str(ex))

def create(request):
    mysql = "CREATE TABLE tmp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT);"
    result = sqlExcuter(mysql)
    return HttpResponse(result)
```

- cursor(): cursor 객체 (SQL문을 수행하고 결과를 얻는데 사용하는 객체)생성

- cursor.execute(): 쿼리문을 연결된 DB로 보내 쿼리를 실행

- cursor.fetchall(): 쿼리 실행 결과로 반환된 전체 데이터를 데이터베이스 서버로부터 가져옴

- connection: 데이터베이스에 접속을 하기 위한 모듈

- connection.commit(): 데이터에 대한 변경사항이 있다면 이를 확정, 갱신

- connection.close(): 데이터베이스와의 연결을 닫힘

- connection.rollback(): 쿼리문 실행 도중 잘못된 경우 실행 전으로 되돌려 놓음

- 이제 `Table`에 대한 `CRUD`를 함수들을 만들고 마찬가지로 `views.py`에 우리가 정의한 함수를 실행 시켜 `DB`에 반영해보도록 하겠습니다.

- `views.py`에서 먼저 `CRUD`,함수들은 `sql`만 바꾸고 간단하게 만들었습니다. (해당 sql을 바꾸셔도 상관없습니다)

```py

#Create
def insert(request):
    mysql = " INSERT INTO tmp(ID, Name, age) VALUES(2, 'KUD2', '3'); "
    result = sqlExcuter(mysql)
    return HttpResponse(result)

#Read
def select(request):
    mysql = "select * from tmp;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

#Update
def update(request):
    mysql = "UPDATE tmp SET age = 2002 WHERE id = 1;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)

#Delete
def delete(request):
    mysql = " DELETE FROM tmp WHERE Name = 1;"
    result = sqlExcuter(mysql)
    return HttpResponse(result)
```

- 두번째는 만든 함수들을 호출하는 `url` 4가지를 설정을 해야합니다.

- `url(127.0.0.1:8000)/insert`,`url(127.0.0.1:8000)/update`,`url(127.0.0.1:8000)/delete`,`url(127.0.0.1:8000)/create`

- `urls.py`에서 코드를 작성해 주도록합시다.

```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sql.views.select, name="select"),
    path('insert', sql.views.insert, name="insert"),
    path('update', sql.views.update, name="update"),
    path('delete', sql.views.delete, name="delete"),
    path('create', sql.views.create, name="create"),
]

```

- 이제 해당 코드들을 돌려보면서 이제 데이터들을 확인해보면 `Django`에서 `sql`을 돌려보았습니다.

- 다음 시간부터는 장고의 `ORM`과 `API`에 대한 공부들을 해보도록 하겠습니다.
