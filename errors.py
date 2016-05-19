__author__ = 'nico'

import sys

py3 = sys.version_info[0] == 3

if py3:
    base_exception_class = Exception
else:
    base_exception_class = StandardError


class UnknownTypeError(base_exception_class):
    pass


class ConcurrentModificationError(base_exception_class):
    pass


# internal exceptions

class KeyDeletedError(base_exception_class):
    pass


class KeyTypeChangedError(base_exception_class):
    pass
