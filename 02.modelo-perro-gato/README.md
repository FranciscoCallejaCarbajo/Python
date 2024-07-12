## Ringa Tech

- Vídeo: https://www.youtube.com/watch?v=DbwKbsCWPSg&ab_channel=RingaTech
- Colab original: https://colab.research.google.com/drive/1DQc8a-WOTctenvoy5T0lWUXn47EuteCy?usp=sharing
- Repo original: https://github.com/ringa-tech/clasificador-perros-gatos

---

- Mi colab: https://colab.research.google.com/drive/18umqKRDoEy3gbB2ZHi-w68s9Pd-lJjWE?usp=sharing

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
  