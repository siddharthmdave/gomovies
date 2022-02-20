Gomovies system designed to manage movies and shows details.
Provides below basic API to manage and get movie details

Installation Details

> Set up a virtual environment	
    python3 -m venv env
> Activate the virtual environment	
    source env/bin/activate
> Install dependencies
    python -m pip freeze > requirements.txt
> Create database tables
    python manage.py makemigrations
    python manage.py migrate
> Start Project 
    python manage.py runserver


API details.
1. Get Movie shows available in City
    /api/movies_list?City=<CityName>

2. Get all movies 
    /api/movies

3. Get Movies by name
    /api/movies?title=<MovieName>

4. Update Movie Details
    /api/movies

