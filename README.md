# AgriGem Website

Official website for **AgriGem** — an integrated agricultural solutions company based in Gwalior, MP, India.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, Vite, React Router v6 |
| Backend | Python 3, FastAPI, SQLAlchemy |
| Database | SQLite |
| Email | SMTP (BigRock cPanel — info@agrigem.in) |
| Hosting | BigRock cPanel (Frontend) + Render (Backend) |

---

## Project Structure

```
agrigem-website/
├── frontend/          # React + Vite app
│   ├── src/
│   │   ├── components/   # Navbar, Footer, Banner, etc.
│   │   ├── pages/        # Home, About, Services, Careers, Contact
│   │   └── api.js        # API calls to backend
│   ├── public/
│   │   └── images/       # Brand logos, banners, icons
│   └── vite.config.js
│
└── backend/           # FastAPI Python app
    ├── app/
    │   ├── main.py        # FastAPI app + all routes
    │   ├── models.py      # SQLAlchemy models
    │   ├── schemas.py     # Pydantic schemas
    │   ├── database.py    # DB connection
    │   ├── seed_data.py   # Initial data
    │   └── email_utils.py # SMTP email sender
    ├── requirements.txt
    └── .env               # Environment variables (not committed)
```

---

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Create `backend/.env`:
```
SMTP_HOST=sh00009.bigrock.com
SMTP_PORT=465
SMTP_USER=info@agrigem.in
SMTP_PASSWORD=your_password
SMTP_FROM=info@agrigem.in
CONTACT_TO_EMAIL=info@agrigem.in
FRONTEND_ORIGIN=http://localhost:5173
BACKEND_BASE_URL=http://localhost:8000
ADMIN_API_KEY=your_api_key
```

Start backend:
```bash
uvicorn app.main:app --reload
```

Backend runs at: `http://localhost:8000`

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## Environment Variables

### Backend (`backend/.env`)

| Variable | Description |
|----------|-------------|
| `SMTP_HOST` | SMTP server hostname |
| `SMTP_PORT` | SMTP port (465 for SSL) |
| `SMTP_USER` | SMTP login email |
| `SMTP_PASSWORD` | SMTP password |
| `SMTP_FROM` | Sender email address |
| `CONTACT_TO_EMAIL` | Where contact/career emails are sent |
| `FRONTEND_ORIGIN` | Allowed CORS origin |
| `ADMIN_API_KEY` | API key for admin routes |

### Frontend (`frontend/.env.production`)

| Variable | Description |
|----------|-------------|
| `VITE_API_BASE_URL` | Backend API base URL (set to Render URL on production) |

---

## Features

- Home page with animated banner slider
- About page (company info, vision, mission)
- Services page (Seeds, Pesticides, Fertilizers, Agronomy)
- Brand Partners section (29 partner logos)
- Careers page with job listings and CV upload form
- Contact page with enquiry form
- Emails sent to `info@agrigem.in` on form submissions
- Fully responsive design

---

## Deployment

### Backend — Render
1. Push code to GitHub
2. Create new **Web Service** on [render.com](https://render.com)
3. Connect GitHub repo → select `backend/` as root directory
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables in Render dashboard

### Frontend — BigRock cPanel
1. Set `VITE_API_BASE_URL=https://your-render-url.onrender.com/api` in `frontend/.env.production`
2. Run `npm run build` in `frontend/`
3. Upload `dist/` contents to `public_html` on BigRock File Manager

---

## Contact

**AgriGem** (NYCC Industries Pvt. Ltd.)
Orchid Tower, Maharana Pratap Nagar, Lashkar, Gwalior, MP — 474009
Email: info@agrigem.in
CIN: U46692MP2025PTC077628
