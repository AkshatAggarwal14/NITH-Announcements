import os
import sys

# Vercel runs this as /api/announcements.py; make project root importable
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app  # noqa: F401 -- Vercel entrypoint, serves "/announcements" (via rewrite) and "/api/announcements"
