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
            'subscribe_topic': '/home/device',
            'publish_topic': '/office/device'
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
    SUBSCRIBE_TOPIC = _config['server']['subscribe_topic']
    PUBLISH_TOPIC = _config['server']['publish_topic']
