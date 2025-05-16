from database.basemodel import db_session


from apps.posts.models import Category


def init_category():
    """
    Initialize the database with default categories.
    """
    categories = [
        "Technology",
        "Health",
        "Travel",
        "Food",
        "Lifestyle",
        "Education",
        "Finance",
        "Entertainment"
    ]

    for category_name in categories:
        category = Category(name=category_name)
        db_session.add(category)

    db_session.commit()
    print("Default categories have been added to the database.")
    print("Database initialized with default categories.")

init_category()
