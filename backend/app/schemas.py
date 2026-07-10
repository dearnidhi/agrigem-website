from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class CompanyInfoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    tagline: Optional[str] = None
    about: Optional[str] = None
    vision: Optional[str] = None
    mission: Optional[str] = None
    address: Optional[str] = None
    phone_primary: Optional[str] = None
    phone_secondary: Optional[str] = None
    email: Optional[str] = None
    facebook_url: Optional[str] = None
    instagram_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    whatsapp_number: Optional[str] = None
    whatsapp_url: Optional[str] = None
    map_embed_url: Optional[str] = None
    cin: Optional[str] = None


class CompanyInfoUpdate(BaseModel):
    name: Optional[str] = None
    tagline: Optional[str] = None
    about: Optional[str] = None
    vision: Optional[str] = None
    mission: Optional[str] = None
    address: Optional[str] = None
    phone_primary: Optional[str] = None
    phone_secondary: Optional[str] = None
    email: Optional[str] = None
    facebook_url: Optional[str] = None
    instagram_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    whatsapp_number: Optional[str] = None
    whatsapp_url: Optional[str] = None
    map_embed_url: Optional[str] = None
    cin: Optional[str] = None


class PartnerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    logo_url: Optional[str] = None
    website_url: Optional[str] = None
    display_order: int
    is_active: bool


class PartnerCreate(BaseModel):
    name: str
    logo_url: Optional[str] = None
    website_url: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class PartnerUpdate(BaseModel):
    name: Optional[str] = None
    logo_url: Optional[str] = None
    website_url: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class TestimonialOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    photo_url: Optional[str] = None
    message: str
    display_order: int
    is_active: bool


class TestimonialCreate(BaseModel):
    name: str
    photo_url: Optional[str] = None
    message: str
    display_order: int = 0
    is_active: bool = True


class TestimonialUpdate(BaseModel):
    name: Optional[str] = None
    photo_url: Optional[str] = None
    message: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class JobOpeningOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    location: Optional[str] = None
    job_type: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    display_order: int
    is_active: bool


class JobOpeningCreate(BaseModel):
    title: str
    location: Optional[str] = None
    job_type: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class JobOpeningUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class JobApplicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    job_title: str
    name: str
    email: str
    phone: Optional[str] = None
    message: Optional[str] = None
    email_sent: bool
    created_at: datetime


class BannerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    subtitle: Optional[str] = None
    image_url: Optional[str] = None
    display_order: int
    is_active: bool


class BannerCreate(BaseModel):
    title: str
    subtitle: Optional[str] = None
    image_url: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class BannerUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    image_url: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class ServiceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None
    display_order: int
    is_active: bool


class ServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class GalleryImageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_url: str
    category: str
    caption: Optional[str] = None
    display_order: int
    is_active: bool


class GalleryImageCreate(BaseModel):
    image_url: str
    category: str = "premises"
    caption: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class GalleryImageUpdate(BaseModel):
    image_url: Optional[str] = None
    category: Optional[str] = None
    caption: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class DirectorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    designation: Optional[str] = None
    photo_url: Optional[str] = None
    bio: Optional[str] = None
    facebook_url: Optional[str] = None
    instagram_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    whatsapp_number: Optional[str] = None
    display_order: int
    is_active: bool


class DirectorCreate(BaseModel):
    name: str
    designation: Optional[str] = None
    photo_url: Optional[str] = None
    bio: Optional[str] = None
    facebook_url: Optional[str] = None
    instagram_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    whatsapp_number: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class DirectorUpdate(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    photo_url: Optional[str] = None
    bio: Optional[str] = None
    facebook_url: Optional[str] = None
    instagram_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    whatsapp_number: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class ImageUploadOut(BaseModel):
    url: str


class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: Optional[str] = None
    message: str


class ContactOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    phone: Optional[str] = None
    subject: Optional[str] = None
    message: str
    email_sent: bool
    created_at: datetime
