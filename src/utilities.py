"""Module for common helper functions"""
import logging
import sys
def logleveler(loglevel_string):
    """map log level common names to python key values"""
    _loglevel = {
        'critical': lambda x: 50,
        'error': lambda x: 40,
        'warning': lambda x: 30,
        'warn': lambda x: 30,
        'info': lambda x: 20,
        'debug': lambda x: 10,
        'notset': lambda x: 0
    }[loglevel_string.lower()](loglevel_string)

    return _loglevel

def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (string or int): minimum loglevel for emitting messages
      'debug','critical,'error','warning','info','debug','notset'
    """
    if type(loglevel) is str:
        _loglevel = logleveler(loglevel)
    else:
        _loglevel = loglevel

    _logger = logging.getLogger(__name__)
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=_loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")
    return _logger
