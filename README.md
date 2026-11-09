# Back-end-Development-Capstone

IBM Back-End Development capstone: a Django band website connected to Flask Pictures and MongoDB Songs microservices.

## Features
Home, song lyrics modals, photo gallery, registration/login/logout, concert listings and per-user attendance; Concert and ConcertAttending are registered in Django admin.

## Run
```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
export SONGS_SERVICE_URL=http://127.0.0.1:5000
export PICTURES_SERVICE_URL=http://127.0.0.1:5001
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
Use a deployment-specific DJANGO_SECRET_KEY. Optional container admin creation reads DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD from the environment.

## Validation
`python manage.py test concert -v 2` passed all four integration tests in IBM Skills Network: home/protected pages, signup/login/logout, service data rendering, and per-user attendance. Migrations completed and `python manage.py check` reported no issues.

## Related services
- https://github.com/rustamprogrammer/Back-End-Development-Pictures
- https://github.com/rustamprogrammer/Back-End-Development-Songs

## Container deployment
```sh
docker build -t us.icr.io/sn-labs-rustamzharky/djangoserver:latest .
docker push us.icr.io/sn-labs-rustamzharky/djangoserver:latest
kubectl apply -f deployment.yml
```
Set SONGS_SERVICE_URL and PICTURES_SERVICE_URL on the deployment to the deployed microservice URLs. This is an educational deployment with SQLite.
