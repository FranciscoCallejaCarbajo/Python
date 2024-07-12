## Setup

Clonamos y abrimos plantilla:
`git clone https://github.com/andyjud/django-starter.git`

`cd django-starter`

Creamos venv: 
`python -m venv .venv` 

**Nota:** a veces es `py` en Windows

Mac/Linux: `source .venv/bin/activate`

Windows: `<venv>\Scripts\activate`

Instalamos pips:
`pip install -r requirements.txt`

Migraciones + Iniciar Django:
`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

Crear app `a_invoices`:
`django-admin startapp a_invoices`

Crear superuser:
`python manag3.py createsuperuser`

Shell:
`python manage.py shell`
  
  Importar modelos:
  `from a_invoices.models import Cliente, Factura`

  `Cliente.objects.all()`
  
  `Factura.objects.all()`
  