import { useEffect, useState } from "react";
import { getServices } from "../api";

const PHOTOS = {
  seed: "/images/photos/grain-bundle.jpg",
  spray: "/images/photos/pesticide-spray.jpg",
  services: "/images/photos/wheat-harvest.jpg",
  equipment: "/images/photos/tractor.jpg",
  fertilizer: "/images/photos/rice-planting.jpg",
};

export default function Services() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    getServices().then(setServices).catch(() => setServices([]));
  }, []);

  if (services.length === 0) return null;

  return (
    <section id="services" className="section services">
      <h2>Our Services</h2>
      <div className="services-grid">
        {services.map((service) => (
          <div key={service.id} className="service-card">
            {PHOTOS[service.icon] && (
              <img src={PHOTOS[service.icon]} alt={service.name} className="service-photo" />
            )}
            <h3>{service.name}</h3>
            <p>{service.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
