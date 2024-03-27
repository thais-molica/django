Para criar um ambiente virtual
`python3 -m venv <nome_do_env>`
Para ativar ambiente virtual
`. venv/bin/activate`
Para sair do ambiente virtual 
`deactivate`
Para criar a aplicação (toda a solução)
` django-admin startproject <nome>`
Para subir aplicação
`python3 manage.py runserver`

Para criar app (sessão django/módulos)
`django-admin startapp <nome-da-aplicacao>`
Criar migration para novo model
`python3 manage.py makemigrations my_app`
Mostra as migrações
`python3 manage.py showmigrations`