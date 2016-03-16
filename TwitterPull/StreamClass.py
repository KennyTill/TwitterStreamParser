# Simple data stream of twitter used for pulling data into database
from twitter import TwitterStream, OAuth
import sqlite3


class StreamClass():
    def __init__(self, config):
        self.app_token = config['token']
        self.app_secret = config['token_secret']
        self.consumer_key = config['consumer_key']
        self.consumer_secret = config['consumer_secret']
        self.limiter = config['limiter']
        self.db = sqlite3.connect(config['database_path'])

    def init_db(self):
        with open('setup.sql', 'r') as file:
            sql = file.read()
        c = self.db.executescript(sql)
        c.close()
        self.db.commit()

    def store_data(self, data):
        c = self.db.execute('INSERT INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?)', (data['id'], data['user']['id'], data['user']['screen_name'], data['user']['name'], data['text'], data['user']['location'], data['lang']))
        c.close()
        self.db.commit()

    def run(self):
        # setting up auth from our config.json file
        auth = OAuth(
            self.app_token, self.app_secret,
            self.consumer_key, self.consumer_secret
        )

        # set limiter in config to cap the number of pulled tweets
        limiter = self.limiter
        count = 0

        # connect to default streaming endpoint
        stream = TwitterStream(auth=auth)
        iterator = stream.statuses.sample()

        # our stream loop
        for tweet in iterator:
            # found the key indicating it is a tweet, lets store it into an arbitrary file for now
            if 'in_reply_to_status_id' in tweet:
                if limiter > 0:
                    count += 1
                    print(count)
                    if count > limiter:
                        return

                # Store to sqlite
                self.store_data(tweet)
