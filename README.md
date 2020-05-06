# python-lambda-read-rds

## how to make upload file for lambda

```command_line.sh
sh make_upload.sh
```

## set up local environment

```command_line.sh
source config/local
```

## set up lambda environment

```command_line.sh
source config/lambda
```

## check code style

```command_line.sh
python -B -m pylint --rcfile=.pylintrc -f parseable `find app -name "*.py" -not -path "app/tests"`
```

## unittest

```command_line.sh
python -B -m unittest discover tests
```

## example for running in local

```command_line.sh
python -m venv .venv
source .venv/bin/activate
source config/local
pip install -r app/requirements.txt
python app/lambda_function.py
```
