mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


makemessages:
	python3 manage.py makemessages -l ru
	python3 manage.py makemessages -l en

compilemessages:
		python3 manage.py compilemessages --ignore=env