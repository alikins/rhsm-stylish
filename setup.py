
from setuptools import setup

setup(name="rhsm-stylish",
      version="1.0",
      description="code style checkr for rhsm python tools",
      py_modules=["rhsm_stylish"],
      entry_points={'flake8.extension':
                    [
                     'R80 = rhsm_stylish:rhsm_localization_strings',
                     'R81 = rhsm_stylish:rhsm_except_format',
                     'R82 = rhsm_stylish:rhsm_except_format_assert',
                     'R83 = rhsm_stylish:rhsm_import_alphabetical',
                     'R84 = rhsm_stylish:rhsm_no_debugger',
                     'R85 = rhsm_stylish:rhsm_editor_fluff',
                     'R = rhsm_stylish:RhsmStylish']}
      )
