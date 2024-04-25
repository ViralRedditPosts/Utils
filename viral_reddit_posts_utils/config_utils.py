from configparser import ConfigParser
import json
import boto3
import os
from collections import defaultdict


def find_config() -> str:
  """
  Finds config file locally

  :return: string of config file location
  """
  # searches for main file, falls back to example file if not found
  home = os.path.expanduser('~')
  file_loc = os.path.join(home, '.reddit.cfg')
  if os.path.exists(file_loc):
    return file_loc
  else:
    raise FileNotFoundError("Reddit config file not found. Place the example config template in your home directory and rename it to '.reddit.cfg'")


DEFAULT_KEYS = {
  'reddit_api': ['CLIENTID', 'CLIENTSECRET', 'PASSWORD', 'USERNAME'],
  'S3_access': ['ACCESSKEY', 'SECRETKEY', ],
  'Discord': ['BOTTOKEN', 'MYSNOWFLAKEID', 'CHANNELSNOWFLAKEID'],
  'Postgres': ['USERNAME', 'PASSWORD', 'HOST', 'PORT', 'DATABASE']
}


def parse_config(
  cfg_file: str,
  keys_to_read: dict = None
) -> dict:
  """
  Read in the config data from a location to a dictionary and return that dictionary.

  :param cfg_file: location of config file. Can be an S3 location
  :param keys_to_read:
  :return: config dictionary
  """
  if keys_to_read is None:
    keys_to_read = DEFAULT_KEYS
  parser = ConfigParser()
  cfg = defaultdict(dict)

  if cfg_file[:2].lower() == 's3':
    s3 = boto3.client('s3')
    path_split = cfg_file.replace('s3://', '').split('/')
    bucket = path_split[0]
    objLoc = '/'.join(path_split[1:])
    obj = s3.get_object(Bucket=bucket, Key=objLoc)
    _ = parser.read_string(obj['Body'].read().decode())
  else:
    _ = parser.read(cfg_file)
  for k, vList in keys_to_read.items():
    for v in vList:
      cfg[k][v] = json.loads(parser.get(k, v))  # json helps with list conversion
  return cfg
