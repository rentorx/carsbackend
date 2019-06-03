import yaml

CUSTOM_CONFIG = {
    'django': {
        'debug': False,
        'allowed_hosts': None,
        'ratelimit': None,
    },
    'databases': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    'celery': {
        'synchronous': None
    },
    'secrets': {
        'secret_key': None
    },
    'slack_notifications': {
        'public_channel': None,
        'private_channel': None
    },
    'sentry': {
        'dsn': None,
    },
    'conekta': {
        'secret_key': None,
        'version': None
    }
}


def load_config():
    with open('config/config.yml') as yaml_file:
        user_conf = yaml.load(yaml_file.read(), Loader=yaml.FullLoader)
    conf = {}
    conf.update(CUSTOM_CONFIG)
    for section in user_conf:
        if section in conf:
            conf[section].update(user_conf[section])
    return conf
