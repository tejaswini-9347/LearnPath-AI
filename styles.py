import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
        );

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {

            background:
                radial-gradient(
                    circle at 15% 20%,
                    rgba(37,99,235,0.18),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 85% 10%,
                    rgba(124,58,237,0.18),
                    transparent 30%
                ),
                #050816;

            color: white;
        }

        header {
            visibility: hidden;
        }

        .block-container {

            padding-top: 1rem;
            padding-bottom: 3rem;
            max-width: 1200px;

        }

        .stButton > button {

            border-radius: 12px;

            border: 1px solid
                rgba(255,255,255,0.12);

            background:
                linear-gradient(
                    135deg,
                    #2563eb,
                    #7c3aed
                );

            color: white;

            font-weight: 700;

            padding: 0.7rem 1.5rem;

            transition: all 0.25s ease;

        }

        .stButton > button:hover {

            transform: translateY(-3px);

            box-shadow:
                0 15px 35px
                rgba(37,99,235,0.35);

        }

        .hero {

            position: relative;

            padding:
                70px
                40px
                80px
                40px;

            text-align: center;

            border-radius: 30px;

            overflow: hidden;

            background:
                linear-gradient(
                    135deg,
                    rgba(15,23,42,0.96),
                    rgba(30,41,59,0.82)
                );

            border:
                1px solid
                rgba(255,255,255,0.10);

            box-shadow:
                0 30px 80px
                rgba(0,0,0,0.45);

        }

        .logo {

            font-size: 1.2rem;

            font-weight: 800;

            letter-spacing: 1px;

            margin-bottom: 25px;

        }

        .badge {

            display: inline-block;

            padding: 8px 16px;

            border-radius: 50px;

            background:
                rgba(59,130,246,0.10);

            border:
                1px solid
                rgba(96,165,250,0.30);

            color: #93c5fd;

            font-size: 0.85rem;

            font-weight: 600;

            margin-bottom: 22px;

        }

        .hero h1 {

            font-size:
                clamp(2.8rem, 7vw, 5.5rem);

            line-height: 1.02;

            margin: 0;

            font-weight: 800;

            letter-spacing: -4px;

        }

        .gradient-text {

            background:
                linear-gradient(
                    90deg,
                    #60a5fa,
                    #a78bfa,
                    #c084fc
                );

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;

        }

        .hero-description {

            max-width: 700px;

            margin:
                25px auto
                35px;

            color: #94a3b8;

            font-size: 1.15rem;

            line-height: 1.8;

        }

        .feature-card {

            padding: 28px;

            min-height: 190px;

            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.07),
                    rgba(255,255,255,0.025)
                );

            border:
                1px solid
                rgba(255,255,255,0.09);

            backdrop-filter: blur(18px);

        }

        .feature-icon {

            font-size: 2rem;

            margin-bottom: 12px;

        }

        .feature-card h3 {

            margin: 0 0 10px;

            font-size: 1.15rem;

        }

        .feature-card p {

            color: #94a3b8;

            line-height: 1.6;

            font-size: 0.9rem;

        }

        .section-title {

            text-align: center;

            margin:
                75px 0 35px;

        }

        .section-title h2 {

            font-size: 2.3rem;

            margin-bottom: 10px;

        }

        .section-title p {

            color: #94a3b8;

        }

        .step-card {

            text-align: center;

            padding: 30px 20px;

        }

        .step-number {

            width: 52px;
            height: 52px;

            margin:
                0 auto 18px;

            border-radius: 50%;

            display: flex;

            align-items: center;

            justify-content: center;

            background:
                linear-gradient(
                    135deg,
                    #2563eb,
                    #7c3aed
                );

            font-weight: 800;

        }

        .step-card p {

            color: #94a3b8;

            line-height: 1.6;

        }

        .stat-box {

            text-align: center;

            padding: 25px;

            border-radius: 18px;

            background:
                rgba(255,255,255,0.04);

            border:
                1px solid
                rgba(255,255,255,0.08);

        }

        .stat-number {

            font-size: 2rem;

            font-weight: 800;

            background:
                linear-gradient(
                    90deg,
                    #60a5fa,
                    #a78bfa
                );

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;

        }

        .stat-label {

            color: #94a3b8;

            font-size: 0.85rem;

        }

        .dashboard-header {

            padding: 30px;

            border-radius: 20px;

            background:
                linear-gradient(
                    135deg,
                    rgba(37,99,235,0.14),
                    rgba(124,58,237,0.12)
                );

            border:
                1px solid
                rgba(255,255,255,0.08);

        }

        .info-card {

            padding: 20px;

            border-radius: 16px;

            background:
                rgba(255,255,255,0.04);

            border:
                1px solid
                rgba(255,255,255,0.08);

        }

        .footer {

            text-align: center;

            padding: 50px 20px 20px;

            color: #64748b;

            font-size: 0.85rem;

        }

        </style>
        """,
        unsafe_allow_html=True
    )