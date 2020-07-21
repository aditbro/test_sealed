import os
import yaml

env = os.environ['API_ENV']
config_file = open('config.yaml', 'r')
config = yaml.safe_load(config_file)
config_file.close()

for key, val in config[env].items():
    print('export {}={}'.format(key, val))
