import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getBanners } from "../api";

export default function HeroSlider() {
  const [banners, setBanners] = useState([]);
  const [active, setActive] = useState(0);

  useEffect(() => {
    getBanners().then(setBanners).catch(() => setBanners([]));
  }, []);

  useEffect(() => {
    if (banners.length < 2) return;
    const timer = setInterval(() => {
      setActive((prev) => (prev + 1) % banners.length);
    }, 5500);
    return () => clearInterval(timer);
  }, [banners]);

  if (banners.length === 0) return null;

  const goTo = (i) => setActive((i + banners.length) % banners.length);

  return (
    <section id="home" className="hero">
      {banners.map((banner, i) => (
        <div
          key={banner.id}
          className={`hero-slide ${i === active ? "active" : ""}`}
          style={{ backgroundImage: `url(${banner.image_url})` }}
        >
          <div className="hero-overlay">
            <h1>{banner.title}</h1>
            {banner.subtitle && <p>{banner.subtitle}</p>}
            <Link to="/contact" className="btn btn-primary">
              Contact Us
            </Link>
          </div>
        </div>
      ))}

      {banners.length > 1 && (
        <>
          <button className="hero-arrow hero-arrow-prev" onClick={() => goTo(active - 1)} aria-label="Previous slide">
            ‹
          </button>
          <button className="hero-arrow hero-arrow-next" onClick={() => goTo(active + 1)} aria-label="Next slide">
            ›
          </button>
        </>
      )}

      <div className="hero-dots">
        {banners.map((banner, i) => (
          <button
            key={banner.id}
            className={i === active ? "active" : ""}
            onClick={() => goTo(i)}
            aria-label={`Slide ${i + 1}`}
          />
        ))}
      </div>
    </section>
  );
}
