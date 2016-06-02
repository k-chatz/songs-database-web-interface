# MySQL Settings

config = dict(charset='utf8',
              init_command='SET NAMES UTF8',
              host='localhost',
              port=3306,
              user='singer',
              passwd='singer',
              db='songs'
              )

# Webserver Settings
# IMPORTANT: The port must be available.
web_port = 9090  # must be integer (this is wrong:'9090')
