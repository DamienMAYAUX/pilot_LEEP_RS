from os import environ

SESSION_CONFIGS = [
    dict(
        name='pilot_recommandation',
        num_demo_participants=5,
        #app_sequence=['instructions', 'choice_experiment', 'attention_test']
        #app_sequence=['instructions', 'choice_experiment']
        app_sequence=['instructions','choice_experiment', 'conclusion'],
        use_browser_bots = True
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.00066, participation_fee=6, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans

#LANGUAGE_CODE = 'en'
LANGUAGE_CODE = 'fr'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_CUSTOM_NAME = "ECU"

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 's^t&h$x*o&rab#_np0k*fb8a-s2+-+_9s#97=b36j%+af(5gd7'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

