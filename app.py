import streamlit as st
from main import answer_customer_query
import utils.db_utils as db
import os

# ---------------------
# Page Configuration
# ---------------------
st.set_page_config(
    page_title="Offline AI Customer Support Chatbot",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------
# Sidebar
# ---------------------
with st.sidebar:
    st.title("⚙️ Settings")

    theme = st.radio("Theme Mode:", ["Light", "Dark"], key="theme_mode")

    st.checkbox("🎤 Voice Input")
    st.checkbox("🔊 Voice Output")

    st.markdown("---")
    st.button("💾 Export Chat", key="export_chat_btn")
    st.button("📊 Show Stats", key="show_stats_btn")


# ---------------------
# Main Title
# ---------------------
st.markdown(
    "<h1 style='text-align:center;'>🤖 Offline AI Customer Support Chatbot</h1>",
    unsafe_allow_html=True,
)
st.write("Ask questions, upload FAQs, rebuild knowledge, and chat with your assistant!")

# ---------------------
# Upload FAQ File Section
# ---------------------
st.subheader("📂 Upload FAQ File to Rebuild Knowledge")

uploaded_file = st.file_uploader(
    "Upload .txt file",
    type=["txt"],
    key="faq_upload"
)

if st.button("Rebuild FAQ Index", key="btn_rebuild_faq"):
    if uploaded_file is None:
        st.warning("Please upload a .txt file first!")
    else:
        with open("data/faqs.txt", "wb") as f:
            f.write(uploaded_file.read())

        st.info("Rebuilding FAISS Index... Please wait.")
        db.create_vector_db("data/faqs.txt")
        st.success("🎉 Knowledge base updated successfully!")

st.markdown("---")

# ---------------------
# Ask Question Section
# ---------------------
st.subheader("💬 Ask Your Question")

user_query = st.text_input("Type your question:", key="user_query_box")

if st.button("Get Answer", key="btn_get_answer"):
    if user_query.strip() == "":
        st.warning("Please enter a question!")
    else:
        with st.spinner("🤖 Generating answer... please wait..."):
            answer, refs = answer_customer_query(user_query)

        st.success(answer)

        # References Section
        st.subheader("📚 References Used")
        for i, ref in enumerate(refs):
            st.info(f"**Reference {i+1}:**\n{ref}")