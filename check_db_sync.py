import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def view_recent_orders():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = conn.cursor()
        
        print("\n� Recent Orders in local PostgreSQL:")
        print("-" * 50)
        
        cur.execute('SELECT table_no, customer_name, total, status, created_at FROM "order" ORDER BY created_at DESC LIMIT 5')
        rows = cur.fetchall()
        
        if not rows:
            print("No orders found in the database.")
        else:
            for row in rows:
                print(f"Table: {row[0]} | Customer: {row[1]} | Total: ₹{row[2]} | Status: {row[3]} | Time: {row[4]}")
                
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    view_recent_orders()
