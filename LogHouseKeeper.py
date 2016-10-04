#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class LogHouseKeeper:

   def __init__(self, config_file):
      self.config_file = config_file
      self.yaml_stream = ''

   def __enter__(self):
      with open(self.config_file, 'r') as stream:
         try:
            self.yaml_stream = yaml.load(stream)
         except yaml.YAMLError as exc:
            print(exc)
      return self

   def __exit__(self, type, msg, traceback):
      if type:
         print(msg)
      return False

   def printConfig(self):
      print(self.yaml_stream)

if __name__ == '__main__':
   with LogHouseKeeper("config.yml") as keeper:
      #print(keeper.yaml_stream)
      keeper.printConfig()

