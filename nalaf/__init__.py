import configparser
import pkg_resources
import os
import sys

config = configparser.ConfigParser()

# if there is a local config.ini file use that
if os.path.exists('config.ini'):
    config.read('config.ini')
# otherwise use the default config.ini file
else:
    config.read(pkg_resources.resource_filename('nalaf.data', 'default_config.ini'))

def _print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

print_warning = _print_err
print_verbose = _print_err if config.getboolean('print', 'verbose', fallback=False) else lambda *a, **k: None
print_debug = _print_err if config.getboolean('print', 'debug', fallback=False) else lambda *a, **k: None
