import os
from datetime import datetime
from utils.user_storage import get_user_subdir

def save_resume_version(email, text):
    folder = get_user_subdir(email, "resumes")
    filename = f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    return filename

def load_resume_versions(email):
    folder = get_user_subdir(email, "resumes")
    return sorted(os.listdir(folder), reverse=True)


def save_cover_letter_version(email, text):
    folder = get_user_subdir(email, "cover_letters")
    filename = f"cover_letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    return filename


def load_cover_letter_versions(email):
    folder = get_user_subdir(email, "cover_letters")
    return sorted(os.listdir(folder), reverse=True)


def save_email_version(email, text):
    folder = get_user_subdir(email, "emails")
    filename = f"email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    return filename


def load_email_versions(email):
    folder = get_user_subdir(email, "emails")
    return sorted(os.listdir(folder), reverse=True)