import os
import subprocess

# Создаем "стерильное" окружение (минимум необходимых переменных)
# Мы исключаем все переменные, которые могут содержать кириллицу
clean_env = {
    'PATH': os.environ.get('PATH', ''),
    'DATABASE_URL': 'postgresql://postgres:password@localhost:5432/komok_db',
    'SECRET_KEY': 'dev-secret-key-123',
    'SQLALCHEMY_TRACK_MODIFICATIONS': 'False'
}

print("Starting Flask in isolated environment...")
# Запускаем Flask
cmd = [r'.\venv\Scripts\python.exe', 'run.py']
subprocess.run(cmd, env=clean_env)
