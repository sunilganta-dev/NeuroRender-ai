"""
Handles feedback loops for model performance improvement and human-in-the-loop updates.
"""

def collect_user_feedback(prompt: str, output_path: str, rating: int, comment: str = ""):
    feedback = {
        "prompt": prompt,
        "output_path": output_path,
        "rating": rating,
        "comment": comment
    }
    # TODO: Store feedback to a DB or file
    print("Feedback collected:", feedback)
    return feedback