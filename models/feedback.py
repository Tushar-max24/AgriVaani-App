"""
Feedback model for storing user feedback in memory.
This is a simple in-memory storage solution for demonstration purposes.
In a production environment, this would be replaced with a database.
"""

# In-memory storage for feedback
feedback_db = []

def add_feedback(feedback: dict):
    """
    Add a new feedback to the in-memory storage.
    
    Args:
        feedback (dict): Dictionary containing feedback details
    """
    feedback_db.append(feedback)
    return {"message": "Feedback submitted successfully!"}

def get_feedback():
    """
    Retrieve all feedback entries.
    
    Returns:
        list: List of all feedback entries
    """
    return feedback_db
