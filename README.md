
# 🩺 VitalImage Analytics – AI-Powered Medical Image Analysis

**VitalImage Analytics** is a Generative AI-powered medical image analysis web application developed using Python, Streamlit, and Google's Gemini Vision model. The application enables users to upload skin-related medical images and obtain AI-generated observations, potential abnormality assessments, and structured recommendations through an interactive web interface.

The project explores the application of multimodal Generative AI in preliminary medical image assessment, combining image understanding, prompt engineering, and an interactive user experience.

---

## 📌 Project Overview

VitalImage Analytics aims to simplify preliminary medical image assessment through an AI-powered interface. By integrating Google's Gemini Vision model, the application processes uploaded medical images and generates descriptive reports based on visible image characteristics.

Users can upload images in PNG, JPG, and JPEG formats and receive structured AI-generated responses covering image observations, potential findings, possible contributing factors, recommended next steps, and general treatment considerations.

The application also includes a multi-page interface that allows users to navigate between the home page, image upload section, and previously generated analysis reports.

## ✨ Key Features

- **AI-Powered Image Analysis:** Integrates Google's Gemini Vision model to analyze uploaded medical images.
- **Skin Abnormality Assessment:** Generates observations of potentially concerning skin features based on the uploaded image.
- **Multimodal AI Integration:** Processes both image data and text-based instructions to generate contextual responses.
- **Interactive Image Upload:** Supports PNG, JPG, and JPEG image formats.
- **Structured Analysis Reports:** Generates organized reports containing:
  - Detailed Analysis
  - Findings Report
  - Highlight the Main Cause
  - Recommendations and Next Steps
  - Treatment Suggestions
- **Multi-Page Navigation:** Includes Home, Upload Image, and View Analysis sections.
- **Analysis History:** Uses Streamlit Session State to maintain previously generated analysis results during the active session.
- **Custom User Interface:** Implements custom CSS styling, page layouts, navigation elements, and interactive components.
- **AI Safety Configuration:** Incorporates content safety settings to guide responsible AI-generated responses.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / Web Framework | Streamlit |
| Generative AI Model | Google Gemini Vision |
| AI Integration | Google Generative AI SDK |
| Image Processing | Multimodal Image Input |
| Styling | Custom CSS, HTML |
| State Management | Streamlit Session State |
| Prompt Engineering | Structured System Prompts |

## ⚙️ Application Workflow

1. **Image Upload:** Users upload a skin-related medical image through the Streamlit interface.
2. **Image Processing:** The application extracts the uploaded image data and prepares it for the AI model.
3. **AI Integration:** The image and structured system prompt are passed to Google's Gemini Vision model.
4. **Image Analysis:** The model interprets the visual information and generates descriptive observations.
5. **Report Generation:** The application displays the generated response in a structured format.
6. **Analysis History:** Generated reports are stored in Streamlit Session State and can be revisited through the View Analysis section.

## 🖥️ Application Modules

### 1. Home
Provides an introduction to VitalImage Analytics and guides users through the application's functionality.

### 2. Upload Image
Allows users to upload medical images and initiate AI-powered analysis. The generated report is displayed through the interactive Streamlit interface.

### 3. View Analysis
Displays previously generated analysis reports using expandable sections, allowing users to revisit results within the active application session.

## 📂 Project Structure

```text
VitalImage-Analytics/
│
├── app.py                  # Main Streamlit application
├── api_Key.py              # API key configuration
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
└── assets/                 # Optional screenshots and UI assets
```

## 🚀 Installation and Setup

### Prerequisites
- Python 3.9 or later
- Google Gemini API key
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/VitalImage-Analytics.git
```

### Step 2: Navigate to the Project Directory

```bash
cd VitalImage-Analytics
```

### Step 3: Install Dependencies

```bash
pip install streamlit google-generativeai
```

### Step 4: Configure the API Key

Create a `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

Update your Python configuration to retrieve the key securely:

```python
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

## 🔮 Future Enhancements

- Integration of dedicated, clinically evaluated skin lesion classification models.
- Implementation of image preprocessing and enhancement techniques.
- Support for multiple medical image categories.
- Downloadable PDF reports for generated analyses.
- Persistent database integration for analysis history.
- Improved image validation and error handling.
- Enhanced UI with patient-friendly reporting and visualization features.
- Integration of verified medical guidelines and clinical evaluation workflows.

## 🎯 Project Objective

The primary objective of VitalImage Analytics is to explore how Generative AI and multimodal image understanding can support preliminary medical image assessment through an accessible web application.

The project demonstrates practical implementation of Generative AI APIs, prompt engineering, image-based AI interaction, Python application development, and interactive web interface design.

## ⚠️ Medical Disclaimer

VitalImage Analytics is an experimental AI-based medical image analysis application developed for educational and research purposes. It is not a clinically validated skin cancer detection or diagnostic system and cannot determine whether a skin lesion is benign or malignant.

AI-generated observations may be inaccurate or incomplete. They should not be used as a substitute for professional medical examination, diagnosis, or treatment. Always consult a qualified healthcare professional regarding skin abnormalities or medical concerns.

## 👩‍💻 Author

**Anupriya Geldra**


---

⭐ If you find this project interesting, consider giving the repository a star!
