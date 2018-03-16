# Mail Sender

##### 1. Clone this repository

```
cd your/development/folder/
git clone https://github.com/yurabysaha/mail_sender.git
```
##### 2. Сhange gir to project
`cd mail_sender`

##### 3. Create new venv. 

> Open console in project directory and run command:
 
 `python3.6 -m venv venv_sender`

##### 4. Activate venv

##### 5. Install all requirement

`pip install -r requirements.txt`

##### 6. Create new database in your local Postgres

##### 7. Create migrations

`./manage.py makemigrations`

##### 8. Apply all migrations

`./manage.py migrate`
