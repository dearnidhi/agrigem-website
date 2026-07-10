import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

const client = axios.create({ baseURL });

export const getCompany = () => client.get("/company").then((res) => res.data);
export const getBanners = () => client.get("/banners").then((res) => res.data);
export const getServices = () => client.get("/services").then((res) => res.data);
export const getPartners = () => client.get("/partners").then((res) => res.data);
export const getTestimonials = () => client.get("/testimonials").then((res) => res.data);
export const getJobs = () => client.get("/jobs").then((res) => res.data);
export const sendContact = (payload) => client.post("/contact", payload).then((res) => res.data);
export const submitApplication = (formData) =>
  client
    .post("/careers/apply", formData, { headers: { "Content-Type": "multipart/form-data" } })
    .then((res) => res.data);

export default client;
