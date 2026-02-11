import os
import uuid
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# =======================
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =======================
# Database model
# =======================
class Order(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    table_no = db.Column(db.Integer)
    customer_name = db.Column(db.String(100))
    items = db.Column(db.JSON)
    total = db.Column(db.Float)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# =======================
# Home route
# =======================
@app.route("/")
def home():
    return "QR Food Backend is running with PostgreSQL"

# =======================
# Customer: Place Order
# =======================
@app.route("/api/order", methods=["POST"])
def place_order():
    try:
        data = request.json
        
        # Validate required fields
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        required_fields = ["table_no", "customer_name", "items", "total"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Log the incoming order
        print(f"📝 New order received:")
        print(f"   Table: {data['table_no']}")
        print(f"   Customer: {data['customer_name']}")
        print(f"   Items: {data['items']}")
        print(f"   Total: ₹{data['total']}")

        order = Order(
            id=str(uuid.uuid4()),
            table_no=data["table_no"],
            customer_name=data["customer_name"],
            items=data["items"],
            total=data["total"],
            status="Pending"
        )

        db.session.add(order)
        db.session.commit()
        
        print(f"✅ Order saved successfully! ID: {order.id}")
        return jsonify({"message": "Order placed successfully", "order_id": order.id})
    
    except Exception as e:
        print(f"❌ Error placing order: {str(e)}")
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# =======================
# Customer: Check Order Status
# =======================
@app.route("/api/order/<id>/status")
def get_order_status(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({"id": order.id, "status": order.status})

# =======================
# Admin: Get all orders
# =======================
@app.route("/api/admin/orders")
def get_orders():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return jsonify([
        {
            "id": o.id,
            "table_no": o.table_no,
            "customer_name": o.customer_name,
            "items": o.items,
            "total": o.total,
            "status": o.status,
            "created_at": o.created_at
        }
        for o in orders
    ])

# =======================
# Admin: Update Order Status
# =======================
@app.route("/api/admin/order/<id>/status", methods=["POST"])
def update_status(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.status = request.json["status"]
    db.session.commit()
    return jsonify({"message": "Status updated"})

# =======================
# Admin: Remove Order
# =======================
@app.route("/api/admin/order/<id>/remove", methods=["DELETE"])
def remove_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order removed"})

# =======================
# Run app
# =======================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates table if it doesn't exist
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
