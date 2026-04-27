# Solar Radiation Prediction & Model Interpretability

This repository contains our coursework implementation for interpreting Machine Learning models trained to predict solar radiation using weather sensor data from the TAHMO network.

## 👥 Group Members

| Name | Registration Number |
|------|---------------------|
| Kigozi Allan | 2400725792 |
| Keith Paul Kato | 2400726593 |
| Mugole Joel | 2400707060 |
| Nalubega Shadiah | 2400708715 |
| Ageno Elizabeth | 2400725850 |

## 🎯 Project Overview

The objective of this project is to train three supervised regression models on a real-world weather dataset and interpret their predictions using model-agnostic explanation techniques.

**Task:** Predict incoming solar radiation ($W/m^2$) based on weather measurements (precipitation, relative humidity, temperature) and spatial-temporal context constraints.

### Machine Learning Models Evaluated:
1. **Decision Tree Regressor**
2. **Random Forest Regressor**
3. **Feed-Forward Neural Network (MLP)**

### Interpretation Methods Used:
1. **SHAP (Shapley Additive Explanations):** Used for **global** feature attribution to understand the overall impact of features on the model predictions.
2. **LIME (Local Interpretable Model-agnostic Explanations):** Used for **local** per-prediction attribution to explain why the model made a specific prediction on a single instance.

## 📂 Repository Contents

* `Solar_Radiation_Prediction.ipynb`: The main Jupyter Notebook containing the full pipeline (Data Loading, EDA, Preprocessing, Model Training, Evaluation, and SHAP/LIME interpretations).
* `dataset_data_dictionary.csv`: A dictionary explaining the dataset variables.
* `Third coursework.pdf`: The detailed coursework instructions and requirements.
* Large datasets (`Train.csv`, `Test.csv`, `SampleSubmission.csv`) are intentionally ignored via `.gitignore` to keep the repository lightweight.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Robotics1025/solar-radiatuion-prediction.git
   ```
2. Place the dataset files (`Train.csv`, `Test.csv`, `SampleSubmission.csv`) in the root directory.
3. Open `Solar_Radiation_Prediction.ipynb` in Jupyter Notebook or VS Code to run the analysis.
