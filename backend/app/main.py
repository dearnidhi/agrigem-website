import os
import uuid

from fastapi import BackgroundTasks, Depends, FastAPI, File, Form, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, SessionLocal, engine, get_db
from .email_utils import send_application_email, send_contact_email
from .seed_data import seed_if_empty

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agri Website API")

RESUME_DIR = os.path.join(os.path.dirname(__file__), "uploads", "resumes")
IMAGE_DIR = os.path.join(os.path.dirname(__file__), "uploads", "images")
os.makedirs(RESUME_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)
ALLOWED_RESUME_TYPES = {".pdf", ".doc", ".docx"}
ALLOWED_IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp", ".svg"}

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000")
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")

frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin, "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "uploads")), name="uploads")


def require_admin(x_admin_key: str | None = Header(None)):
    if not ADMIN_API_KEY:
        raise HTTPException(status_code=500, detail="ADMIN_API_KEY not configured on server")
    if x_admin_key != ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing X-Admin-Key header")


@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    try:
        seed_if_empty(db)
    finally:
        db.close()


@app.get("/api/company", response_model=schemas.CompanyInfoOut)
def get_company(db: Session = Depends(get_db)):
    company = db.query(models.CompanyInfo).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company info not found")
    return company


@app.put("/api/company", response_model=schemas.CompanyInfoOut, dependencies=[Depends(require_admin)])
def update_company(payload: schemas.CompanyInfoUpdate, db: Session = Depends(get_db)):
    company = db.query(models.CompanyInfo).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company info not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(company, field, value)
    db.commit()
    db.refresh(company)
    return company


@app.post("/api/upload/image", response_model=schemas.ImageUploadOut, dependencies=[Depends(require_admin)])
def upload_image(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Image must be one of: jpg, jpeg, png, webp, svg")

    stored_filename = f"{uuid.uuid4().hex}{ext}"
    stored_path = os.path.join(IMAGE_DIR, stored_filename)
    with open(stored_path, "wb") as f:
        f.write(file.file.read())

    return {"url": f"{BACKEND_BASE_URL}/uploads/images/{stored_filename}"}


@app.get("/api/banners", response_model=list[schemas.BannerOut])
def get_banners(db: Session = Depends(get_db)):
    return (
        db.query(models.Banner)
        .filter(models.Banner.is_active == True)  # noqa: E712
        .order_by(models.Banner.display_order)
        .all()
    )


@app.post("/api/banners", response_model=schemas.BannerOut, dependencies=[Depends(require_admin)])
def create_banner(payload: schemas.BannerCreate, db: Session = Depends(get_db)):
    banner = models.Banner(**payload.model_dump())
    db.add(banner)
    db.commit()
    db.refresh(banner)
    return banner


@app.put("/api/banners/{banner_id}", response_model=schemas.BannerOut, dependencies=[Depends(require_admin)])
def update_banner(banner_id: int, payload: schemas.BannerUpdate, db: Session = Depends(get_db)):
    banner = db.query(models.Banner).get(banner_id)
    if not banner:
        raise HTTPException(status_code=404, detail="Banner not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(banner, field, value)
    db.commit()
    db.refresh(banner)
    return banner


@app.delete("/api/banners/{banner_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_banner(banner_id: int, db: Session = Depends(get_db)):
    banner = db.query(models.Banner).get(banner_id)
    if not banner:
        raise HTTPException(status_code=404, detail="Banner not found")
    db.delete(banner)
    db.commit()


@app.get("/api/services", response_model=list[schemas.ServiceOut])
def get_services(db: Session = Depends(get_db)):
    return (
        db.query(models.Service)
        .filter(models.Service.is_active == True)  # noqa: E712
        .order_by(models.Service.display_order)
        .all()
    )


@app.post("/api/services", response_model=schemas.ServiceOut, dependencies=[Depends(require_admin)])
def create_service(payload: schemas.ServiceCreate, db: Session = Depends(get_db)):
    service = models.Service(**payload.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@app.put("/api/services/{service_id}", response_model=schemas.ServiceOut, dependencies=[Depends(require_admin)])
def update_service(service_id: int, payload: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    service = db.query(models.Service).get(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(service, field, value)
    db.commit()
    db.refresh(service)
    return service


@app.delete("/api/services/{service_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(models.Service).get(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(service)
    db.commit()


@app.get("/api/gallery", response_model=list[schemas.GalleryImageOut])
def get_gallery(category: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.GalleryImage).filter(models.GalleryImage.is_active == True)  # noqa: E712
    if category:
        query = query.filter(models.GalleryImage.category == category)
    return query.order_by(models.GalleryImage.display_order).all()


@app.post("/api/gallery", response_model=schemas.GalleryImageOut, dependencies=[Depends(require_admin)])
def create_gallery_image(payload: schemas.GalleryImageCreate, db: Session = Depends(get_db)):
    image = models.GalleryImage(**payload.model_dump())
    db.add(image)
    db.commit()
    db.refresh(image)
    return image


@app.put("/api/gallery/{image_id}", response_model=schemas.GalleryImageOut, dependencies=[Depends(require_admin)])
def update_gallery_image(image_id: int, payload: schemas.GalleryImageUpdate, db: Session = Depends(get_db)):
    image = db.query(models.GalleryImage).get(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Gallery image not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(image, field, value)
    db.commit()
    db.refresh(image)
    return image


@app.delete("/api/gallery/{image_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_gallery_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(models.GalleryImage).get(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Gallery image not found")
    db.delete(image)
    db.commit()


@app.get("/api/directors", response_model=list[schemas.DirectorOut])
def get_directors(db: Session = Depends(get_db)):
    return (
        db.query(models.Director)
        .filter(models.Director.is_active == True)  # noqa: E712
        .order_by(models.Director.display_order)
        .all()
    )


@app.post("/api/directors", response_model=schemas.DirectorOut, dependencies=[Depends(require_admin)])
def create_director(payload: schemas.DirectorCreate, db: Session = Depends(get_db)):
    director = models.Director(**payload.model_dump())
    db.add(director)
    db.commit()
    db.refresh(director)
    return director


@app.put("/api/directors/{director_id}", response_model=schemas.DirectorOut, dependencies=[Depends(require_admin)])
def update_director(director_id: int, payload: schemas.DirectorUpdate, db: Session = Depends(get_db)):
    director = db.query(models.Director).get(director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(director, field, value)
    db.commit()
    db.refresh(director)
    return director


@app.delete("/api/directors/{director_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_director(director_id: int, db: Session = Depends(get_db)):
    director = db.query(models.Director).get(director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    db.delete(director)
    db.commit()


@app.post("/api/contact", response_model=schemas.ContactOut)
def create_contact(
    payload: schemas.ContactCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    contact = models.ContactMessage(
        name=payload.name,
        email=payload.email,
        phone=payload.phone,
        subject=payload.subject,
        message=payload.message,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)

    def _send_and_update(contact_id: int):
        sent = send_contact_email(payload.name, payload.email, payload.phone, payload.subject, payload.message)
        if sent:
            session = SessionLocal()
            try:
                row = session.query(models.ContactMessage).get(contact_id)
                if row:
                    row.email_sent = True
                    session.commit()
            finally:
                session.close()

    background_tasks.add_task(_send_and_update, contact.id)
    return contact


@app.get("/api/partners", response_model=list[schemas.PartnerOut])
def get_partners(db: Session = Depends(get_db)):
    return (
        db.query(models.Partner)
        .filter(models.Partner.is_active == True)  # noqa: E712
        .order_by(models.Partner.display_order)
        .all()
    )


@app.post("/api/partners", response_model=schemas.PartnerOut, dependencies=[Depends(require_admin)])
def create_partner(payload: schemas.PartnerCreate, db: Session = Depends(get_db)):
    partner = models.Partner(**payload.model_dump())
    db.add(partner)
    db.commit()
    db.refresh(partner)
    return partner


@app.put("/api/partners/{partner_id}", response_model=schemas.PartnerOut, dependencies=[Depends(require_admin)])
def update_partner(partner_id: int, payload: schemas.PartnerUpdate, db: Session = Depends(get_db)):
    partner = db.query(models.Partner).get(partner_id)
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(partner, field, value)
    db.commit()
    db.refresh(partner)
    return partner


@app.delete("/api/partners/{partner_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_partner(partner_id: int, db: Session = Depends(get_db)):
    partner = db.query(models.Partner).get(partner_id)
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    db.delete(partner)
    db.commit()


@app.get("/api/testimonials", response_model=list[schemas.TestimonialOut])
def get_testimonials(db: Session = Depends(get_db)):
    return (
        db.query(models.Testimonial)
        .filter(models.Testimonial.is_active == True)  # noqa: E712
        .order_by(models.Testimonial.display_order)
        .all()
    )


@app.post("/api/testimonials", response_model=schemas.TestimonialOut, dependencies=[Depends(require_admin)])
def create_testimonial(payload: schemas.TestimonialCreate, db: Session = Depends(get_db)):
    testimonial = models.Testimonial(**payload.model_dump())
    db.add(testimonial)
    db.commit()
    db.refresh(testimonial)
    return testimonial


@app.put("/api/testimonials/{testimonial_id}", response_model=schemas.TestimonialOut, dependencies=[Depends(require_admin)])
def update_testimonial(testimonial_id: int, payload: schemas.TestimonialUpdate, db: Session = Depends(get_db)):
    testimonial = db.query(models.Testimonial).get(testimonial_id)
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(testimonial, field, value)
    db.commit()
    db.refresh(testimonial)
    return testimonial


@app.delete("/api/testimonials/{testimonial_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_testimonial(testimonial_id: int, db: Session = Depends(get_db)):
    testimonial = db.query(models.Testimonial).get(testimonial_id)
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    db.delete(testimonial)
    db.commit()


@app.get("/api/jobs", response_model=list[schemas.JobOpeningOut])
def get_jobs(db: Session = Depends(get_db)):
    return (
        db.query(models.JobOpening)
        .filter(models.JobOpening.is_active == True)  # noqa: E712
        .order_by(models.JobOpening.display_order)
        .all()
    )


@app.post("/api/jobs", response_model=schemas.JobOpeningOut, dependencies=[Depends(require_admin)])
def create_job(payload: schemas.JobOpeningCreate, db: Session = Depends(get_db)):
    job = models.JobOpening(**payload.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@app.put("/api/jobs/{job_id}", response_model=schemas.JobOpeningOut, dependencies=[Depends(require_admin)])
def update_job(job_id: int, payload: schemas.JobOpeningUpdate, db: Session = Depends(get_db)):
    job = db.query(models.JobOpening).get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job opening not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(job, field, value)
    db.commit()
    db.refresh(job)
    return job


@app.delete("/api/jobs/{job_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(models.JobOpening).get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job opening not found")
    db.delete(job)
    db.commit()


@app.post("/api/careers/apply", response_model=schemas.JobApplicationOut)
def apply_for_job(
    background_tasks: BackgroundTasks,
    job_title: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    phone: str | None = Form(None),
    message: str | None = Form(None),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    ext = os.path.splitext(resume.filename or "")[1].lower()
    if ext not in ALLOWED_RESUME_TYPES:
        raise HTTPException(status_code=400, detail="Resume must be a PDF or Word document")

    stored_filename = f"{uuid.uuid4().hex}{ext}"
    stored_path = os.path.join(RESUME_DIR, stored_filename)
    with open(stored_path, "wb") as f:
        f.write(resume.file.read())

    application = models.JobApplication(
        job_title=job_title,
        name=name,
        email=email,
        phone=phone,
        message=message,
        resume_path=stored_path,
    )
    db.add(application)
    db.commit()
    db.refresh(application)

    def _send_and_update(application_id: int):
        sent = send_application_email(job_title, name, email, phone, message, stored_path)
        if sent:
            session = SessionLocal()
            try:
                row = session.query(models.JobApplication).get(application_id)
                if row:
                    row.email_sent = True
                    session.commit()
            finally:
                session.close()

    background_tasks.add_task(_send_and_update, application.id)
    return application
