from flask import Flask, render_template
from models.collection import Customer

from jinja2 import Template
app = Flask(__name__)

mlab.connect()


def index():
    return render_template('index.html')

@app.route('/customer')
def customer():

    customer_list = []
    customer = Customer.objects(gender = 0, contacted = False
    for index, item in enumerate(customer):
        if index < 10:
            customer_list.append(item)
    return render_template("customer.html",customer = customer_list)

if __name__ == '__main__':
  app.run( debug=True)
