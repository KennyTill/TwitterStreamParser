DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    tweet_id INTEGER,
    tweet_user_id INTEGER,
    tweet_user_screen_name TEXT,
    tweet_user_name TEXT,
    tweet_text TEXT,
    tweet_location TEXT,
    tweet_lang TEXT
);