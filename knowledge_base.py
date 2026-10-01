# LearnPath AI - Knowledge Base


TOPICS = {

    "Programming Basics": {
        "prerequisites": []
    },

    "Problem Solving": {
        "prerequisites": [
            "Programming Basics"
        ]
    },

    "Python": {
        "prerequisites": [
            "Programming Basics",
            "Problem Solving"
        ]
    },

    "Statistics": {
        "prerequisites": [
            "Mathematics"
        ]
    },

    "Mathematics": {
        "prerequisites": []
    },

    "NumPy": {
        "prerequisites": [
            "Python"
        ]
    },

    "Pandas": {
        "prerequisites": [
            "Python",
            "NumPy"
        ]
    },

    "Machine Learning": {
        "prerequisites": [
            "Python",
            "NumPy",
            "Pandas",
            "Statistics"
        ]
    },

    "Neural Networks": {
        "prerequisites": [
            "Machine Learning"
        ]
    },

    "Deep Learning": {
        "prerequisites": [
            "Python",
            "Statistics",
            "Machine Learning",
            "Neural Networks"
        ]
    },

    "Transformers": {
        "prerequisites": [
            "Deep Learning"
        ]
    },

    "Generative AI": {
        "prerequisites": [
            "Python",
            "Deep Learning",
            "Transformers"
        ]
    },

    "HTML": {
        "prerequisites": []
    },

    "CSS": {
        "prerequisites": [
            "HTML"
        ]
    },

    "JavaScript": {
        "prerequisites": [
            "HTML",
            "CSS"
        ]
    },

    "Web Development": {
        "prerequisites": [
            "HTML",
            "CSS",
            "JavaScript"
        ]
    },

    "React": {
        "prerequisites": [
            "HTML",
            "CSS",
            "JavaScript"
        ]
    },

    "Data Science": {
        "prerequisites": [
            "Python",
            "Statistics",
            "NumPy",
            "Pandas"
        ]
    }
}
# Difficulty and estimated learning time

TOPIC_INFO = {

    "Programming Basics": {
        "level": "Beginner",
        "hours": 4
    },

    "Problem Solving": {
        "level": "Beginner",
        "hours": 5
    },

    "Python": {
        "level": "Beginner",
        "hours": 10
    },

    "Mathematics": {
        "level": "Beginner",
        "hours": 8
    },

    "Statistics": {
        "level": "Intermediate",
        "hours": 8
    },

    "NumPy": {
        "level": "Beginner",
        "hours": 5
    },

    "Pandas": {
        "level": "Beginner",
        "hours": 6
    },

    "Machine Learning": {
        "level": "Intermediate",
        "hours": 15
    },

    "Neural Networks": {
        "level": "Intermediate",
        "hours": 10
    },

    "Deep Learning": {
        "level": "Advanced",
        "hours": 15
    },

    "Transformers": {
        "level": "Advanced",
        "hours": 12
    },

    "Generative AI": {
        "level": "Advanced",
        "hours": 15
    },

    "HTML": {
        "level": "Beginner",
        "hours": 4
    },

    "CSS": {
        "level": "Beginner",
        "hours": 5
    },

    "JavaScript": {
        "level": "Intermediate",
        "hours": 10
    },

    "Web Development": {
        "level": "Intermediate",
        "hours": 15
    },

    "React": {
        "level": "Intermediate",
        "hours": 12
    },

    "Data Science": {
        "level": "Intermediate",
        "hours": 15
    }
}