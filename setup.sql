CREATE DATABASE IF NOT EXISTS `TwitterItems`;

USE `TwitterItems`;


-- Basic table for now
CREATE TABLE IF NOT EXISTS `Tweets`(
    id INTEGER PRIMARY KEY,
    tweet_text VARCHAR(255),
    lang VARCHAR(255),
    location VARCHAR(255)
);

