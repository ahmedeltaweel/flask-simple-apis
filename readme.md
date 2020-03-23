Flask simple APIs
======

Simple Flask app that exposes 3 apis for handling items and bids on those items.

```

GET /api/v1/items/
GET /api/v1/items/<id>/
GET /api/v1/items/<id>/bids/
POST /api/v1/v1/items/bid/
{'item_id', 'bid_amount', 'user_id'}

```

To up and run this app, a few dependencies need to be installed:

- Make sure python3 is installed and running.
- Make sure that a good package manager is installed like [pip3](https://pip.pypa.io/en/stable/installing/) is installed.
- Install an environment isolation tool like [Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


Once the upper requirements are installed lets up and run the app:

- create a virtualenv using this command `virtualenv -p python3 venv`
- Activate the venv by using `source venv/bin/activate`
- Install Flask version 1.1.1 using `pip install flask==1.1.1`
- once done run the main file using `python3 main.py`
- You can now access the API on `0.0.0.0:8888`

## Resources 

- [Intor to Flask](https://realpython.com/flask-by-example-part-1-project-setup/)
