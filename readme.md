## Getting started

Start server by running the following command in the virtual environment

```shell
python manage.py runserver localhost:4000
```

## http post and get requests

```shell
http --json :8000/api/leads/ 'name=Jane Williams' 'email=jane@gmail.com' 'message=Please contact Jane'
http --json :8000/api/leads/ 'name=Sam Smith' 'email=sam@gmail.com' 'message=Please contact Sam'
http --json :8000/api/leads/ 'name=John Doe' 'email=jdoe@gmail.com' 'message=Please contact John'
```

List all data entries from the Lead table

```shell
http --json :9000/api/leads/
```

## Fixtures

To dumpdate in yaml format install `pyyaml`

```shell
pip install pyyaml
```

Fixtures for the Lead table in `yaml` format were created with

```shell
python manage.py dumpdata --format yaml leads.lead > ./leads/fixtures/leads.yaml
```
