CREATE TABLE ciudad(
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE NOT NULL
);