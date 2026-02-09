from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

orders = []
order_counter = 1

@app.route("/")
def index():
    return render_template("index.html", orders=orders)

@app.route("/create", methods=["GET", "POST"])
def create():
    global order_counter

    if request.method == "POST":
        order = {
            "order_id": order_counter,
            "customer_name": request.form.get("customer_name"),
            "order_date": request.form.get("order_date"),
            "status": "Pending"
        }

        orders.append(order)
        order_counter += 1

        return redirect(url_for("index"))

    return render_template("create_order.html")

@app.route("/update/<int:order_id>")
def update_status(order_id):
    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = "Delivered"
            break

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
