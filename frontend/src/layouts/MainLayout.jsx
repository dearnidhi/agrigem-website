import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar.jsx";
import Footer from "../components/Footer.jsx";

export default function MainLayout({ company }) {
  return (
    <>
      <Navbar company={company} />
      <Outlet context={{ company }} />
      <Footer company={company} />
    </>
  );
}
