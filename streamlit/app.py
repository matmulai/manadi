import streamlit as st
from openai import OpenAI
from manadi.logger import GenAILogger
import logging

# Logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize logger
logger = GenAILogger("interactions.jsonl")

st.title("🧠 Manadi Chat & Logger")

# Sidebar to enter OpenAI API key
st.sidebar.header("API Configuration")
api_key = st.sidebar.text_input("Enter OpenAI API key:", type="password")

# Main prompt input
st.header("🚀 Chat with GenAI")
prompt = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key.")
    elif not prompt:
        st.error("⚠️ Please enter a prompt.")
    else:
        import openai
        openai.api_key = api_key

        with st.spinner("Generating response..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            ai_response = response.choices[0].message.content.strip()

        st.subheader("🤖 Response")
        st.write(ai_response)

        # Log automatically
        logger.log_interaction(prompt, ai_response)
        st.success("✅ Interaction logged successfully!")

# Optional Feedback
feedback = st.text_area("Provide feedback (optional):")
if st.button("Submit Feedback"):
    interactions = logger.get_all_interactions()
    if interactions:
        interactions[-1]['feedback'] = feedback
        logger.storage.save(interactions[-1])
        st.success("Feedback recorded!")

# Display past interactions
st.header("📚 Previous Interactions")
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

