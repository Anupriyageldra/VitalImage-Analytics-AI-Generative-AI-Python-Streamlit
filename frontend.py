import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_Key import api_Key

# Configure genai with API key
genai.configure(api_key=api_Key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Apply safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_prompt = """
As a highly skilled and experienced medical practitioner specializing in image analysis, you are entrusted with the critical responsibility of analyzing medical images for a leading hospital. Your role is pivotal in identifying anomalies, diseases, or any other health issues that could impact patient outcomes. Accuracy, clarity, and actionable insights are essential in your reports.

### Primary Responsibilities:
1. **Detailed Analysis**:
   - Conduct an in-depth examination of the medical image provided.
   - Identify and describe any observable anomalies, abnormalities, or disease markers.
   - Ensure that findings are supported by clear observations and explanations, avoiding ambiguity.

2. **Findings Report**:
   - Document all findings in a structured, professional, and concise format.
   - Include visual observations and, where possible, correlate these with potential underlying medical conditions.

3. **Highlight the Main Cause**:
   - Pinpoint the **primary cause or contributing factor** of the observed condition.


4. **Recommendations and Next Steps**:
   - Suggest relevant diagnostic tests, imaging, or medical consultations that can provide further clarity.
   - Outline immediate actions or precautions the patient or physician should take based on the findings.

5. **Treatment Suggestions**:
   - Provide potential treatment recommendations tailored to the observed condition.
   - Highlight both medical and lifestyle interventions where applicable.
   - Use evidence-based approaches to suggest actionable solutions.

---

### Additional Guidelines:
- **Context Sensitivity**: Limit responses to cases directly related to human health. Politely decline to analyze unrelated images with an appropriate note.
- **Image Quality**: If the image quality is insufficient for proper analysis, mention this explicitly, along with suggestions to improve image acquisition.
- **Clear Communication**: Avoid technical jargon unless essential; ensure the output is accessible to both medical professionals and non-specialists.
- **Ethical Disclaimer**: Conclude every report with: _"Consult with a licensed medical professional before making any decisions."_  

---

### Output Format:
Your response should adhere to this structure for clarity and comprehensiveness:
- **Detailed Analysis**: Provide an in-depth breakdown of the image findings.  
- **Findings Report**: Summarize the observations in a concise and professional format.  
- **Highlight the Main Cause**: Emphasize the primary cause of the issue using **bold red text**.   
- **Recommendations and Next Steps**: Suggest further diagnostic steps or actions.  
- **Treatment Suggestions**: Propose potential medical and lifestyle interventions.  

---

### Example Use Case:
If analyzing an X-ray of the chest showing signs of pneumonia:
1. **Detailed Analysis**: "The image displays patchy opacities in the lower right lung, indicative of alveolar consolidation."  
2. **Findings Report**: "Observations suggest a bacterial infection, consistent with community-acquired pneumonia."   
3. **Recommendations and Next Steps**: "Recommend a sputum culture and sensitivity test to confirm bacterial strain. Immediate referral to a pulmonologist is advised."  
4. **Treatment Suggestions**: "Initial empirical antibiotic therapy with amoxicillin-clavulanate is recommended, alongside supportive care (e.g., hydration, rest)."  

---

This advanced prompt ensures that your analysis is highly professional, actionable, and patient-centric, while maintaining an ethical and empathetic approach.

"""


# Model configuration
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Set the page configuration
st.set_page_config(page_title="Vital Image Analysis", page_icon=":robot:", layout="wide")

# Add custom CSS for background and styling
st.markdown(
    """
    <style>
    body {
        background-color: #ffc0cb; /* Pink Background */
        color: #000;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #000; /* Black Title */
        margin-bottom: 1rem;
    }
    .subheader {
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 2rem;
        color: #555; /* Subheader in dark gray */
    }
    .analysis-section {
        background: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
    }
    .sidebar-button {
        background-color: #004c97;
        color: #fff;
        border: none;
        padding: 10px 20px;
        text-align: center;
        font-size: 1rem;
        border-radius: 5px;
        cursor: pointer;
        margin: 5px 0;
    }
    .sidebar-button:hover {
        background-color: #0066cc;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for storing analysis results
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = []

# Sidebar Navigation
st.sidebar.markdown('<h2 style="color: #004c97;">Navigation</h2>', unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ["Home", "Upload Image", "View Analysis"], index=0)

# Title and Subheader
st.markdown('<div class="title">👩🏻‍⚕️ Vital Image Analytics 📈</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">An application to assist in analyzing medical images.</div>', unsafe_allow_html=True)

# Navigation logic
if page == "Home":
    st.write("### 🏠 Welcome to the Vital Image Analysis tool!")
    st.write("Navigate to **Upload Image** to analyze medical images and view detailed results.")
elif page == "Upload Image":
    st.write("### 📤 Upload a Medical Image")
    uploaded_file = st.file_uploader("Upload a medical image for analysis", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, width=300, caption="Uploaded Medical Image")
        submit_button = st.button("🔍 Generate Analysis")

        if submit_button:
            with st.spinner("Analyzing image... Please wait."):
                # Process the uploaded image
                image_data = uploaded_file.getvalue()

                # Prepare image for processing
                image_parts = [
                    {
                        "mime_type": "image/jpeg",
                        "data": image_data,
                    },
                ]

                # Prepare prompt
                prompt_parts = [
                    image_parts[0],
                    system_prompt,
                ]

                # Generate a response based on the prompt and image
                response = model.generate_content(prompt_parts)

                # Display results
                if response:
                    st.success("Analysis completed successfully!")
                    st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
                    st.markdown("### Here is the analysis based on your image:")
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Save the analysis to session state
                    st.session_state.analysis_results.append(response.text)
elif page == "View Analysis":
    st.write("### 📊 View Previously Generated Analyses")
    if st.session_state.analysis_results:
        for idx, result in enumerate(st.session_state.analysis_results, start=1):
            with st.expander(f"Analysis {idx}"):
                st.write(result)
    else:
        st.info("No analyses available. Please upload an image to generate analysis.")

# Footer
st.markdown('<div class="footer">© 2024 Vital Image Analytics </div>', unsafe_allow_html=True)
