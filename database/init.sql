CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS token_blocklist (
    id SERIAL PRIMARY KEY,
    jti VARCHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    artist VARCHAR(200) NOT NULL,
    album VARCHAR(200),
    genre VARCHAR(50),
    year INT,
    duration INT
);

CREATE TABLE IF NOT EXISTS streams (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    song_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duration_listened INT
);

CREATE TABLE IF NOT EXISTS search_queries (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    query VARCHAR(200) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
