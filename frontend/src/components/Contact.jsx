import { useState } from "react";
import { sendContact } from "../api";

const EMPTY_FORM = { name: "", email: "", phone: "", subject: "", message: "" };

export default function Contact({ company }) {
  const [form, setForm] = useState(EMPTY_FORM);
  const [status, setStatus] = useState(null); // "sending" | "success" | "error"

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("sending");
    try {
      await sendContact(form);
      setStatus("success");
      setForm(EMPTY_FORM);
    } catch {
      setStatus("error");
    }
  };

  return (
    <section id="contact" className="section contact">
      <h2>Contact Us</h2>

      <div className="contact-grid">
        <form className="contact-form" onSubmit={handleSubmit}>
          <input
            name="name"
            placeholder="Your Name"
            value={form.name}
            onChange={handleChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Your Email"
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
          <input
            name="subject"
            placeholder="Subject"
            value={form.subject}
            onChange={handleChange}
          />
          <textarea
            name="message"
            placeholder="Your Message"
            rows={5}
            value={form.message}
            onChange={handleChange}
            required
          />
          <button type="submit" className="btn btn-primary" disabled={status === "sending"}>
            {status === "sending" ? "Sending..." : "Send Message"}
          </button>

          {status === "success" && (
            <p className="form-success">Thanks! Your message has been sent.</p>
          )}
          {status === "error" && (
            <p className="form-error">Something went wrong. Please try again or call us directly.</p>
          )}
        </form>

        {company && (
          <div className="contact-info">
            <p><strong>Address:</strong> {company.address}</p>
            <p><strong>Phone:</strong> {company.phone_primary}{company.phone_secondary ? `, ${company.phone_secondary}` : ""}</p>
            <p><strong>Email:</strong> {company.email}</p>
            {company.map_embed_url && (
              <iframe
                title="Location map"
                src={company.map_embed_url}
                width="100%"
                height="250"
                style={{ border: 0 }}
                loading="lazy"
              />
            )}
          </div>
        )}
      </div>
    </section>
  );
}
