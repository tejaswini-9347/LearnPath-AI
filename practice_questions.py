# LearnPath AI - Practice Questions


PRACTICE_QUESTIONS = {

    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": "def"
        },
        {
            "question": "Which data type is used to store True or False?",
            "options": ["String", "Integer", "Boolean", "Float"],
            "answer": "Boolean"
        }
    ],

    "NumPy": [
        {
            "question": "What is NumPy mainly used for?",
            "options": [
                "Web development",
                "Numerical computing",
                "Database management",
                "Game development"
            ],
            "answer": "Numerical computing"
        }
    ],

    "Pandas": [
        {
            "question": "Which Pandas structure is two-dimensional?",
            "options": [
                "Series",
                "DataFrame",
                "Array",
                "Tuple"
            ],
            "answer": "DataFrame"
        }
    ],

    "Machine Learning": [
        {
            "question": "Which type of learning uses labeled data?",
            "options": [
                "Unsupervised Learning",
                "Supervised Learning",
                "Reinforcement Learning",
                "Random Learning"
            ],
            "answer": "Supervised Learning"
        },
        {
            "question": "Which algorithm can be used for classification?",
            "options": [
                "Decision Tree",
                "Linear Search",
                "Binary Search",
                "Bubble Sort"
            ],
            "answer": "Decision Tree"
        }
    ],

    "Deep Learning": [
        {
            "question": "Which structure is the basic building block of a neural network?",
            "options": [
                "Neuron",
                "Database",
                "Compiler",
                "Router"
            ],
            "answer": "Neuron"
        }
    ],

    "Generative AI": [
        {
            "question": "What does Generative AI primarily do?",
            "options": [
                "Only stores data",
                "Generates new content",
                "Only sorts data",
                "Only analyzes networks"
            ],
            "answer": "Generates new content"
        },
        {
            "question": "Which architecture is widely used in modern Generative AI?",
            "options": [
                "Transformer",
                "Bubble Sort",
                "Linked List",
                "Binary Search"
            ],
            "answer": "Transformer"
        }
    ],

    "Web Development": [
        {
            "question": "Which language is used to structure web pages?",
            "options": [
                "HTML",
                "Python",
                "SQL",
                "C"
            ],
            "answer": "HTML"
        }
    ],

    "React": [
        {
            "question": "React is mainly used for building what?",
            "options": [
                "User interfaces",
                "Operating systems",
                "Databases",
                "Computer networks"
            ],
            "answer": "User interfaces"
        }
    ],

    "Data Science": [
        {
            "question": "Which language is widely used in Data Science?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "Assembly"
            ],
            "answer": "Python"
        }
    ]
}


def get_questions(topic):
    """Return practice questions for a topic."""

    return PRACTICE_QUESTIONS.get(topic, [])