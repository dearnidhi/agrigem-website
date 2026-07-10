import { useOutletContext } from "react-router-dom";
import Contact from "../components/Contact.jsx";

export default function ContactPage() {
  const { company } = useOutletContext();
  return <Contact company={company} />;
}
