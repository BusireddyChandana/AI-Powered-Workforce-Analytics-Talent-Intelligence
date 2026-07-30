import streamlit as st


# Demo users and roles
USERS = {
    "hr_admin": {
        "password": "admin123",
        "role": "HR Admin"
    },
    "manager": {
        "password": "manager123",
        "role": "Manager"
    },
    "employee": {
        "password": "employee123",
        "role": "Employee"
    }
}


def login():

    st.sidebar.subheader("🔐 User Login")

    username = st.sidebar.text_input(
        "Username"
    )

    password = st.sidebar.text_input(
        "Password",
        type="password"
    )


    if st.sidebar.button("Login"):

        if username in USERS and USERS[username]["password"] == password:

            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = USERS[username]["role"]

            st.sidebar.success(
                f"Logged in as {st.session_state['role']}"
            )

        else:
            st.sidebar.error(
                "Invalid username or password"
            )


def check_role():

    if "role" in st.session_state:
        return st.session_state["role"]

    return None