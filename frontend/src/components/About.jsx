export default function About({ company }) {
  if (!company) return null;

  const aboutParagraphs = company.about
    ? company.about.split("\n\n").filter(Boolean)
    : [];

  return (
    <>
      <div className="about-banner">
        <img src="/images/photos/wheat-harvest.jpg" alt="Farmer with harvest" />
        <div className="about-banner-overlay">
          <h2>Who We Are</h2>
        </div>
      </div>

      <section id="about" className="section about">
        <div className="about-body">
          {aboutParagraphs.map((para, i) => (
            <p key={i} className="about-text">{para}</p>
          ))}
          <p className="about-tagline">AgriGem – Empowering Growth.</p>
        </div>

        <div className="about-grid">
          {company.vision && (
            <div className="about-card">
              <h3>Our Vision</h3>
              <p>{company.vision}</p>
            </div>
          )}
          {company.mission && (
            <div className="about-card">
              <h3>Our Mission</h3>
              <p>{company.mission}</p>
            </div>
          )}
        </div>
      </section>
    </>
  );
}
