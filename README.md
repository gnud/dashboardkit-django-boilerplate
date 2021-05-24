Boilerplate for any dashboard integration
======================

# Features

- Using forms from the UI-kit
- Using other components from the UI-kit
- Having layout + charts
- Table model integration via iommi




# Significant files

- core/templates/iommi_base.html
- core/templates/promotions.html
- core/templates/promotions.html
- core/templates/includes/sidebar.html
- app/views.py MyPage for Products page
- app/views.py IndexPage for Promotions grid page

# Development
## Prepare local env

```bash
virtualenv -p python3.8 venv

. venv/bin/activate

pip install -r requirements.txt
```

## Prepare Django

```bash
./manage.py migrate

./manage.py createsuperuser
```

### Run project

```bash
./manage.py runserver 0.0.0.0:8001
```
