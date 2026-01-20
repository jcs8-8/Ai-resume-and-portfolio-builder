import streamlit as st
from auth.auth_utils import register_user, authenticate_user

# -------------------------------------------------
# Config
# -------------------------------------------------
st.set_page_config(page_title="AI Resume Builder", layout="wide")

# -------------------------------------------------
# Session Init
# -------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None

if "user_fullname" not in st.session_state:
    st.session_state.user_fullname = None

# -------------------------------------------------
# Auto Redirect
# -------------------------------------------------
if st.session_state.authenticated:
    st.switch_page("pages/0_Dashboard.py")

# -------------------------------------------------
# UI
# -------------------------------------------------
st.title("🔐 AI Resume & Portfolio Builder")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------------------------------------
# LOGIN
# -------------------------------------------------
if choice == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, user = authenticate_user(email, password)

        if success:
            st.session_state.authenticated = True
            st.session_state.user_email = email
            st.session_state.user_fullname = user["fullname"]

            st.success("Login successful 🎉")
            st.switch_page("pages/0_Dashboard.py")
        else:
            st.error("Invalid email or password")

# -------------------------------------------------
# SIGN UP
# -------------------------------------------------
elif choice == "Sign Up":
    st.subheader("Create Account")

    fullname = st.text_input("Full Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if not all([fullname, username, email, password]):
            st.error("All fields are required")
        elif password != confirm:
            st.error("Passwords do not match")
        else:
            success, msg = register_user(
                email=email,
                username=username,
                fullname=fullname,
                password=password
            )

            if success:
                st.success(msg)
                st.info("You can now login using your email")
            else:
                st.error(msg)

