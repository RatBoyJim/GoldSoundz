DROP TABLE albums;
DROP labels;

CREATE TABLE labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    label VARCHAR(255),
    amount_units INT,
    ideal_units INT,
    cost FLOAT,
    sell_price FLOAT
    genre VARCHAR(255),
    label_id INT REFERENCES labels(id)
);
