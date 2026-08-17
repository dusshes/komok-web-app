import os
import sys
import subprocess

# Список переменных, которые могут содержать кириллицу и мешать psycopg2
problematic_vars = ['PSMODULEPATH', 'APPDATA', 'LOCALAPPDATA', 'USERPROFILE']

for var in problematic_vars:
    if var in os.environ:
        os.environ[var] = ''

# Запускаем Flask миграции
cmd = [r'.\venv\Scripts\python.exe', '-m', 'flask', 'db', 'upgrade']
subprocess.run(cmd, env=os.environ)
