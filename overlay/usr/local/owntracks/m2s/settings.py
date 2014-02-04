#(@)settings.py

logfile	= '/var/log/mosquitto/m2s.log'		
mqtt_broker = 'localhost'       # default: 'localhost'
mqtt_port = 1883                # default: 1883
mqtt_clientid = 'm2s-backend'   # MUST be set
# mqtt_username = 'jane'
# mqtt_password = 'secret'

# List of topics we should subscribe to
topics = [
        'owntracks/#',
    ]

# optional: if any words in this list are present in a topic
# name, ignore the message

# blocked_topics = [ 'isim', 'jjolie' ]

# Storage
storage_plugin = 'storage.py'
dbname = 'owntracks'
dbuser = 'a'
dbpasswd = 'a'

# data_plugins = None
data_plugins = [
        # dbcolumn=pluginname       path-to-plugin.py
        dict(column='weather',      filename='pl-weather.py'),
        dict(column='revgeo',       filename='pl-revgeo.py'),
]

# The following configuration is made available to plugins through
# the m2s object. A plugin can access
#
#	m2s.cf.replublish_topic   or
#	m2s.cf.name
#	etc.
#
# See pl-republish.py for an example which uses 'republish_topic',
# 'republish_users', 'republish_devices'

plugin_configs = {
	"republish_topic" : "local/loca",
	"republish_users" : [ 'john', ],
	"republish_devices" : [ 'iphone', 'nexus', ],
	"name" : "JP Mens",
}

