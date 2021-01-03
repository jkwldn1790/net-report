-- schema.sql
-- Since we might run the import many times we'll drop if exists
DROP DATABASE IF EXISTS public;

CREATE DATABASE public;

-- Make sure we're using our `blog` database
\c public;

-- We can create our post table
CREATE TABLE IF NOT EXISTS netresults (
    id SERIAL PRIMARY KEY,
    time VARCHAR(255),
    download numeric,
    upload numeric
);