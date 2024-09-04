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

print(_config.server)