import os
import sys

# Vercel runs this as /api/index.py; make project root importable
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app  # noqa: F401 -- Vercel entrypoint, serves "/" (via rewrite) and "/api/index"
