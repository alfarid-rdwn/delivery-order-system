from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, init_db

# Initialize Flask application
app = Flask(__name__, template_folder="templates", static_folder="static")

# Initialize database
init_db()

@app.route("/")
def index():
    conn = get_connection()
    orders = conn.execute("SELECT * FROM orders").fetchall()
    conn.close()

    return render_template("index.html", orders=orders)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        order_date = request.form.get("order_date")

        conn = get_connection()
        conn.execute(
            "INSERT INTO orders (customer_name, order_date, status) VALUES (?, ?, ?)",
            (customer_name, order_date, "Pending")
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("create_order.html")

@app.route("/update/<int:order_id>")
def update_status(order_id):
    conn = get_connection()
    conn.execute(
        "UPDATE orders SET status = 'Delivered' WHERE order_id = ?",
        (order_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
