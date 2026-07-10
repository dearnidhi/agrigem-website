import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import { getCompany } from "./api";

import MainLayout from "./layouts/MainLayout.jsx";
import Home from "./pages/Home.jsx";
import AboutPage from "./pages/AboutPage.jsx";
import ServicesPage from "./pages/ServicesPage.jsx";
import CareerPage from "./pages/CareerPage.jsx";
import ContactPage from "./pages/ContactPage.jsx";

export default function App() {
  const [company, setCompany] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    getCompany()
      .then(setCompany)
      .catch(() => setError(true));
  }, []);

  if (error) {
    return (
      <div className="api-error">
        Backend se connect nahi ho paaya. Pehle FastAPI server start karo (uvicorn app.main:app --reload)
        aur phir page refresh karo.
      </div>
    );
  }

  return (
    <Routes>
      <Route element={<MainLayout company={company} />}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/services" element={<ServicesPage />} />
        <Route path="/careers" element={<CareerPage />} />
        <Route path="/contact" element={<ContactPage />} />
      </Route>
    </Routes>
  );
}
