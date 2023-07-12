# WHERE TO GO

This project is learning and dedicated to keeping spots on a map. You can add your own places, and they will be displayed on the map as clickable markers, providing further information about each place you added including images.

Test data to enter can be found [here](https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json) and [here](https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json)
## Installation
1. Clone `git clone ...`
2. Install venv `python3 -m venv venv`
3. Activate venv `source venv/bin/python`
4. Install dependencies `pip install -r requirements.txt`
5. Optionally create `.env` file in the project root directory
   * env vars  
     * `DEBUG` - `False` is the default value  
     * `ALLOWED_HOSTS` - list (e.g. *,localhost,website.ru) If `DEBUG` is set to false, this option is required. `[]` is the default value. 
     * `SECRET_KEY` - `REPLACE_ME` is the default value.
6. Make migrations
   * `./manage.py makemigrations`
   * `./manage.py migrate`
7. Run 
   * `./manage.py runserver`
### Admin page access
To access the admin page, you need to follow additional steps:
1. Create super user `./manage.py createsuperuser`
2. Go `/admin` address (e.g. http://127.0.0.1:8000/admin) in browser