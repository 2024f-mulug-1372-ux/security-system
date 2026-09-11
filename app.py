import streamlit as st

st.set_page_config(
    page_title="Security Management System",
    page_icon="🔐"
)

st.title("🔐 Security Management System")
st.write("Manage security staff, visitors, and access records.")

# Store data
if "visitors" not in st.session_state:
    st.session_state.visitors = []

# Menu
choice = st.sidebar.selectbox(
    "Select Option",
    ["Dashboard", "Add Visitor", "Security Check"]
)

# Dashboard
if choice == "Dashboard":

    st.header("📊 Security Dashboard")

    st.metric("Total Visitors", len(st.session_state.visitors))

    if len(st.session_state.visitors) == 0:
        st.info("No visitor records available.")
    else:
        for visitor in st.session_state.visitors:
            st.write(
                f"👤 {visitor['name']} | "
                f"ID: {visitor['id']} | "
                f"Purpose: {visitor['purpose']} | "
                f"Status: {visitor['status']}"
            )

# Add Visitor
elif choice == "Add Visitor":

    st.header("➕ Add Visitor")

    name = st.text_input("Visitor Name")
    visitor_id = st.text_input("Visitor ID")
    purpose = st.text_input("Purpose of Visit")

    if st.button("Register Visitor"):

        if name == "" or visitor_id == "" or purpose == "":
            st.error("Please fill all fields.")

        else:
            visitor = {
                "name": name,
                "id": visitor_id,
                "purpose": purpose,
                "status": "Pending"
            }

            st.session_state.visitors.append(visitor)

            st.success("Visitor registered successfully!")

# Security Check
elif choice == "Security Check":

    st.header("🛡️ Security Check")

    if len(st.session_state.visitors) == 0:
        st.info("No visitors to check.")

    else:

        visitor_names = [
            visitor["name"]
            for visitor in st.session_state.visitors
        ]

        selected = st.selectbox(
            "Select Visitor",
            visitor_names
        )

        status = st.selectbox(
            "Access Decision",
            ["Approved", "Denied"]
        )

        if st.button("Update Security Status"):

            for visitor in st.session_state.visitors:

                if visitor["name"] == selected:
                    visitor["status"] = status

                    if status == "Approved":
                        st.success("Visitor access approved.")

                    else:
                        st.warning("Visitor access denied.")