from sqlalchemy.orm import Session

from . import models


def seed_if_empty(db: Session) -> None:
    if not db.query(models.CompanyInfo).first():
        db.add(
            models.CompanyInfo(
                name="AgriGem",
                tagline="A modern day solution to all your agri-needs!",
                about=(
                    "AgriGem is an integrated agricultural solutions company committed to empowering "
                    "farmers, dealers, and agri-businesses with high-quality inputs, modern technology, "
                    "and expert guidance to achieve sustainable growth.\n\n"
                    "With a strong commitment to quality, innovation, and customer success, AgriGem delivers "
                    "comprehensive agricultural solutions that empower stakeholders across the value chain. "
                    "Our focus is on fostering growth, improving productivity, and building lasting partnerships "
                    "that drive the future of agriculture.\n\n"
                    "At AgriGem, we believe agriculture thrives when quality inputs, innovation, and knowledge "
                    "come together. Our mission is to bridge the gap between traditional farming and modern "
                    "agricultural practices, creating lasting value for farmers and the entire agricultural ecosystem."
                ),
                vision=(
                    "To be India's most trusted agricultural solutions partner, empowering farmers and "
                    "agri-businesses through quality products, innovative technology, and expert support."
                ),
                mission=(
                    "To deliver high-quality agricultural inputs, innovative technologies, and expert agronomic "
                    "support that enhance farm productivity, strengthen dealer partnerships, and drive sustainable "
                    "growth across the agricultural ecosystem."
                ),
                address="Orchid Tower, Maharana Pratap Nagar, Lashkar, Gwalior, MP, India. 474009",
                phone_primary="+91 89627 38381",
                phone_secondary="+91 89627 38380",
                email="info@agrigem.in",
                map_embed_url="https://maps.google.com/maps?q=Orchid+Tower+Maharana+Pratap+Nagar+Lashkar+Gwalior+MP+474009&output=embed",
                cin="U46692MP2025PTC077628",
                linkedin_url="https://www.linkedin.com/company/agrigem-india/",
                instagram_url="https://www.instagram.com/agrigem.in?igsh=MWUxbmloNHlwM2xzaA%3D%3D&utm_source=qr",
                whatsapp_url="https://whatsapp.com/channel/0029VbC8UplKbYMSMxgRgc0w",
            )
        )

    if not db.query(models.Banner).first():
        db.add_all(
            [
                models.Banner(
                    title="Modern Solutions for Every Agricultural Need",
                    subtitle="High-quality seeds, crop protection solutions, fertilizers, and expert farming advice.",
                    image_url="/images/banners/farm-sunrise.svg",
                    display_order=1,
                ),
                models.Banner(
                    title="As Agriculture Evolves, So Do We",
                    subtitle="Modern agricultural solutions backed by trusted brands.",
                    image_url="/images/banners/farm-daytime.svg",
                    display_order=2,
                ),
                models.Banner(
                    title="A New-Generation Agricultural Enterprise",
                    subtitle="Proudly based in central India, delivering trusted agricultural solutions to farmers pan India.",
                    image_url="/images/banners/farm-harvest.svg",
                    display_order=3,
                ),
            ]
        )

    if not db.query(models.Service).first():
        db.add_all(
            [
                models.Service(
                    name="Seeds",
                    description="Sourced from leading organizations with assured originality and germination quality.",
                    icon="seed",
                    display_order=1,
                ),
                models.Service(
                    name="Pesticides",
                    description="Quality-assured pesticides from major manufacturers to protect every crop cycle.",
                    icon="spray",
                    display_order=2,
                ),
                models.Service(
                    name="Fertilizers",
                    description="Quality-focused fertilizers chosen to maximize yield and soil health.",
                    icon="fertilizer",
                    display_order=3,
                ),
                models.Service(
                    name="Agronomy Support",
                    description="Trusted agronomy expertise to maximize crop performance.",
                    icon="services",
                    display_order=4,
                ),
            ]
        )

    if not db.query(models.Partner).first():
        db.add_all(
            [
                models.Partner(name="ADAMA", logo_url="/images/brands/adama.jpeg", display_order=1),
                models.Partner(name="BASF", logo_url="/images/brands/BASF.png", display_order=2),
                models.Partner(name="Bayer CropScience", logo_url="/images/brands/Bayer.png", display_order=3),
                models.Partner(name="Bharat Certis", logo_url="/images/brands/Bharat certis.jpeg", display_order=4),
                models.Partner(name="Bioseed", logo_url="/images/brands/Bioseed.png", display_order=5),
                models.Partner(name="Coromandel", logo_url="/images/brands/Coromandal.jpeg", display_order=6),
                models.Partner(name="Corteva", logo_url="/images/brands/Corteva.png", display_order=7),
                models.Partner(name="Crystal Crop Protection", logo_url="/images/brands/Crystal.png", display_order=8),
                models.Partner(name="DCM Shriram", logo_url="/images/brands/DCM Shriram.png", display_order=9),
                models.Partner(name="Dhanesha", logo_url="/images/brands/Dhanesha.png", display_order=10),
                models.Partner(name="Dhanuka Agritech", logo_url="/images/brands/Dhanuka.png", display_order=11),
                models.Partner(name="FMC", logo_url="/images/brands/fmc.png", display_order=12),
                models.Partner(name="IIL", logo_url="/images/brands/IIL.jpeg", display_order=13),
                models.Partner(name="JU", logo_url="/images/brands/JU.jpeg", display_order=14),
                models.Partner(name="Kamadgiri", logo_url="/images/brands/Kamadgiri.jpeg", display_order=15),
                models.Partner(name="Kaveri Seeds", logo_url="/images/brands/Kaveri.jpeg", display_order=16),
                models.Partner(name="Krishi Rasayan", logo_url="/images/brands/Krishi rasayan.png", display_order=17),
                models.Partner(name="Mahindra Agri", logo_url="/images/brands/Mahindra.jpeg", display_order=18),
                models.Partner(name="NACL Industries", logo_url="/images/brands/NACL.jpeg", display_order=19),
                models.Partner(name="NATCO Agri", logo_url="/images/brands/Natco.jpeg", display_order=20),
                models.Partner(name="Nath Seeds", logo_url="/images/brands/Nath seeds.jpeg", display_order=21),
                models.Partner(name="Nichino", logo_url="/images/brands/NICHINO.jpeg", display_order=22),
                models.Partner(name="Nuziveedu Seeds", logo_url="/images/brands/Nuziveedu.jpeg", display_order=23),
                models.Partner(name="PI Industries", logo_url="/images/brands/PI.png", display_order=24),
                models.Partner(name="Sumil", logo_url="/images/brands/SUmil.jpeg", display_order=25),
                models.Partner(name="Sumitomo Chemical", logo_url="/images/brands/Sumitomo.jpeg", display_order=26),
                models.Partner(name="Syngenta", logo_url="/images/brands/Syngenta.png", display_order=27),
                models.Partner(name="Torpical", logo_url="/images/brands/Torpical.jpeg", display_order=28),
                models.Partner(name="Willowood", logo_url="/images/brands/Willowood.jpeg", display_order=29),
            ]
        )

    if not db.query(models.JobOpening).first():
        db.add(
            models.JobOpening(
                title="Sales Executive",
                location="Multiple Locations",
                job_type="Full-time",
                description=(
                    "ABOUT AGRIGEM\n"
                    "AgriGem is an integrated agricultural solutions company dedicated to empowering farmers "
                    "and agri-businesses through quality products, innovative solutions, and expert support. "
                    "We work closely with dealers, distributors, and farmers to deliver value across the "
                    "agricultural ecosystem.\n\n"
                    "JOB SUMMARY\n"
                    "We are looking for a dynamic and result-oriented Sales Executive to drive business growth, "
                    "strengthen dealer relationships, and expand AgriGem's market presence. The ideal candidate "
                    "should be self-motivated, proactive, and passionate about agriculture, with a strong "
                    "commitment to achieving sales targets and delivering excellent customer service.\n\n"
                    "KEY RESPONSIBILITIES\n"
                    "Develop and maintain strong relationships with dealers, distributors, and farmers.\n"
                    "Promote and sell AgriGem's portfolio of agricultural products and solutions.\n"
                    "Identify new business opportunities and expand market reach.\n"
                    "Conduct regular field visits and market surveys to understand customer needs and competitor activities.\n"
                    "Achieve assigned sales targets and business objectives.\n"
                    "Organize and participate in farmer meetings, demonstrations, and promotional activities.\n"
                    "Provide timely market feedback and sales reports to management.\n"
                    "Ensure effective product positioning and brand visibility in the assigned territory.\n"
                    "Coordinate with internal teams to ensure smooth execution of sales and customer support activities.\n\n"
                    "MUST-HAVE REQUIREMENTS\n"
                    "Self-motivated and self-driven personality.\n"
                    "Strong communication and interpersonal skills.\n"
                    "Willingness to travel extensively within the assigned territory.\n"
                    "Dedicated, hardworking, and goal-oriented.\n"
                    "Ability to work independently and take ownership of assigned responsibilities.\n"
                    "Positive attitude with a strong desire to learn and grow.\n\n"
                    "DESIRED QUALIFICATIONS\n"
                    "B.Sc. Agriculture / M.Sc. Agriculture preferred.\n"
                    "Fluency in English (spoken and written).\n"
                    "Prior experience in the agriculture, seeds, fertilizers, or crop protection industry will be an added advantage.\n\n"
                    "WHAT WE OFFER\n"
                    "Opportunity to work with a fast-growing agricultural solutions company.\n"
                    "Professional growth and learning opportunities.\n"
                    "Performance-driven work environment.\n"
                    "Competitive compensation and incentives."
                ),
                requirements="",
                display_order=1,
            )
        )

    db.commit()
