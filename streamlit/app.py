import streamlit as st
from manadiai.logger import GenAILogger

logger = GenAILogger(storage_path="interactions.jsonl")

st.title("🧠 ManadiAI Interaction Logger")

st.sidebar.header("Log a new interaction")

prompt = st.sidebar.text_area("Prompt")
response = st.sidebar.text_area("Response")
feedback = st.sidebar.text_area("Feedback (optional)")

if st.sidebar.button("Log Interaction"):
    if prompt and response:
        logger.log_interaction(prompt, response, feedback)
        st.sidebar.success("✅ Interaction logged successfully!")
    else:
        st.sidebar.error("⚠️ Prompt and response are required.")

st.header("📚 Logged Interactions")

interactions = logger.get_all_interactions()

if interactions:
    for idx, entry in enumerate(interactions[::-1], 1):
        st.subheader(f"Interaction {idx}")
        st.markdown(f"**Prompt:** {entry['prompt']}")
        st.markdown(f"**Response:** {entry['response']}")
        if entry.get("feedback"):
            st.markdown(f"**Feedback:** {entry['feedback']}")
        st.markdown("---")
else:
    st.info("No interactions logged yet.")

