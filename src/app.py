from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

delivery_orders = []

@app.route('/')
def index():
    return render_template('index.html', orders=delivery_orders)

@app.route('/create', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        order = {
            'order_id': request.form['order_id'],
            'customer_name': request.form['customer_name'],
            'status': 'Pending'
        }
        delivery_orders.append(order)
        return redirect(url_for('index'))

    return render_template('create_order.html')

@app.route('/update/<order_id>')
def update_status(order_id):
    for order in delivery_orders:
        if order['order_id'] == order_id:
            order['status'] = 'Delivered'
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
