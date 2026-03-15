# 🏥 Medical Cost Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-red?style=flat-square&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8.0-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A **Machine Learning web application** that predicts hospital/medical treatment costs based on patient attributes using a trained Linear Regression model — deployed with Streamlit for an interactive user experience.

---

## 📌 Project Overview

Medical costs vary significantly based on factors like age, BMI, smoking habits, and region. This project builds a predictive model trained on real-world insurance data to estimate individual medical expenses, helping users understand potential healthcare costs.

---

## ✨ Features

- 🔮 **Instant Predictions** — Enter patient info and get a cost estimate in one click
- 📊 **Data-Driven** — Trained on a real insurance dataset with 1,338 records
- 🧠 **Smart Preprocessing** — Handles categorical variables and feature scaling automatically
- 🌐 **Web App Interface** — Clean, interactive UI built with Streamlit
- 💾 **Pre-trained Model** — Serialized `model.pkl` for fast inference without retraining

---

## 🗂️ Project Structure

```
Medical-Cost-prediction/
├── app.py                 # Streamlit web application
├── medical-cost.ipynb     # Jupyter Notebook (EDA + Model Training)
├── insurance.csv          # Dataset (1,338 records)
├── model.pkl              # Trained ML model (serialized pipeline)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🤖 Machine Learning Workflow

| Step | Description |
|------|-------------|
| 1️⃣ Data Loading | Load `insurance.csv` using Pandas |
| 2️⃣ EDA | Explore distributions, correlations, and outliers |
| 3️⃣ Preprocessing | `ColumnTransformer` with `StandardScaler` + `OneHotEncoder` |
| 4️⃣ Model Training | `LinearRegression` via Scikit-learn `Pipeline` |
| 5️⃣ Serialization | Save pipeline as `model.pkl` using `joblib` |
| 6️⃣ Deployment | Streamlit app loads model and serves predictions |

---

## 📥 Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `age` | Numeric | Age of the primary beneficiary |
| `sex` | Categorical | Gender (`male` / `female`) |
| `bmi` | Numeric | Body Mass Index |
| `children` | Numeric | Number of dependents (0–5) |
| `smoker` | Categorical | Smoking status (`yes` / `no`) |
| `region` | Categorical | US region (`southwest`, `southeast`, `northwest`, `northeast`) |

---

## 🛠️ Technologies Used

| Library | Version | Purpose |
|---------|---------|---------|
| `streamlit` | 1.55.0 | Web UI framework |
| `scikit-learn` | 1.8.0 | ML model & preprocessing |
| `pandas` | 2.3.3 | Data manipulation |
| `numpy` | 2.4.3 | Numerical computing |
| `joblib` | 1.5.3 | Model serialization |
| `matplotlib` | 3.10.8 | Data visualization (notebook) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Yash12-cloud/Medical-Cost-prediction.git
cd Medical-Cost-prediction
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

---

## 📓 Explore the Notebook

For a full walkthrough of the EDA and model training process, open the Jupyter Notebook:

```bash
jupyter notebook medical-cost.ipynb
```

---

## 📊 Dataset

- **Source**: [Kaggle — Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Records**: 1,338 rows × 7 columns
- **Target Variable**: `charges` (individual medical costs in USD)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙋‍♂️ Author

**Yash** — [GitHub](https://github.com/Yash12-cloud)

> ⭐ If you found this project useful, please give it a star!
