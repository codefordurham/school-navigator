#!/usr/bin/env python
import os
import sys

import dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '')
dotenv_path = os.path.join(APP_ROOT, '.env')
dotenv.load_dotenv(dotenv_path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_navigator.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
