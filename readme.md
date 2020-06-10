## Getting started

Start server by running the following command in the virtual environment

```shell
python manage.py runserver localhost:4000
```

## Create http post and get requests

```shell
http :4000/api/leads/ 'name=Jane Williams' 'email=jane@gmail.com' 'message=Please contact Jane'
http :4000/api/leads/ 'name=Sam Smith' 'email=sam@gmail.com' 'message=Please contact Sam'
http :4000/api/leads/ 'name=John Doe' 'email=jdoe@gmail.com' 'message=Please contact John'
```

List all data entries from the Lead table

```shell
http :4000/api/leads/
```

## Delete leads

For example, if you want to remove lead with the id 3, do the following

```shell
http DELETE :4000/api/leads/3/
```

## Fixtures

You can restore model data from fixtures by running the following command

```shell
python manage.py loaddata leads
```

To dumpdate in yaml format install `pyyaml`

```shell
pip install pyyaml
```

Fixtures for the Lead table in `yaml` format were created with

```shell
python manage.py dumpdata --format yaml leads.lead > ./leads/fixtures/leads.yaml
```
