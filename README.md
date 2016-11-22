# django.video

[django.video](http://django.video) 📹 is a collection of curated videos about the [Django Web Framework](https://www.djangoproject.com) put together by people from **[rmotr.com](https://rmotr.com)** 🐶.

Learn more the ideas behind it in our [about page](http://django.video/about).

# Development docs

This project is also intended to be used as a learning resource. So here are the first basic setup steps. We're using Python 3.5, but it should properly work on any major Python version.

## Installation

##### Clone the project

`$ git clone https://github.com/rmotr/django-video.git`

##### Create a virtualenv

_(Feel free to remove the -p argument to use your default Python installed version)_
`$ mkvirtualenv django-video -p $(which python3.5)`

##### Install dependencies

`$ pip install -r requirements.txt`

##### Configure your envrionment variables

For it to work properly and without many headaches, `DJANGO_SETTINGS_MODULE` should be `django_video.settings.base` and `PYTHONPATH` should be pointing to `django_video`. You can automate this by adding the following lines to the `postactivate` file of your virtualenv (located in `.virtualenvs/django-video/bin/postactivate`):

```
export OLD_PYTHONPATH=${PYTHONPATH}

export PYTHONPATH=/Users/[YOUR-USER]/[YOUR-PATH]/django-video/django_video:${PYTHONPATH}

export DJANGO_SETTINGS_MODULE=django_video.settings.base
```

And this to `postdeactivate`:

```
unset DJANGO_SETTINGS_MODULE

export PYTHONPATH=${OLD_PYTHONPATH}

unset OLD_PYTHONPATH
```

##### Run migrations

`$ django-admin migrate`

##### Run the development server

`$ django-admin runserver`
