from pathlib import Path
import yaml

YAML_FILE = Path('config.yaml')

if not YAML_FILE.parent.exists():
    YAML_FILE.parent.mkdir(parents=True)

if not YAML_FILE.exists():
    _config = {
        'server': {
            'hostname': 'localhost',
            'port': 1883,
            'office_sub_topic': '/home/device',
            'office_pub_topic': '/office/device',
            'home_sub_topic': '/office/device',
            'home_pub_topic': '/home/device'
        }
    }
    with open(YAML_FILE, 'w') as f:
        yaml.dump(_config, f)
else:
    with open(YAML_FILE, 'r') as f:
        _config = yaml.safe_load(f)


class Server:
    HOSTNAME = _config['server']['hostname']
    PORT = _config['server']['port']
    OFFICE_SUB_TOPIC = _config['server']['office_sub_topic']
    OFFICE_PUB_TOPIC = _config['server']['office_pub_topic']
    HOME_SUB_TOPIC = _config['server']['home_sub_topic']
    HOME_PUB_TOPIC = _config['server']['home_pub_topic']
