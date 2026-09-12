# -*- coding: utf-8 -*-
"""
Python psignifit - based on Matlab psignifit by Heiko Schütt with help from
Felix Wichmann, Jakob Macke and Stefan Harmeling.
"""
# import here the main function
from .psignifit import psignifit
from .tools import pool_blocks
from ._configuration import Configuration
from ._result import Result

# public submodules; psigniplot is deliberately not imported here, so that
# importing psignifit does not pull in matplotlib. Plotting is opt-in:
# `import psignifit.psigniplot` or `from psignifit import psigniplot`.
from . import sigmoids
from . import tools

__all__ = ['Configuration', 'Result', 'pool_blocks', 'psignifit',
           'sigmoids', 'tools']
