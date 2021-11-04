## Curso de RestFul API usando Django Rest Framework

Curso feito na [Udemy](https://www.udemy.com/course/apis-restful-com-django-rest-framework/), ministrado pelo professor Gregory Pacheco.

Resultado deste projeto no [Heroku](https://drf-api-pontos-turisticos.herokuapp.com/).

Repositório do Projeto do Professor no [Github](https://github.com/Gpzim98/pontos-turisticos).   

* #### Para instalar as dependências do projeto basta rodar:    
```
$ pipenv install

$ pipenv run python manage.py makemigrations

$ pipenv run python manage.py migrate

$ pipenv run python manage.py runserver
```

As variáveis de ambiente do _python-decouple_ estão _setadas_ em
**contrib/.env-sample**, devendo ser copiadas para um arquivo *.env* na raíz do projeto.

