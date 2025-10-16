import streamlit as st
import requests

# ---------------------------
# Streamlit App Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Blog Writer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Blog Writer")
st.markdown(
    """
    Enter a **blog topic or context**, and this app will generate a **long, detailed, plain-text blog** using the Replicate Granite LLM.
    """
)

# ---------------------------
# User Input
# ---------------------------
topic = st.text_input("Enter your blog topic or context:", placeholder="e.g., AI in Education, Travel Technology Trends")

if st.button("Generate Blog"):

    if not topic.strip():
        st.warning("Please enter a topic or context for the blog!")
    else:
        with st.spinner("Generating blog... This may take a few seconds."):
            # ---------------------------
            # API Configuration (LangFlow Granite)
            # ---------------------------
            api_key = "sk-xd_y557IZ0qnqpuahiffF-JeWQdOveVFNTMzuyRgq2o"
            url = "http://localhost:7860/api/v1/run/7b473c3a-52ea-4f2d-8682-ea27a4926f96"

            payload = {
                "output_type": "chat",  # Chat type output
                "input_type": "chat",
                "input_value": f"Write a very long, detailed, human-like blog in plain text about: {topic}"
            }

            headers = {
                "Content-Type": "application/json",
                "x-api-key": api_key
            }

            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
                data = response.json()

                # ---------------------------
                # Extract plain text safely
                # ---------------------------
                text_output = ""
                outputs_list = data.get("outputs", [])
                if outputs_list:
                    first_output = outputs_list[0]
                    try:
                        text_output = first_output["outputs"][0]["results"]["message"]["text"]
                    except (KeyError, IndexError, TypeError):
                        text_output = str(first_output)

                # ---------------------------
                # Display the blog
                # ---------------------------
                st.markdown("### Generated Blog:")
                st.text_area("", value=text_output.strip(), height=500)

            except requests.exceptions.RequestException as e:
                st.error(f"Error making API request: {e}")
            except ValueError as e:
                st.error(f"Error parsing response: {e}")
