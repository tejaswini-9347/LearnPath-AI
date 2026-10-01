from knowledge_base import TOPICS, TOPIC_INFO

def get_prerequisites(topic):
    """Return direct prerequisites for a topic."""

    if topic not in TOPICS:
        return []

    return TOPICS[topic]["prerequisites"]


def build_learning_path(topic, visited=None):
    """Recursively find all prerequisites."""

    if visited is None:
        visited = set()

    learning_path = []

    if topic not in TOPICS:
        return learning_path

    if topic in visited:
        return learning_path

    visited.add(topic)

    for prerequisite in TOPICS[topic]["prerequisites"]:

        prerequisite_path = build_learning_path(
            prerequisite,
            visited
        )

        learning_path.extend(prerequisite_path)

    learning_path.append(topic)

    return learning_path


def generate_roadmap(topic):
    """Generate the complete learning roadmap."""

    return build_learning_path(topic)


def get_topic_info(topic):
    """Return difficulty and learning time."""

    return TOPIC_INFO.get(
        topic,
        {
            "level": "Unknown",
            "hours": 0
        }
    )


def calculate_total_time(roadmap):
    """Calculate total estimated learning time."""

    total_hours = 0

    for topic in roadmap:
        info = get_topic_info(topic)
        total_hours += info["hours"]

    return total_hours


def personalize_roadmap(roadmap, known_topics):
    """Remove topics that the user already knows."""

    personalized_path = []

    for topic in roadmap:

        if topic not in known_topics:
            personalized_path.append(topic)

    return personalized_path

def generate_study_schedule(roadmap, hours_per_day):
    """Create a day-by-day study schedule."""

    schedule = []
    day = 1

    remaining_day_hours = hours_per_day

    for topic in roadmap:

        topic_hours = get_topic_info(topic)["hours"]
        remaining_topic_hours = topic_hours

        while remaining_topic_hours > 0:

            hours_today = min(
                remaining_topic_hours,
                remaining_day_hours
            )

            schedule.append({
                "day": day,
                "topic": topic,
                "hours": hours_today
            })

            remaining_topic_hours -= hours_today
            remaining_day_hours -= hours_today

            # Start a new day when today's hours are full
            if remaining_day_hours <= 0:

                day += 1
                remaining_day_hours = hours_per_day

    return schedule