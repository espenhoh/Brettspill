#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv



def main():
    """Register .env files"""
    env_path = Path('.') / 'brettspill_db/database.env'
    load_dotenv(dotenv_path=env_path, verbose=True)

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brettspill_py.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
