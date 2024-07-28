USE alx_book_store;

CREATE TABLE IF NOT EXISTS Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(250) NOT NULL
);
CREATE TABLE IF NOT EXISTS Books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    author_id INT,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES (author_id)
);
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(250) NOT NULL,
    email VARCHAR(250) NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY(250) REFERENCES(customer_id)
);

CREATE TABLE IF NOT EXISTS order_details(
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY(order_id) REFERENCES(order_id)
    FOREIGN KEY(book_id) REFERENCES(book_id)
);
