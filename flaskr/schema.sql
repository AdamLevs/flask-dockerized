-- Drop existing tables if they exist
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS "user";

-- Create user table
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Create post table
CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL REFERENCES "user"(id),
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL
);