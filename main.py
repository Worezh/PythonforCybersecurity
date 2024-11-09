import math
import os
import codecs
import re
import configparser

config = configparser.ConfigParser()
config['APIKeys'] = {'GitHub': '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'}
with open('C:/Users/Rexh/Desktop/GRC/IT102 - Scripting for Cybersecurity/secrets.ini', 'w') as configfile:
  config.write(configfile)
