-- PostgreSQL Database Schema for QR Food Ordering System
-- Run this file to manually create the database structure

-- Create database (run this separately)
-- CREATE DATABASE qr_food_db;

-- Connect to the database
\c qr_food_db;

-- Create orders table
CREATE TABLE IF NOT EXISTS "order" (
    id VARCHAR(36) PRIMARY KEY,
    table_no INTEGER NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    items JSON NOT NULL,
    total FLOAT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_order_status ON "order"(status);
CREATE INDEX IF NOT EXISTS idx_order_created_at ON "order"(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_order_table_no ON "order"(table_no);

-- Sample data (optional)
-- INSERT INTO "order" (id, table_no, customer_name, items, total, status)
-- VALUES 
--     ('550e8400-e29b-41d4-a716-446655440000', 1, 'John Doe', '["Masala Dosa (2)", "Tea (1)"]', 120.0, 'Pending'),
--     ('550e8400-e29b-41d4-a716-446655440001', 2, 'Jane Smith', '["Chicken Biryani (1)", "Mango Lassi (1)"]', 170.0, 'Served');

-- Grant permissions (adjust username as needed)
-- GRANT ALL PRIVILEGES ON DATABASE qr_food_db TO postgres;
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
