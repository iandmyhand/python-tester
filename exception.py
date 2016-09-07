import sys


try:
    int('string')
except ValueError:
    e = sys.exc_info()[1]
    print(str(e))
    raise e
