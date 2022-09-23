# django-nextjs
## Integrating Django and NextJs

``` bash
docker-compose run django django-admin startproject mynext_project ./app
sudo chown -R $USER:$USER mynext_project manage.py
docker-compose run django python manage.py createsuperuser
```

## Update Pyenv
``` bash
brew update && brew upgrade pyenv
pyenv install --list
pyenv install 3.10.6
pyenv virtualenv 3.10.6 django-next
pyenv shell django-next 
pyenv local django-next 
```

## Visual Studio Cool Stuff
````
pip install black
pip install isort
````
