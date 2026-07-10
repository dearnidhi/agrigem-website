import { useRef, useState } from "react";
import { submitApplication } from "../api";

const EMPTY = { name: "", email: "", phone: "", message: "" };

export default function Career() {
  const [form, setForm] = useState(EMPTY);
  const [resume, setResume] = useState(null);
  const [status, setStatus] = useState(null);
  const formRef = useRef(null);
  const fileInputRef = useRef(null);

  const handleChange = (e) =>
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!resume) { setStatus("error"); return; }
    setStatus("sending");
    try {
      const fd = new FormData();
      fd.append("job_title", "Sales Executive");
      fd.append("name", form.name);
      fd.append("email", form.email);
      fd.append("phone", form.phone);
      fd.append("message", form.message);
      fd.append("resume", resume);
      await submitApplication(fd);
      setStatus("success");
      setForm(EMPTY);
      setResume(null);
      if (fileInputRef.current) fileInputRef.current.value = "";
    } catch {
      setStatus("error");
    }
  };

  return (
    <>
      {/* Banner */}
      <div className="career-banner">
        <img src="/images/photos/wheat-harvest.jpg" alt="Careers at AgriGem" />
        <div className="career-banner-overlay">
          <h2>Careers at AgriGem</h2>
          <p>Join a fast-growing team building the future of agriculture</p>
        </div>
      </div>

      <div className="section careers">
        <div className="careers-layout">

          {/* ── Job Description ── */}
          <div className="job-posting">
            <div className="job-card-rich">

              {/* Header */}
              <div className="job-card-header">
                <div>
                  <h3 className="job-title">Sales Executive – AgriGem</h3>
                  <p className="job-company">
                    AgriGem &nbsp;·&nbsp; Agriculture | Seeds | Crop Protection | Plant Nutrition
                  </p>
                </div>
                <div className="job-badges">
                  <span className="job-badge job-badge-location">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                    </svg>
                    Multiple Locations
                  </span>
                  <span className="job-badge job-badge-type">Full-time</span>
                </div>
              </div>

              {/* Body sections */}
              <div className="job-sections">

                <div className="job-section">
                  <h4 className="job-section-heading">About AgriGem</h4>
                  <p className="job-section-para">
                    AgriGem is an integrated agricultural solutions company dedicated to empowering
                    farmers and agri-businesses through quality products, innovative solutions, and
                    expert support. We work closely with dealers, distributors, and farmers to deliver
                    value across the agricultural ecosystem.
                  </p>
                </div>

                <div className="job-section">
                  <h4 className="job-section-heading">Job Summary</h4>
                  <p className="job-section-para">
                    We are looking for a dynamic and result-oriented Sales Executive to drive business
                    growth, strengthen dealer relationships, and expand AgriGem's market presence. The
                    ideal candidate should be self-motivated, proactive, and passionate about
                    agriculture, with a strong commitment to achieving sales targets and delivering
                    excellent customer service.
                  </p>
                </div>

                <div className="job-section">
                  <h4 className="job-section-heading">Key Responsibilities</h4>
                  <ul className="job-section-list">
                    <li>Develop and maintain strong relationships with dealers, distributors, and farmers.</li>
                    <li>Promote and sell AgriGem's portfolio of agricultural products and solutions.</li>
                    <li>Identify new business opportunities and expand market reach.</li>
                    <li>Conduct regular field visits and market surveys to understand customer needs and competitor activities.</li>
                    <li>Achieve assigned sales targets and business objectives.</li>
                    <li>Organize and participate in farmer meetings, demonstrations, and promotional activities.</li>
                    <li>Provide timely market feedback and sales reports to management.</li>
                    <li>Ensure effective product positioning and brand visibility in the assigned territory.</li>
                    <li>Coordinate with internal teams to ensure smooth execution of sales and customer support activities.</li>
                  </ul>
                </div>

                <div className="job-section">
                  <h4 className="job-section-heading">Must-Have Requirements</h4>
                  <ul className="job-section-list">
                    <li>Self-motivated and self-driven personality.</li>
                    <li>Strong communication and interpersonal skills.</li>
                    <li>Willingness to travel extensively within the assigned territory.</li>
                    <li>Dedicated, hardworking, and goal-oriented.</li>
                    <li>Ability to work independently and take ownership of assigned responsibilities.</li>
                    <li>Positive attitude with a strong desire to learn and grow.</li>
                  </ul>
                </div>

                <div className="job-section">
                  <h4 className="job-section-heading">Desired Qualifications</h4>
                  <ul className="job-section-list">
                    <li>B.Sc. Agriculture / M.Sc. Agriculture preferred.</li>
                    <li>Fluency in English (spoken and written).</li>
                    <li>Prior experience in the agriculture, seeds, fertilizers, or crop protection industry will be an added advantage.</li>
                  </ul>
                </div>

                <div className="job-section">
                  <h4 className="job-section-heading">What We Offer</h4>
                  <ul className="job-section-list">
                    <li>Opportunity to work with a fast-growing agricultural solutions company.</li>
                    <li>Professional growth and learning opportunities.</li>
                    <li>Performance-driven work environment.</li>
                    <li>Competitive compensation and incentives.</li>
                  </ul>
                </div>

              </div>

              <div className="job-cta-row">
                <p className="job-cta-text">
                  Join AgriGem and be a part of our mission to empower agriculture through quality,
                  innovation, and expertise. <strong>AgriGem – Empowering Growth.</strong>
                </p>
                <button
                  className="btn btn-primary job-apply-btn"
                  onClick={() => formRef.current?.scrollIntoView({ behavior: "smooth" })}
                >
                  Apply Now
                </button>
              </div>

            </div>
          </div>

          {/* ── Application Form ── */}
          <div className="application-form-wrap" ref={formRef}>
            <h3>Apply Now</h3>
            <p className="apply-subtitle">
              Applying for: <strong>Sales Executive</strong>
            </p>
            <form className="contact-form" onSubmit={handleSubmit}>
              <input
                name="name"
                placeholder="Your Full Name *"
                value={form.name}
                onChange={handleChange}
                required
              />
              <input
                type="email"
                name="email"
                placeholder="Email Address *"
                value={form.email}
                onChange={handleChange}
                required
              />
              <input
                name="phone"
                placeholder="Phone Number"
                value={form.phone}
                onChange={handleChange}
              />
              <textarea
                name="message"
                placeholder="Tell us about yourself (optional)"
                rows={3}
                value={form.message}
                onChange={handleChange}
              />
              <label className="file-input-label">
                Resume / CV (PDF or Word) *
                <input
                  type="file"
                  accept=".pdf,.doc,.docx"
                  onChange={(e) => setResume(e.target.files[0])}
                  ref={fileInputRef}
                  required
                />
              </label>
              {resume && <p className="file-chosen">{resume.name}</p>}
              <button
                type="submit"
                className="btn btn-primary"
                disabled={status === "sending"}
              >
                {status === "sending" ? "Submitting…" : "Submit Application"}
              </button>
              {status === "success" && (
                <p className="form-success">
                  Application submitted! We'll be in touch soon.
                </p>
              )}
              {status === "error" && (
                <p className="form-error">
                  Please fill all required fields and attach a resume.
                </p>
              )}
            </form>
          </div>

        </div>
      </div>
    </>
  );
}
