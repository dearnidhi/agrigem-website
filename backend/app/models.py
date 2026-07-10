from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func

from .database import Base


class CompanyInfo(Base):
    __tablename__ = "company_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tagline = Column(String)
    about = Column(Text)
    vision = Column(Text)
    mission = Column(Text)
    address = Column(String)
    phone_primary = Column(String)
    phone_secondary = Column(String)
    email = Column(String)
    facebook_url = Column(String)
    instagram_url = Column(String)
    linkedin_url = Column(String)
    whatsapp_number = Column(String)
    whatsapp_url = Column(String)
    map_embed_url = Column(String)
    cin = Column(String)


class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    logo_url = Column(String)
    website_url = Column(String)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class Testimonial(Base):
    __tablename__ = "testimonials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    photo_url = Column(String)
    message = Column(Text, nullable=False)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class JobOpening(Base):
    __tablename__ = "job_openings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    location = Column(String)
    job_type = Column(String)
    description = Column(Text)
    requirements = Column(Text)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    message = Column(Text)
    resume_path = Column(String)
    email_sent = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Banner(Base):
    __tablename__ = "banners"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    subtitle = Column(String)
    image_url = Column(String)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    icon = Column(String)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class GalleryImage(Base):
    __tablename__ = "gallery_images"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    category = Column(String, default="premises")
    caption = Column(String)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    designation = Column(String)
    photo_url = Column(String)
    bio = Column(Text)
    facebook_url = Column(String)
    instagram_url = Column(String)
    linkedin_url = Column(String)
    whatsapp_number = Column(String)
    whatsapp_url = Column(String)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    subject = Column(String)
    message = Column(Text, nullable=False)
    email_sent = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
