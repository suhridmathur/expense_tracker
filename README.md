# Expense Tracker

Expense Tracker is an application created using Django Framework for tracking of personal expenses and managing finances.

Key Features:
  - Manage Income, Expenses and Investments.
  - Analyse spending patterns.
  - Visualize all statistics

## Technologies Used:

- Python3.8
- Django 3.1
- MySQL

Going forward, we will separate front-end and back-end. We'll be using Django-Rest-Framework & React.JS


## Installation:
- [Install python3.8](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)

- [Install pip3](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)

- [Install Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

- [Install Git](https://linuxize.com/post/how-to-install-git-on-ubuntu-18-04/)

- [Install MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)


Install Python Dependencies:
```bash
sudo apt install python3-dev 
```

Clone the repository using:
```bash
git clone git@github.com:suhridmathur/expense_tracker.git
```
Create environment and install python packages:
```bash
virtualenv -p python3.8 env
pip install -r requirementst.txt
```

Export the following envirnment variables in bashrc:
- EXPENSE_TRACKER_SECRET_KEY
- db_user
- db_password
- db_host
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

Create Migrations
```python
python manage.py migrate
```

Run server:
```python
python manage.py runserver
```
