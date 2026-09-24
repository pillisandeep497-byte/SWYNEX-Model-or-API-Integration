import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="AI Website Copy Generator",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ AI Website Copy Generator")
st.write("Generate website content for local restaurants using AI.")

business_name = st.text_input(
    "Restaurant Name",
    placeholder="Spice Garden"
)

business_type = st.selectbox(
    "Business Type",
    ["Restaurant", "Cafe", "Bakery", "Food Truck"]
)

city = st.text_input(
    "City",
    placeholder="Visakhapatnam"
)

generate = st.button("Generate Website Copy")

if generate:

    if not business_name:
        st.warning("Enter restaurant name")
        st.stop()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    prompt = f"""
    Create website copy for:

    Business Name: {business_name}
    Type: {business_type}
    City: {city}

    Generate:

    1. Hero Section
    2. About Us
    3. Why Choose Us
    4. Services
    5. Call To Action
    """

    with st.spinner("Generating..."):

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    result = response.choices[0].message.content

    st.success("Content Generated Successfully")

    st.markdown(result)