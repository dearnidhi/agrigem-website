import { useEffect, useState } from "react";
import { getTestimonials } from "../api";

export default function Testimonials() {
  const [testimonials, setTestimonials] = useState([]);

  useEffect(() => {
    getTestimonials().then(setTestimonials).catch(() => setTestimonials([]));
  }, []);

  if (testimonials.length === 0) return null;

  return (
    <section className="section testimonials">
      <h2>Customer Testimonials</h2>
      <div className="testimonials-grid">
        {testimonials.map((t) => (
          <div key={t.id} className="testimonial-card">
            {t.photo_url ? (
              <img src={t.photo_url} alt={t.name} className="testimonial-photo" />
            ) : (
              <div className="testimonial-photo testimonial-photo-fallback">
                {t.name.charAt(0).toUpperCase()}
              </div>
            )}
            <p className="testimonial-message">&ldquo;{t.message}&rdquo;</p>
            <p className="testimonial-name">{t.name}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
