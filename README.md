# NITH Announcements
This API fetches the announcements from the [NITH Website](https://www.nith.ac.in) which can further be used in any discord bots or things like that.

Deployed on Vercel (Deta is discontinued). Endpoints:

- `GET /` → list of announcements (legacy path)
- `GET /api/announcements` → list of announcements
- `GET /announcements` → alias
- `GET /docs` → Swagger UI

## Local dev

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deploy to Vercel

```bash
npm i -g vercel
vercel
```

No build settings needed — `api/index.py` + `vercel.json` handle routing.
