# Simple data stream of twitter used for pulling data into database
from twitter import TwitterStream, OAuth
import json
import sqlite3




def run(config):
    # setting up auth from our config.json file
    auth = OAuth(
        config['token'], config['token_secret'],
        config['consumer_key'], config['consumer_secret']
    )

    # set limiter in config to cap the number of pulled tweets
    limiter = config['limiter']
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
                if count > limiter:
                    return

            #Store to sqlite




# open our json configuration file readonly
with open('config.json', 'r') as configuration_file:
    config = json.load(configuration_file)

# setup section


# run section
run(config)
