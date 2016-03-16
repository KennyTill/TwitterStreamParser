import json
from StreamClass import *



#check for setup data




# open our json configuration file readonly
with open('config.json', 'r') as configuration_file:
    config = json.load(configuration_file)


streamer = StreamClass(config)
# call init before we begin to process
streamer.init_db()


streamer.run()


