CREATE TABLE ciudades(
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE clientes(
    id SERIAL PRIMARY KEY,
    nombre  Text  NOT null,
    direccion text not null,
    telefono numeric not null,
    correo_electronico text not null
);

CREATE TABLE jugadores(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(60) UNIQUE NOT null,
    dorsal numeric not null
);