"""
Setup script for QR Food Ordering System
Initializes the database and creates necessary tables
"""
import os
import sys
from app import app, db
from dotenv import load_dotenv

def setup_database():
    """Initialize database and create all tables"""
    load_dotenv()
    
    print("🔧 Setting up QR Food Ordering System...")
    print("=" * 50)
    
    # Check if DATABASE_URL is set
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        print("❌ ERROR: DATABASE_URL not found in .env file")
        print("Please configure your .env file with PostgreSQL credentials")
        sys.exit(1)
    
    print(f"📊 Database URL: {db_url.split('@')[1] if '@' in db_url else 'Not configured'}")
    
    try:
        with app.app_context():
            # Create all tables
            print("📝 Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Verify tables
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n📋 Created tables: {', '.join(tables)}")
            print("\n" + "=" * 50)
            print("✨ Setup completed successfully!")
            print("\n🚀 You can now run the application with: python app.py")
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure PostgreSQL is running")
        print("2. Verify database 'qr_food_db' exists")
        print("3. Check credentials in .env file")
        print("4. Ensure psycopg2-binary is installed")
        sys.exit(1)

if __name__ == "__main__":
    setup_database()
