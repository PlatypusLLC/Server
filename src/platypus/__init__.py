# Set up `platypus` as a namespace package.
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
