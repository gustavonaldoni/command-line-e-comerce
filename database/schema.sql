CREATE DATABASE ecommerce_db;

USE ecommerce_db;

CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS carts(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS cart_product(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    cart_id INT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(cart_id) REFERENCES carts(id)
);

CREATE TABLE IF NOT EXISTS orders(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ordered_at DATETIME NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    user_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS order_products(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    order_id INT,
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(order_id) REFERENCES orders(id)
);

CREATE TABLE IF NOT EXISTS promotional_codes(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    code CHAR(5) NOT NULL,
    discount_percentage INT NOT NULL,
    status VARCHAR(15) DEFAULT 'unused'
);