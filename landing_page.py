import streamlit as st


def show_landing_page():

    # Navbar

    st.markdown(
        """
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding:10px 5px 25px;
        ">

            <div style="
                font-size:1.25rem;
                font-weight:800;
            ">
                🎓 LearnPath
                <span style="color:#60a5fa;">AI</span>
            </div>

            <div style="
                color:#94a3b8;
                font-size:0.9rem;
            ">
                Personalized Learning • Smart Roadmaps
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # Hero

    st.markdown(
        """
        <div class="hero">

            <div class="logo">
                🎓 LEARNPATH AI
            </div>

            <div class="badge">
                ✨ Personalized Learning Assistant
            </div>

            <h1>
                Learn Smarter.<br>

                <span class="gradient-text">
                    Build Your Path.
                </span>

            </h1>

            <p class="hero-description">

                Stop wondering what to learn next.

                LearnPath AI creates a personalized
                learning journey based on your goals,
                current knowledge and available time.

            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    # Get Started

    col1, col2, col3 = st.columns(
        [1.5, 1, 1.5]
    )

    with col2:

        if st.button(
            "🚀 Get Started",
            use_container_width=True
        ):

            st.session_state.page = "setup"

            st.rerun()


    # Features

    st.markdown(
        """
        <div class="section-title">

            <h2>
                Everything you need to learn
                with direction
            </h2>

            <p>
                From your first topic to a complete
                learning journey.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    feature_cols = st.columns(4)


    features = [

        (
            "🧠",
            "Personalized Learning",
            "Build a learning path based on what you already know."
        ),

        (
            "🗺️",
            "Smart Roadmaps",
            "Understand prerequisites and learn topics in the right order."
        ),

        (
            "📅",
            "Study Planning",
            "Turn your roadmap into a practical daily schedule."
        ),

        (
            "📝",
            "Practice & Quiz",
            "Test your understanding with topic-based questions."
        )

    ]


    for col, feature in zip(
        feature_cols,
        features
    ):

        with col:

            st.markdown(
                f"""
                <div class="feature-card">

                    <div class="feature-icon">
                        {feature[0]}
                    </div>

                    <h3>
                        {feature[1]}
                    </h3>

                    <p>
                        {feature[2]}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    # How it works

    st.markdown(
        """
        <div class="section-title">

            <h2>
                How LearnPath AI works
            </h2>

            <p>
                Three simple steps to start your journey.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    step_cols = st.columns(3)


    steps = [

        (
            "01",
            "Choose Your Goal",
            "Select the technical skill you want to master."
        ),

        (
            "02",
            "Tell Us What You Know",
            "Select topics you already understand."
        ),

        (
            "03",
            "Follow Your Path",
            "Get your roadmap, schedule and practice questions."
        )

    ]


    for col, step in zip(
        step_cols,
        steps
    ):

        with col:

            st.markdown(
                f"""
                <div class="step-card">

                    <div class="step-number">
                        {step[0]}
                    </div>

                    <h3>
                        {step[1]}
                    </h3>

                    <p>
                        {step[2]}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    # Stats

    st.markdown(
        """
        <div class="section-title">

            <h2>
                Built for modern learners
            </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    stat_cols = st.columns(4)


    stats = [

        ("17+", "Learning Topics"),
        ("5+", "Core Modules"),
        ("100%", "Personalized"),
        ("24/7", "Available")

    ]


    for col, stat in zip(
        stat_cols,
        stats
    ):

        with col:

            st.markdown(
                f"""
                <div class="stat-box">

                    <div class="stat-number">
                        {stat[0]}
                    </div>

                    <div class="stat-label">
                        {stat[1]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # CTA

    st.markdown(
        """
        <div class="section-title">

            <h2>
                Ready to build your learning path?
            </h2>

            <p>
                Your next skill starts with one click.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(
        [1.5, 1, 1.5]
    )


    with col2:

        if st.button(
            "✨ Start Learning",
            use_container_width=True,
            key="bottom_start"
        ):

            st.session_state.page = "setup"

            st.rerun()


    # Footer

    st.markdown(
        """
        <div class="footer">

            🎓 <b>LearnPath AI</b>

            <br><br>

            Intelligent Learning Prerequisite &
            Roadmap Generator

            <br><br>

            Built with Python & Streamlit

            <br><br>

            © 2026 LearnPath AI

        </div>
        """,
        unsafe_allow_html=True
    )