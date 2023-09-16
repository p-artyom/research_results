WORKDIR = backend
MANAGE = python $(WORKDIR)/manage.py

run:
	$(MANAGE) runserver

style:
	black -S -l 79 $(WORKDIR)/
	isort $(WORKDIR)/
	flake8 $(WORKDIR)/

super:
	$(MANAGE) createsuperuser

makemig:
	$(MANAGE) makemigrations

mig:
	$(MANAGE) migrate

test:
	$(MANAGE) test
