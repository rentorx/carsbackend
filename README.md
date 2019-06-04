# Carsbackend

### System requirements ###

* Python >=3.7.0
* Pip >=3.7.0
* Postgres >=11.1.0
* Redis >=5.0.3

Create a user e.g `createuser mydbuser`  and new data base e.g `createdb mydb`.
Here is a nice [reference](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e) for set the DB.

### Virtual ENV ###

* Install virtual env `pip install virtualenv virtualenvwrapper` please read virtalenvwrapper documentation to fully setup virtual env wrapper.

* Create a virtual environment `mkvirtualenv carservice --python=$(which python3.7)`

* By default the virtual env should be active, for now on when you need to activate the virtual env run `workon xvpn`.

### Repo ###

* Clone the repo `git@github.com:rentorx/carsbackend.git`.

* Move to project `cd carsbackend`.

We use the *github flow* and branch model for development, meaning that we have 3 main branches, `develop`, `staging`, `master` and two branches folders `feature/` and `hotfix/`.

**feature/** here is where a new branch per new feature should be added once ready and tested locally it should be PR/MR to `develop` branch for code review.

**hotfix/** well, what it said, onces tested locally the hot fix should be PR to `develop` for code review in order to get merged.

**develop** we use this branch the main development merge point.

**staging** here where acceptance tests and integration tests are perform.

**master** this is were we archive stable and well tested code. This code is run in production.

I must emphasize that all PR/MR should include **unit/integration tests** and should be manually tested too.

### Project ###

* Install dependencies `pip install -r requirements.txt`.

* Copy configuration sample `cp config/config.yml.sample config/config.yml` and set all appropriated values.

* Run migrations `python manage.py migrate`.

* Create super user `python manage.py createsuperuser`.

* Run server `python manage.py runserver`.
