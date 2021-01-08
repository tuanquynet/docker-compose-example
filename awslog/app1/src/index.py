import os
import time
from shared.logger import warn

print(os.environ.get('CONFIG_MONGODB_USERNAME'))
print(os.environ.get('VAR1'))
print(warn('some potential problem'))

while True:
  time.sleep(10)
  pass