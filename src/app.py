from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

# temporary storage (Sprint 3)
orders = []

@app.route("/")
def index():
    return render_template("index.html", orders=orders)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        order = {
            "customer_name": request.form.get("customer_name"),
            "order_date": request.form.get("order_date")
        }

        orders.append(order)

        return redirect(url_for("index"))

    return render_template("create_order.html")

if __name__ == "__main__":
    app.run(debug=True)
