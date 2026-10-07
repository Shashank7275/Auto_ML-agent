# 🤖 Agentic AutoML AI

> An AI-powered AutoML application that turns an uploaded tabular dataset into an end-to-end machine-learning workflow — from data understanding and cleaning to preprocessing, model selection, evaluation, prediction, and an AI-generated explanation.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open%20App-success?style=for-the-badge)](https://auto-ml-agent.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-black?style=for-the-badge&logo=github)](https://github.com/Shashank7275/Auto_ML-agent)

---

## 🚀 Live Demo

🌐 **Try the deployed application:**  
https://auto-ml-agent.onrender.com

📦 **Source code:**  
https://github.com/Shashank7275/Auto_ML-agent

---

## 🎬 Demo Video

> **Add your demo video here after uploading `demo.mp4` to the repository under `assets/`.**

<video src="assets/demo.mp4" controls width="100%"></video>

**Demo:** Upload a CSV/XLSX dataset → AI agents analyze the data → clean and preprocess it → identify the target → train/evaluate models → select a suitable model → generate predictions and explain the results.

---

## 🖥️ Application Screenshots

### 1. AutoML Agent — Dataset Upload

![Agentic AutoML AI - Dataset Upload](<img width="1920" height="1080" alt="Screenshot (318)" src="https://github.com/user-attachments/assets/81c5f3ae-b9ff-48fd-baee-b2f1e9a83517" />
)

### 2. AutoML Agent — Workflow / Results

![Agentic AutoML AI - Workflow](assets/Screenshot-318.png)

---

## 🧠 What is Agentic AutoML AI?

**Agentic AutoML AI** is an intelligent machine-learning assistant designed to automate the repetitive parts of a typical tabular ML project.

Instead of manually performing every step, the application uses a multi-agent workflow to help with:

1. 📥 Dataset upload
2. 🔎 Dataset inspection and understanding
3. 🧹 Data cleaning
4. 🛠️ Feature preprocessing
5. 🎯 Target-column identification
6. 🤖 Model training
7. 📊 Model evaluation
8. 🏆 Best-model selection
9. 🔮 Prediction
10. 📝 AI-generated explanation and reporting

The project combines **Agno**, **Google Gemini**, **Pandas**, and **Scikit-learn** in a Streamlit application.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📂 CSV / XLSX Upload | Upload a tabular dataset directly from the web UI |
| 🔍 Data Analysis | Understand columns, data types, missing values and dataset structure |
| 🧹 Data Cleaning | Detect and handle common data-quality problems |
| ⚙️ Preprocessing | Prepare numerical and categorical features for ML |
| 🎯 Target Detection | Identify the target variable for supervised learning |
| 🤖 Model Training | Train suitable machine-learning models |
| 🏆 Model Selection | Compare evaluation results and select a strong candidate |
| 📈 Evaluation | View model performance and evaluation results |
| 🔮 Prediction | Generate predictions using the trained model |
| 🧠 Agentic AI | Use AI agents to coordinate and explain the ML workflow |
| 📊 Reports / Charts | Produce useful outputs for understanding the pipeline |
| ☁️ Render Deployment | Run the Streamlit application as a deployed web app |

---

## 🏗️ Agentic Workflow

```text
                    ┌──────────────────────┐
                    │   Upload CSV / XLSX  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Data Agent       │
                    │ Inspect / Understand │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Cleaning Agent     │
                    │ Missing / Duplicate  │
                    │ Data Quality Checks  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Preprocessing Agent  │
                    │ Encode / Scale /     │
                    │ Prepare Features     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Target Agent      │
                    │ Find Target Column   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Model Agent      │
                    │ Train ML Candidates  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Evaluation Agent    │
                    │ Compare Performance  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Best Model       │
                    │      + Prediction    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Report Agent     │
                    │ Explain the Results  │
                    └──────────────────────┘
```

---

## 🧩 Project Structure

```text
Auto_ML-agent/
│
├── agent/
│   ├── cleaning_agent.py
│   ├── data_agent.py
│   ├── eda_agent.py
│   ├── Evaluation_agent.py
│   ├── model_agent.py
│   ├── preprocessing_agent.py
│   ├── report_agent.py
│   └── target_agent.py
│
├── core/
│   ├── detector.py
│   ├── model_registry.py
│   ├── pipeline.py
│   └── state.py
│
├── tools/
│   ├── cleaning_tools.py
│   ├── data_tools.py
│   ├── eda_tools.py
│   ├── evaluation_tools.py
│   ├── model_tools.py
│   └── preprocessing_tools.py
│
├── models/
│   └── trained_models/
│
├── data/
│   └── uploads/
│
├── output/
│   └── charts/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── render.yaml
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit** — web application UI
- **Agno** — agentic AI workflow
- **Google Gemini / google-genai** — AI reasoning and explanations
- **Pandas** — data manipulation
- **NumPy** — numerical computing
- **Scikit-learn** — machine-learning pipeline and models
- **Matplotlib / Seaborn** — visualization
- **Joblib** — model persistence
- **OpenPyXL** — Excel file support
- **SQLAlchemy** — database-related utilities
- **Render** — deployment

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shashank7275/Auto_ML-agent.git
cd Auto_ML-agent
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The repository includes `requirements.txt` with the project's core dependencies and `runtime.txt` specifying Python 3.11.13. 

### 4. Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

> Never commit your real API key to GitHub.

### 5. Run locally

```bash
streamlit run app.py
```

Open the local Streamlit URL shown in your terminal.

---

## ☁️ Deploy on Render

This project includes a `render.yaml` configuration for deployment.

### Render configuration

```yaml
services:
  - type: web
    name: my-streamlit-app
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```

### Deployment steps

1. Push the project to GitHub.
2. Open Render.
3. Create a new **Web Service**.
4. Connect the GitHub repository.
5. Select the Python environment.
6. Add your required environment variables/secrets.
7. Deploy.
8. Open the generated Render URL.

### 🌐 Current deployed application

https://auto-ml-agent.onrender.com

---

## 📊 How to Use

### Step 1 — Upload a dataset

Upload a supported **CSV or XLSX** dataset.

### Step 2 — Let the agents analyze it

The agents inspect the dataset and determine useful information such as:

- rows and columns
- data types
- missing values
- duplicate records
- numerical features
- categorical features
- possible target column
- data-quality issues

### Step 3 — Clean and preprocess

The pipeline prepares the dataset for machine learning.

Typical operations can include:

- missing-value handling
- duplicate handling
- categorical encoding
- numerical preprocessing
- feature preparation
- train/test preparation

### Step 4 — Train and evaluate models

Candidate ML models are trained and evaluated.

The evaluation stage compares the available model results and identifies a suitable model based on the task and evaluation metrics.

### Step 5 — Prediction

Use the selected trained model to generate predictions.

### Step 6 — AI explanation

The agentic AI layer can explain the workflow and results in a more human-readable form.

---

## 🔐 Environment Variables

Create `.env` locally:

```env
GOOGLE_API_KEY=your_api_key
```

For Render, add the secret through the service's environment-variable settings instead of committing `.env`.

---

## 📦 Supported Dataset Formats

Currently supported by the application UI:

```text
CSV
XLSX
```

The deployed interface provides a dataset upload flow for tabular data.

---

## 🧪 Example Use Cases

This project can be useful for experimenting with:

- customer churn prediction
- sales prediction
- classification problems
- regression problems
- tabular business datasets
- exploratory data analysis
- automated ML experimentation
- ML project demonstrations
- AI/ML portfolio projects

---

## 🎯 Why Agentic AutoML?

Traditional ML workflow:

```text
Data → Clean → EDA → Preprocess → Train → Evaluate → Predict → Explain
```

Agentic AutoML workflow:

```text
              ┌──────────────────────┐
              │     User Dataset     │
              └──────────┬───────────┘
                         ▼
                ┌─────────────────┐
                │   AI Agents     │
                └────────┬────────┘
                         ▼
       ┌──────────────────────────────────┐
       │ Analyze → Clean → Prepare        │
       │ → Train → Evaluate → Predict     │
       │ → Explain                        │
       └────────────────┬─────────────────┘
                        ▼
                ┌─────────────────┐
                │   ML Results    │
                └─────────────────┘
```

The goal is to reduce repetitive manual ML work while keeping the workflow understandable.

---

## 📸 Screenshots

Place the supplied screenshots in:

```text
assets/
├── Screenshot-317.png
└── Screenshot-318.png
```

Then the README will display them automatically.

---

## 🎥 Demo Video

Place the supplied demo recording in:

```text
assets/demo.mp4
```

The README includes a video section so visitors can see the complete workflow.

> If GitHub does not render the relative `<video>` element in your repository view, upload the video to a GitHub Issue/Release or another video host and replace the video source with the resulting public URL.

---

## 🚀 Future Improvements

- Automatic problem-type detection
- More ML algorithms
- Hyperparameter optimization
- Cross-validation
- Feature importance
- SHAP explainability
- Prediction input form
- Downloadable prediction results
- Downloadable ML report
- Authentication
- Job history
- Model versioning
- Better error recovery between agents
- Larger dataset support
- Docker deployment

---

## 🤝 Contributing

Contributions, ideas, bug reports, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application.
5. Create a pull request.

---

## ⭐ Support

If this project is useful to you:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Open an issue
- 💡 Suggest improvements

---

## 👨‍💻 Author

**Shashank Singh**

GitHub:  
https://github.com/Shashank7275

Project:  
https://github.com/Shashank7275/Auto_ML-agent

Live Demo:  
https://auto-ml-agent.onrender.com

---

## 📄 License

Add your preferred license before publishing commercial distributions.

If you plan to sell the source code, define the license and usage rights clearly before distributing it.
