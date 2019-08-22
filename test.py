import sys
from lib import hi

if __name__ == '__main__':
  assert(sys.version_info[0] == 2)
  assert(hi() == 'hi')
