#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class LogHouseKepeer:

   def __init__(self, config_file):
      self.config_file = config_file

   def __enter__(self):
#      self.file = open(self.config_file, 'r', encoding='UTF-8')
      with open(self.config_file, 'r') as self.file:
         try:
	    print(yaml.load(stream))
         except yaml.YAMLError as exc:
            print(exc)
#      return self.file

   def __exit__(self, type, msg, traceback):
      if type:
         print(msg)  # 作你的例外處理
      self.file.close()
      return False


if __name__ == '__main__':
   keeper = LogHouseKeeper("config.yml")
   keeper.config()

