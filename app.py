import streamlit as st

from roadmap_generator import (
    get_prerequisites,
    generate_roadmap,
    get_topic_info,
    calculate_total_time,
    personalize_roadmap,
    generate_study_schedule
)

from practice_questions import get_questions


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="LearnPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# SESSION STATE
# ==================================================

if "show_landing" not in st.session_state:
    st.session_state.show_landing = True

if "generated" not in st.session_state:
    st.session_state.generated = False


# ==================================================
# LANDING PAGE
# ==================================================

if st.session_state.show_landing:

    # Landing-page navigation state
    if "landing_section" not in st.session_state:
        st.session_state.landing_section = "home"

    # --------------------------------------------------
    # LANDING PAGE STYLE
    # --------------------------------------------------

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }

        .stApp {
            background:
                radial-gradient(circle at 10% 10%, rgba(99,102,241,0.12), transparent 28%),
                radial-gradient(circle at 90% 20%, rgba(168,85,247,0.10), transparent 25%),
                radial-gradient(circle at 50% 100%, rgba(14,165,233,0.08), transparent 30%),
                var(--background-color);
            color: var(--text-color);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }

        .lp-nav {
            padding: 12px 18px;
            border: 1px solid var(--secondary-background-color);
            border-radius: 18px;
            background: color-mix(in srgb, var(--secondary-background-color) 88%, transparent);
            backdrop-filter: blur(14px);
        }

        .lp-brand {
            font-size: 22px;
            font-weight: 800;
            color: var(--text-color);
            padding-top: 5px;
        }

        .lp-brand span {
            color: #a78bfa;
        }

        .lp-label {
            color: var(--text-color);
            font-size: 13px;
            padding-top: 10px;
            text-align: right;
        }

        .lp-hero {
            padding: 60px 0 35px 0;
        }

        .lp-kicker {
            color: #a78bfa;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 14px;
        }

        .lp-title {
            color: var(--text-color);
            font-size: clamp(42px, 6vw, 70px);
            line-height: 1.02;
            font-weight: 900;
            letter-spacing: -3px;
            margin-bottom: 20px;
        }

        .lp-title span {
            background: linear-gradient(90deg, #60a5fa, #a78bfa, #f0abfc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .lp-description {
            color: var(--text-color);
            font-size: 17px;
            line-height: 1.75;
            max-width: 680px;
        }

        .lp-note {
            color: var(--text-color);
            font-size: 13px;
            margin-top: 13px;
        }

        .lp-preview {
            border: 1px solid rgba(127,127,127,0.25);
            border-radius: 25px;
            padding: 24px;
            background: var(--secondary-background-color);
            box-shadow: 0 25px 80px rgba(0,0,0,0.35);
        }

        .lp-preview-title {
            color: var(--text-color);
            font-size: 21px;
            font-weight: 800;
            margin-bottom: 4px;
        }

        .lp-preview-subtitle {
            color: var(--text-color);
            font-size: 13px;
            margin-bottom: 18px;
        }

        .lp-step {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            margin-top: 9px;
            border-radius: 13px;
            background: color-mix(in srgb, var(--background-color) 70%, var(--secondary-background-color));
            border: 1px solid rgba(127,127,127,0.18);
            color: var(--text-color);
            font-size: 14px;
        }

        .lp-number {
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 9px;
            background: rgba(139,92,246,0.18);
            color: #c4b5fd;
            font-weight: 700;
        }

        .lp-section-title {
            text-align: center;
            color: var(--text-color);
            font-size: 30px;
            font-weight: 800;
            margin: 42px 0 7px 0;
        }

        .lp-section-text {
            text-align: center;
            color: var(--text-color);
            margin-bottom: 25px;
        }

        .lp-card {
            min-height: 165px;
            padding: 23px;
            border-radius: 19px;
            border: 1px solid rgba(127,127,127,0.20);
            background: var(--secondary-background-color);
        }

        .lp-card-icon {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .lp-card-title {
            color: var(--text-color);
            font-size: 18px;
            font-weight: 750;
            margin-bottom: 8px;
        }

        .lp-card-text {
            color: var(--text-color);
            font-size: 14px;
            line-height: 1.6;
        }

        .lp-footer {
            text-align: center;
            color: var(--text-color);
            font-size: 13px;
            padding: 30px 0 5px 0;
        }

        /* =========================================
           GLOWING LANDING PAGE BUTTONS
           ========================================= */

        [data-testid="stButton"] button {
            border: 1px solid rgba(167,139,250,0.55) !important;
            border-radius: 12px !important;
            background: linear-gradient(135deg, rgba(79,70,229,0.95), rgba(124,58,237,0.95)) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            box-shadow: 0 0 12px rgba(124,58,237,0.35), 0 0 28px rgba(96,165,250,0.12) !important;
            transition: all 0.2s ease-in-out !important;
        }

        [data-testid="stButton"] button:hover {
            border-color: #c4b5fd !important;
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: #ffffff !important;
            transform: translateY(-2px);
            box-shadow: 0 0 18px rgba(124,58,237,0.65), 0 0 38px rgba(96,165,250,0.25) !important;
        }

        [data-testid="stButton"] button:focus,
        [data-testid="stButton"] button:focus-visible,
        [data-testid="stButton"] button:active {
            border-color: #ddd6fe !important;
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: #ffffff !important;
            box-shadow: 0 0 20px rgba(139,92,246,0.75), 0 0 42px rgba(96,165,250,0.28) !important;
            outline: none !important;
        }

        [data-testid="stButton"] button p {
            color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # TOP NAVIGATION
    # --------------------------------------------------

    st.markdown('<div class="lp-nav">', unsafe_allow_html=True)

    nav_logo, nav_space, nav_features, nav_about, nav_start = st.columns(
        [3.8, 2.8, 1.0, 0.8, 1.3]
    )

    with nav_logo:
        st.markdown(
            '<div class="lp-brand">🎓 Learn<span>Path AI</span></div>',
            unsafe_allow_html=True
        )

    with nav_features:
        if st.button(
            "Features",
            key="landing_features",
            use_container_width=True,
            type="primary" if st.session_state.landing_section == "features" else "secondary"
        ):
            st.session_state.landing_section = "features"
            st.rerun()

    with nav_about:
        if st.button(
            "About",
            key="landing_about",
            use_container_width=True,
            type="primary" if st.session_state.landing_section == "about" else "secondary"
        ):
            st.session_state.landing_section = "about"
            st.rerun()

    with nav_start:
        if st.button("Get Started →", key="landing_start", type="primary", use_container_width=True):
            st.session_state.show_landing = False
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------
    # FEATURES / ABOUT PANEL
    # --------------------------------------------------

    if st.session_state.landing_section == "features":

        st.markdown(
            '<div class="lp-section-title">✨ Features</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="lp-section-text">Everything available in your current LearnPath AI application.</div>',
            unsafe_allow_html=True
        )

        f1, f2, f3 = st.columns(3)
        feature_cards = [
            (f1, "🧠", "Personalized Learning", "Uses the topics you already know to remove them from your remaining learning path."),
            (f2, "🗺️", "Prerequisite Roadmap", "Finds prerequisite topics and places them in a logical learning order."),
            (f3, "📅", "Study Schedule", "Converts the learning path into a day-by-day schedule using your available hours."),
            (f1, "⏱️", "Learning Time", "Estimates the total learning hours for the remaining topics."),
            (f2, "📝", "Practice Quiz", "Provides topic-based practice questions so you can check your understanding."),
            (f3, "📊", "Learning Overview", "Shows your target topic, difficulty, remaining hours and topics to learn.")
        ]

        for col, icon, title, description in feature_cards:
            with col:
                st.markdown(
                    f'<div class="lp-card" style="margin-top:14px;">'
                    f'<div class="lp-card-icon">{icon}</div>'
                    f'<div class="lp-card-title">{title}</div>'
                    f'<div class="lp-card-text">{description}</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        st.divider()

    elif st.session_state.landing_section == "about":

        st.markdown(
            '<div class="lp-section-title">ℹ️ About LearnPath AI</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="lp-section-text">A student-focused learning roadmap and prerequisite planner.</div>',
            unsafe_allow_html=True
        )

        a1, a2 = st.columns(2, gap="large")

        with a1:
            st.markdown(
                '<div class="lp-card">'
                '<div class="lp-card-icon">🎯</div>'
                '<div class="lp-card-title">Project Goal</div>'
                '<div class="lp-card-text">'
                'LearnPath AI helps students understand what to learn first, '
                'what comes next and how much time they may need. '
                'It creates a structured learning path from a predefined knowledge base.'
                '</div></div>',
                unsafe_allow_html=True
            )

        with a2:
            st.markdown(
                '<div class="lp-card">'
                '<div class="lp-card-icon">🛠️</div>'
                '<div class="lp-card-title">How This Project Works</div>'
                '<div class="lp-card-text">'
                'The current application is a Python and Streamlit knowledge-based system. '
                'It uses predefined topic relationships, prerequisite logic, personalization, '
                'time estimation, scheduling and practice questions. '
                '<strong>It does not use a generative AI model or an external AI API.</strong>'
                '</div></div>',
                unsafe_allow_html=True
            )

        st.divider()

    # --------------------------------------------------
    # HERO
    # --------------------------------------------------

    hero_left, hero_right = st.columns([1.15, 0.85], gap="large")

    with hero_left:
        st.markdown(
            '<div class="lp-hero">'
            '<div class="lp-kicker">🎯 Personalized learning, simplified</div>'
            '<div class="lp-title">Learn smarter.<br><span>Build your path.</span></div>'
            '<div class="lp-description">'
            'Choose a learning goal, tell us what you already know, and get a structured '
            'learning path with prerequisites, estimated time, study schedule and practice questions.'
            '</div>'
            '<div class="lp-note">⚡ No external AI API required • Built with Python & Streamlit</div>'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "🚀 Start Learning",
            key="hero_start",
            type="primary"
        ):
            st.session_state.show_landing = False
            st.rerun()

    with hero_right:
        st.markdown(
            '<div class="lp-preview">'
            '<div style="color:#94a3b8;font-size:12px;margin-bottom:12px;">YOUR LEARNING PATH</div>'
            '<div class="lp-preview-title">Machine Learning</div>'
            '<div class="lp-preview-subtitle">Example roadmap</div>'
            '<div class="lp-step"><div class="lp-number">01</div><span>🐍 Python</span></div>'
            '<div class="lp-step"><div class="lp-number">02</div><span>🔢 NumPy</span></div>'
            '<div class="lp-step"><div class="lp-number">03</div><span>📊 Pandas</span></div>'
            '<div class="lp-step"><div class="lp-number">04</div><span>🤖 Machine Learning</span></div>'
            '</div>',
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # THREE FEATURE HIGHLIGHTS
    # --------------------------------------------------

    st.markdown(
        '<div class="lp-section-title">Everything you need to learn with direction</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="lp-section-text">A simple workflow that turns a learning goal into an actionable plan.</div>',
        unsafe_allow_html=True
    )

    h1, h2, h3 = st.columns(3)

    highlights = [
        (h1, "🧠", "Know where to start", "Identify the prerequisite concepts needed before your target topic."),
        (h2, "🗺️", "See the full path", "Follow the topics in a structured order instead of learning randomly."),
        (h3, "📅", "Plan your time", "Turn the roadmap into a practical daily schedule and practice along the way.")
    ]

    for col, icon, title, description in highlights:
        with col:
            st.markdown(
                f'<div class="lp-card">'
                f'<div class="lp-card-icon">{icon}</div>'
                f'<div class="lp-card-title">{title}</div>'
                f'<div class="lp-card-text">{description}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    # --------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------

    st.markdown(
        '<div class="lp-section-title">How your journey works</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="lp-section-text">Three simple steps to create your learning path.</div>',
        unsafe_allow_html=True
    )

    j1, j2, j3 = st.columns(3)

    journey = [
        (j1, "01", "Choose your goal", "Select Python, Machine Learning, Generative AI, Web Development or another available topic."),
        (j2, "02", "Tell us what you know", "Select the concepts you already understand so they can be skipped."),
        (j3, "03", "Follow your path", "Explore prerequisites, roadmap, study schedule and quiz."),
    ]

    for col, number, title, description in journey:
        with col:
            st.markdown(
                f'<div class="lp-card">'
                f'<div class="lp-card-icon">{number}</div>'
                f'<div class="lp-card-title">{title}</div>'
                f'<div class="lp-card-text">{description}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    st.divider()
    st.markdown(
        '<div class="lp-footer">🎓 LearnPath AI · Intelligent Learning Prerequisite & Roadmap Generator · Built with Python & Streamlit</div>',
        unsafe_allow_html=True
    )


# ==================================================
# EXISTING APPLICATION
# ==================================================

else:



    # ==================================================
    # SIDEBAR
    # ==================================================

    with st.sidebar:

        st.header("🎓 LearnPath AI")

        st.write(
            "Build a personalized learning roadmap "
            "based on your current knowledge."
        )

        st.divider()

        st.subheader("📌 How It Works")

        st.write("1️⃣ Select a learning topic")
        st.write("2️⃣ Select topics you already know")
        st.write("3️⃣ Choose your daily study time")
        st.write("4️⃣ Generate your learning roadmap")
        st.write("5️⃣ Explore each section")
        st.write("6️⃣ Test yourself with the quiz")

        st.divider()

        st.info(
            "LearnPath AI uses a Python knowledge base "
            "to identify prerequisites and create "
            "a personalized learning path."
        )


    # ==================================================
    # PAGE 1 — SETUP PAGE
    # ==================================================

    if not st.session_state.generated:

        # --------------------------------------------------
        # HEADER
        # --------------------------------------------------

        st.title("🎓 LearnPath AI")

        st.subheader(
            "Intelligent Learning Prerequisite & Roadmap Generator"
        )

        st.divider()


        # --------------------------------------------------
        # LEARNING GOAL
        # --------------------------------------------------

        st.header("🎯 Choose Your Learning Goal")

        col1, col2 = st.columns(2)


        # Target topic
        with col1:

            topic = st.selectbox(
                "What do you want to learn?",
                [
                    "Python",
                    "NumPy",
                    "Pandas",
                    "Machine Learning",
                    "Deep Learning",
                    "Generative AI",
                    "Web Development",
                    "React",
                    "Data Science"
                ]
            )


        # Daily study time
        with col2:

            hours_per_day = st.slider(
                "⏰ How many hours can you study per day?",
                min_value=1,
                max_value=8,
                value=2
            )

            st.write(
                f"📚 You can study "
                f"**{hours_per_day} hour(s)** per day."
            )


        # --------------------------------------------------
        # EXISTING KNOWLEDGE
        # --------------------------------------------------

        st.header("🧠 Your Existing Knowledge")

        all_topics = [
            "Programming Basics",
            "Problem Solving",
            "Python",
            "Mathematics",
            "Statistics",
            "NumPy",
            "Pandas",
            "Machine Learning",
            "Neural Networks",
            "Deep Learning",
            "Transformers",
            "HTML",
            "CSS",
            "JavaScript"
        ]

        known_topics = st.multiselect(
            "Select the topics you already know:",
            all_topics,
            placeholder="Choose topics..."
        )


        if known_topics:

            st.success(
                f"✅ You selected "
                f"{len(known_topics)} known topic(s)."
            )

        else:

            st.caption(
                "No previous knowledge selected. "
                "The complete learning path will be shown."
            )


        # --------------------------------------------------
        # GENERATE BUTTON
        # --------------------------------------------------

        st.write("")

        if st.button(
            "🚀 Generate My Learning Path",
            use_container_width=True
        ):

            # Generate roadmap
            prerequisites = get_prerequisites(topic)

            roadmap = generate_roadmap(topic)

            personalized_roadmap = personalize_roadmap(
                roadmap,
                known_topics
            )

            study_schedule = generate_study_schedule(
                personalized_roadmap,
                hours_per_day
            )

            total_hours = calculate_total_time(
                personalized_roadmap
            )

            topic_info = get_topic_info(topic)


            # --------------------------------------------------
            # STORE EVERYTHING
            # --------------------------------------------------

            st.session_state.generated = True

            st.session_state.prerequisites = prerequisites

            st.session_state.roadmap = roadmap

            st.session_state.personalized_roadmap = (
                personalized_roadmap
            )

            st.session_state.study_schedule = (
                study_schedule
            )

            st.session_state.total_hours = total_hours

            st.session_state.topic_info = topic_info

            st.session_state.generated_topic = topic

            st.session_state.known_topics = known_topics

            st.session_state.hours_per_day = hours_per_day


            # --------------------------------------------------
            # MOVE TO NEXT PAGE
            # --------------------------------------------------

            st.rerun()


    # ==================================================
    # PAGE 2 — LEARNING DASHBOARD
    # ==================================================

    else:

        # --------------------------------------------------
        # RETRIEVE STORED DATA
        # --------------------------------------------------

        prerequisites = st.session_state.prerequisites

        personalized_roadmap = (
            st.session_state.personalized_roadmap
        )

        study_schedule = (
            st.session_state.study_schedule
        )

        total_hours = st.session_state.total_hours

        topic_info = st.session_state.topic_info

        generated_topic = st.session_state.generated_topic

        known_topics = st.session_state.known_topics

        hours_per_day = st.session_state.hours_per_day


        # --------------------------------------------------
        # DASHBOARD HEADER
        # --------------------------------------------------

        st.title("🎓 Your Personalized Learning Path")

        st.subheader(
            f"Learning roadmap for {generated_topic}"
        )

        st.divider()


        # --------------------------------------------------
        # BACK TO SETUP
        # --------------------------------------------------

        if st.button("⬅️ Back to Setup"):

            st.session_state.generated = False

            st.rerun()


        st.write("")


        # --------------------------------------------------
        # SUCCESS MESSAGE
        # --------------------------------------------------

        st.success(
            f"🎉 Learning path generated successfully "
            f"for **{generated_topic}**!"
        )


        # ==================================================
        # NAVIGATION TABS
        # ==================================================

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "📊 Overview",
                "📌 Prerequisites",
                "🪜 Roadmap",
                "📅 Study Schedule",
                "📝 Quiz"
            ]
        )


        # ==================================================
        # TAB 1 — OVERVIEW
        # ==================================================

        with tab1:

            st.header("📊 Learning Overview")

            card1, card2, card3, card4 = st.columns(4)


            with card1:

                st.metric(
                    "🎯 Target Topic",
                    generated_topic
                )


            with card2:

                st.metric(
                    "📚 Difficulty",
                    topic_info["level"]
                )


            with card3:

                st.metric(
                    "⏱️ Remaining Hours",
                    f"{total_hours} hrs"
                )


            with card4:

                st.metric(
                    "📖 Topics to Learn",
                    len(personalized_roadmap)
                )


            st.divider()

            st.subheader("📈 Learning Summary")


            if total_hours > 0:

                estimated_days = (
                    (total_hours + hours_per_day - 1)
                    // hours_per_day
                )

            else:

                estimated_days = 0


            summary_col1, summary_col2 = st.columns(2)


            with summary_col1:

                st.info(
                    f"📚 **Total Learning Time**\n\n"
                    f"**{total_hours} hours**"
                )


            with summary_col2:

                st.info(
                    f"📅 **Estimated Completion Time**\n\n"
                    f"**{estimated_days} day(s)**"
                )


            st.subheader("🧠 Your Current Knowledge")


            if known_topics:

                for item in known_topics:

                    st.write(
                        f"✅ {item}"
                    )

            else:

                st.write(
                    "No previous topics selected."
                )


        # ==================================================
        # TAB 2 — PREREQUISITES
        # ==================================================

        with tab2:

            st.header("📌 Direct Prerequisites")

            st.write(
                f"Prerequisites required before learning "
                f"**{generated_topic}**:"
            )


            if prerequisites:

                prereq_col1, prereq_col2 = st.columns(2)


                for index, item in enumerate(
                    prerequisites
                ):

                    if index % 2 == 0:

                        with prereq_col1:

                            st.success(
                                f"✅ {item}"
                            )

                    else:

                        with prereq_col2:

                            st.success(
                                f"✅ {item}"
                            )

            else:

                st.info(
                    "🎉 No prerequisites are required "
                    "for this topic."
                )


            st.divider()

            st.subheader(
                "💡 Why Are Prerequisites Important?"
            )

            st.write(
                "Prerequisites are concepts that help "
                "you understand the target topic more easily. "
                "LearnPath AI identifies these concepts "
                "and places them in the recommended learning path."
            )


        # ==================================================
        # TAB 3 — ROADMAP
        # ==================================================

        with tab3:

            st.header(
                "🪜 Personalized Learning Roadmap"
            )

            st.write(
                "Follow these topics in the recommended order."
            )


            if personalized_roadmap:

                for index, item in enumerate(
                    personalized_roadmap,
                    start=1
                ):

                    info = get_topic_info(item)


                    with st.container(border=True):

                        st.subheader(
                            f"{index}. {item}"
                        )

                        col_a, col_b = st.columns(2)


                        with col_a:

                            st.write(
                                f"📚 **Difficulty:** "
                                f"{info['level']}"
                            )


                        with col_b:

                            st.write(
                                f"⏱️ **Estimated Time:** "
                                f"{info['hours']} hours"
                            )

            else:

                st.success(
                    "🎉 You already know all the topics "
                    "required for this learning goal!"
                )


        # ==================================================
        # TAB 4 — STUDY SCHEDULE
        # ==================================================

        with tab4:

            st.header(
                "📅 Personalized Study Schedule"
            )

            st.write(
                f"Your schedule is based on "
                f"**{hours_per_day} hour(s) per day**."
            )


            if study_schedule:

                current_day = None


                for session in study_schedule:

                    day = session["day"]


                    if day != current_day:

                        st.divider()

                        st.subheader(
                            f"📅 Day {day}"
                        )

                        current_day = day


                    with st.container(border=True):

                        st.write(
                            f"📖 **{session['topic']}**"
                        )

                        st.write(
                            f"⏱️ Study Time: "
                            f"**{session['hours']} hour(s)**"
                        )

            else:

                st.success(
                    "🎉 No additional study schedule "
                    "is required."
                )


        # ==================================================
        # TAB 5 — QUIZ
        # ==================================================

        with tab5:

            st.header("📝 Practice Quiz")

            st.write(
                f"Test your understanding of "
                f"**{generated_topic}**."
            )


            questions = get_questions(
                generated_topic
            )


            if questions:

                with st.form(
                    key=f"quiz_form_{generated_topic}"
                ):

                    answers = []


                    for index, question in enumerate(
                        questions,
                        start=1
                    ):

                        st.subheader(
                            f"Question {index}"
                        )

                        st.write(
                            question["question"]
                        )


                        answer = st.radio(
                            "Choose your answer:",
                            question["options"],
                            key=(
                                f"quiz_"
                                f"{generated_topic}_"
                                f"{index}"
                            )
                        )


                        answers.append(answer)

                        st.write("")


                    check_answers = (
                        st.form_submit_button(
                            "📊 Check My Answers",
                            use_container_width=True
                        )
                    )


                if check_answers:

                    score = 0


                    for index, question in enumerate(
                        questions
                    ):

                        if (
                            answers[index]
                            == question["answer"]
                        ):

                            score += 1


                    percentage = (
                        score / len(questions)
                    ) * 100


                    st.divider()

                    st.subheader(
                        "📊 Quiz Result"
                    )


                    result_col1, result_col2 = (
                        st.columns(2)
                    )


                    with result_col1:

                        st.metric(
                            "Your Score",
                            f"{score}/{len(questions)}"
                        )


                    with result_col2:

                        st.metric(
                            "Percentage",
                            f"{percentage:.0f}%"
                        )


                    if score == len(questions):

                        st.balloons()

                        st.success(
                            "🏆 Excellent! "
                            "You answered all questions correctly!"
                        )


                    elif score >= len(questions) / 2:

                        st.info(
                            "👍 Good job! Review the questions "
                            "you missed and keep practicing."
                        )


                    else:

                        st.warning(
                            "📖 Keep practicing! Review the "
                            "learning roadmap and try again."
                        )


            else:

                st.info(
                    "Practice questions are not available "
                    "for this topic yet."
                )


        # ==================================================
        # FOOTER
        # ==================================================

        st.divider()

        st.markdown(
            "### 🎓 LearnPath AI"
        )

        st.caption(
            "Intelligent Learning Prerequisite & Roadmap Generator"
        )

        st.caption(
            "Python • Streamlit • Knowledge-Based Recommendation"
        )
