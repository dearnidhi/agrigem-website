import { useEffect, useState } from "react";
import { getPartners } from "../api";

export default function Partners() {
  const [partners, setPartners] = useState([]);

  useEffect(() => {
    getPartners().then(setPartners).catch(() => setPartners([]));
  }, []);

  if (partners.length === 0) return null;

  const items = [...partners, ...partners];

  return (
    <section className="section partners">
      <h2>Our Brand Partners</h2>
      <p className="partners-subtitle">Trusted brands we work with</p>
      <div className="partners-marquee-wrap">
        <div className="partners-marquee-track">
          {items.map((partner, i) => (
            <div key={i} className="partner-logo-card">
              {partner.logo_url ? (
                <img
                  src={partner.logo_url}
                  alt={partner.name}
                  className="partner-logo-img"
                />
              ) : (
                <span className="partner-logo-fallback">{partner.name}</span>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
