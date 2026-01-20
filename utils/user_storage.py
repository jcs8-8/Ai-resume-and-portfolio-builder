import os

BASE_DIR = "data/users"

def _sanitize_user_id(user_id: str) -> str:
    """
    Make a filesystem-safe folder name.
    We keep it readable and stable for emails/usernames.
    """
    user_id = (user_id or "").strip().lower()
    safe = []
    for ch in user_id:
        if ch.isalnum() or ch in ("-", "_"):
            safe.append(ch)
        elif ch in (".", "@"):
            safe.append("_")
        else:
            safe.append("_")
    return "".join(safe).strip("_") or "user"

def get_user_dir(email):
    """
    Returns the per-user directory. For backwards compatibility, if the legacy
    directory exists (using raw email), we keep using it.
    """
    legacy = os.path.join(BASE_DIR, email)
    if email and os.path.exists(legacy):
        os.makedirs(legacy, exist_ok=True)
        return legacy

    safe_id = _sanitize_user_id(email)
    path = os.path.join(BASE_DIR, safe_id)
    os.makedirs(path, exist_ok=True)
    return path

def get_user_subdir(email, subfolder):
    path = os.path.join(get_user_dir(email), subfolder)
    os.makedirs(path, exist_ok=True)
    return path
