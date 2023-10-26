#import ast
#import redis
#import os



#if bool(os.environ.get("WEBHOOK", False)):
#    from sample_config import Config
#else:
  #  from config import Config

#INFO = Config.REDIS_URI.split(":")

#DB = redis.StrictRedis(
   # host=INFO[0],
   # port=INFO[1],
   # password=Config.REDIS_PASS,
   # charset="utf-8",
   # decode_responses=True,
#)

#def get_stuff(WHAT):
   # n = []
    #cha = DB.get(WHAT)
  #  if not cha:
    #    cha = "{}"
   # n.append(ast.literal_eval(cha))
   # return n[0]


# Split the URL at "://"
#url_parts = Config.REDIS_URI.split("://")

# Split the second part (after "://") using ":"
#host_port_parts = url_parts[1].split(":")

# Extract host and port
#host = host_port_parts[0]
#port = int(host_port_parts[1])

#DB = redis.StrictRedis(
 #   host=host,
#    port=port,
 #   password=Config.REDIS_PASS,
#    charset="utf-8",
#    decode_responses=True,
#)

#def get_stuff(WHAT):
#    n = []
 #   cha = DB.get(WHAT)
 #   if not cha:
  #      cha = "{}"
   # n.append(ast.literal_eval(cha))
   # return n[0]


import ast
import redis
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# Split the URL at "://"
url_parts = Config.REDIS_URI.split("://")

# Split the second part (after "://") using "@"
host_port_password_parts = url_parts[1].split("@")
host_and_port = host_port_password_parts[1]

# Split the host and port
host, port = host_and_port.split(":")

# Extract the password
password = host_port_password_parts[0]

DB = redis.StrictRedis(
    host=host,
    port=int(port),
    password=password,
    charset="utf-8",
    decode_responses=True,
)

def get_stuff(WHAT):
    n = []
    cha = DB.get(WHAT)
    if not cha:
        cha = "{}"
    n.append(ast.literal_eval(cha))
    return n[0]
