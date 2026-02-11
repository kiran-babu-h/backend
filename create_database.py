"""
Script to create the PostgreSQL database
"""
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database():
    try:
        # Connect to PostgreSQL server (not to a specific database)
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="kiran123",
            port=5432
        )
        
        # Set autocommit mode
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        # Create cursor
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='qr_food_db'")
        exists = cursor.fetchone()
        
        if exists:
            print("✅ Database 'qr_food_db' already exists!")
        else:
            # Create database
            cursor.execute("CREATE DATABASE qr_food_db")
            print("✅ Database 'qr_food_db' created successfully!")
        
        cursor.close()
        conn.close()
        
        print("\n🎉 Database is ready!")
        print("📝 Next step: Run 'python setup.py' to create tables")
        
    except psycopg2.OperationalError as e:
        print(f"❌ Connection Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure PostgreSQL is running")
        print("2. Verify password is 'kiran123'")
        print("3. Check if PostgreSQL is on port 5432")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🔧 Creating PostgreSQL Database...")
    print("=" * 50)
    create_database()
