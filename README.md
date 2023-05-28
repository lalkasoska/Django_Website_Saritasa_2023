# Places Remember Django Application

## Installation guide

1. Clone the repository
2. Cd to `/PlacesRemember/`
3. Run `pip install -r requrements.txt`
4. Run `python manage.py makemigrations`
5. Run `python manage.py migrate`
6. Run `python manage.py runserver`
7. Open http://127.0.0.1:8000/

## Requirements to be satisfied

- Local Docker Run<br>
  I haven't worked with Docker before and decided to work on other aspects of
  this work more thoroughly instead.
- Running tests on push with GitHub Actions<br>
  I've successfully set up linters but configuring automatic testing led to
  some errors I haven't found a workaround for yet.

## Satified requirements

- The Django applicaiton is built
- Deployed the application on the web service https://railwatdeploy-production.up.railway.app
- PEP 8 coding style
- Relevant packages are used
- Used git during entire development process
- Followed commit style from https://chris.beams.io/posts/git-commit/. (Forgot
  imperative mood at first but started using it later)
- Wrote unit tests for adding and retrieving memories
- Set up flake8 and ruff linting on push with GitHub Actions
- Added badge from https://coveralls.io/ <a href='https://coveralls.io/github/lalkasoska/Django_Website_Saritasa_2023?branch=main'><img src='https://coveralls.io/repos/github/lalkasoska/Django_Website_Saritasa_2023/badge.svg?branch=main' alt='Coverage Status' /></a>
  <br><br>
  ![image](https://github.com/lalkasoska/Django_Website_Saritasa_2023/assets/35616551/e294f3c4-37ee-452b-9ac5-48368728370a)
<br><br>

## Overview

Here's a quick overview of the application
<h2 align="center"> Welcome Page</h2>
<p align="center">
The starting page. Logging in implemented with django-allauth.
<br><br><img src=https://github.com/lalkasoska/Django_Website_Saritasa_2023/assets/35616551/f204a516-4ffe-4004-82e0-88258b55274e><br><br>
</p>

<h2 align="center">Home Page </h2>
<p align="center">
This is the page where a user can find all their memories.
<br><br><img src=https://github.com/lalkasoska/Django_Website_Saritasa_2023/assets/35616551/edc2c713-f5eb-42e8-a70a-9b569b6a1b2b><br><br>
</p>

<h2 align="center">Adding and revisiting a memory</h2>
<p align="center">
This is a page where user can add a new memory. Location selection is implemented with Yandex Maps API.
<br><br><img src=https://github.com/lalkasoska/Django_Website_Saritasa_2023/assets/35616551/50a1d417-0ca4-4c4c-9d54-fc16c0638642><br><br>
After adding the memory it is now displayed at the home page.
<br><br><img src=https://github.com/lalkasoska/Django_Website_Saritasa_2023/assets/35616551/294ad641-3fe6-4f98-b214-31ecabf3961a><br><br>
The user can revisit and change their memories anytime.
<br><br><img src=https://github.com/lalkasoska/Django_Website_Saritasa_2023/assets/35616551/2ffeb032-bcef-4176-98fc-343654b2a9ac><br><br>
</p>




