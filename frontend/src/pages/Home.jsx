import { useEffect, useState } from "react";
import { Link, useOutletContext } from "react-router-dom";
import HeroSlider from "../components/HeroSlider.jsx";
import Partners from "../components/Partners.jsx";
import Testimonials from "../components/Testimonials.jsx";
import { getServices } from "../api";

const ICONS = {
  seed: "🌱",
  spray: "🧴",
  services: "🧑‍🌾",
  equipment: "🚜",
  fertilizer: "🌾",
};

const WHY_US = [
  { icon: "✅", title: "Quality Assured", text: "Every product we sell is checked for originality and quality before it reaches you." },
  { icon: "🤝", title: "Farmer-First", text: "We build our services around what farmers actually need, not the other way around." },
  { icon: "⚡", title: "Modern Approach", text: "A new-age agri startup blending trusted sourcing with tech-driven service." },
  { icon: "🌏", title: "Pan India Reach", text: "From our roots in Gwalior, we offer our products and services across India — empowering farmers nationwide." },
];

export default function Home() {
  const { company } = useOutletContext();
  const [services, setServices] = useState([]);

  useEffect(() => {
    getServices().then(setServices).catch(() => setServices([]));
  }, []);

  return (
    <>
      <HeroSlider />

      <section className="section home-teaser">
        <h2>Welcome to {company?.name || "AgriGem"}</h2>
        {company?.tagline && <p className="home-tagline">{company.tagline}</p>}
        {company?.about && <p className="home-about-snippet">{company.about}</p>}
        <div className="home-teaser-links">
          <Link to="/about" className="btn btn-outline">Who We Are</Link>
          <Link to="/services" className="btn btn-outline">Our Services</Link>
          <Link to="/contact" className="btn btn-primary">Contact Us</Link>
        </div>
      </section>

      <section className="section why-us">
        <h2>Why Choose Us</h2>
        <div className="why-us-grid">
          {WHY_US.map((item) => (
            <div key={item.title} className="why-us-card">
              <div className="why-us-icon">{item.icon}</div>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section certifications">
        <h2>Certifications &amp; Accreditations</h2>
        <p className="cert-subtitle">Our products and processes meet the highest industry standards.</p>
        <div className="cert-grid">
          <div className="cert-card">
            <img src="/images/cibrc.jpeg" alt="CIBRc Certification" />
          </div>
          <div className="cert-card">
            <img src="/images/iso.jpeg" alt="ISO Certification" />
          </div>
        </div>
      </section>

      {services.length > 0 && (
        <section className="section home-services">
          <h2>What We Offer</h2>
          <div className="home-services-grid">
            {services.map((service) => (
              <div key={service.id} className="home-service-pill">
                <span>{ICONS[service.icon] || "🌿"}</span>
                {service.name}
              </div>
            ))}
          </div>
          <div className="home-teaser-links">
            <Link to="/services" className="btn btn-outline">View All Services</Link>
          </div>
        </section>
      )}

      <Partners />

      <Testimonials />

      <section className="home-cta">
        <h2>Ready to grow with AgriGem?</h2>
        <p>Get in touch and let's talk about what your farm needs.</p>
        <Link to="/contact" className="btn btn-primary">Contact Us</Link>
      </section>
    </>
  );
}
