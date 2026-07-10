import { useOutletContext } from "react-router-dom";
import About from "../components/About.jsx";

export default function AboutPage() {
  const { company } = useOutletContext();
  return <About company={company} />;
}
