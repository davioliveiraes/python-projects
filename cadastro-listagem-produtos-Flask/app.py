from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []

def calculate_totals():
    total_count = len(products)
    total_sum = sum(product["price"] for product in products)
    return total_count, total_sum

@app.route("/")
def index():
    total_count, total_sum = calculate_totals()
    return render_template("index.html", products=products, total_count=total_count, total_sum=total_sum)


@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        if not name or not price:
            return "Missing name or price", 400
        
        try:
            price = float(price)
        except ValueError:
            return "Invalid input for price", 400

        products.append({"name": name, "price": price})
        return redirect(url_for("index"))

    return render_template("add_product.html")


@app.route("/edit/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = products[product_id]
    if request.method == "POST":
        product["name"] = request.form["name"]
        product["price"] = request.form["price"]

        try:
            product["price"] = float(request.form["price"])
        except ValueError:
            return "Invalid input for price", 400

        return redirect(url_for("index"))

    return render_template("edit_product.html", product=product, product_id=product_id)


@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    del products[product_id]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
