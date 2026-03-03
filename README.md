# Django Jinja Template Demo

This project demonstrates the use of Jinja template printing tags in Django to render dynamic content in HTML pages.

## 🚀 Features

- Dynamic HTML rendering using Jinja
- Conditional statements (`if-else`)
- Template variables (`{{ variable }}`)
- Basic Django project structure

## 🛠 Tech Stack

- Python
- Django
- HTML
- Jinja Template Engine

## 📂 Project Structure

project7/
│── app/
│── templates/
│── db.sqlite3
│── manage.py

## 💡 Example Used

```html
{% if age > 18 %}
    <h1>{{ name }} is eligible to drink</h1>
{% else %}
    <h1>{{ name }} is underage</h1>
{% endif %}
