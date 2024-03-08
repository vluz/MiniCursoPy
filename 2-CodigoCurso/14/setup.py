from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["pygame","simpleaudio"], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('game.py', base=base, target_name = 'pares')
]

setup(name='Pares',
      version = '1.0',
      description = 'Encontra os pares!',
      options = {'build_exe': build_options},
      executables = executables)
