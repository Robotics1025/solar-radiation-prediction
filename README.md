# Solar Radiation Prediction & Model Interpretability

This repository contains our coursework implementation for interpreting Machine Learning models trained to predict solar radiation using weather sensor data from the TAHMO network.

## 👥 Group Members

| Name | Email | Registration Number |
|------|-------|---------------------|
| Kigozi Allan | chigozieallanie@gmail.com | 24/U/25792/PS |
| Keith Paul Kato | keithpaulkato@gmail.com | 24/U/26593/EVE |
| Mugole Joel | joelmugole74@gmail.com | 24/U/07060/EVE |
| Nalubega Shadiah | shadiaahmed1302@gmail.com | 24/U/08715/EVE |
| Ageno Elizabeth | [EMAIL_ADDRESS] | 24/U/25850/EVE |

## 📓 The Notebook & Pipeline

The core of this project is maintained in `Solar_Radiation_Prediction.ipynb`, which contains the full data science pipeline from start to finish. Our pipeline consists of the following steps:

1. **Data Loading & Validation**: Securely loading `Train.csv` and validating the schemas against the data dictionary.
2. **Exploratory Data Analysis (EDA)**: Understanding data distributions, identifying missing values, visualizing the diurnal and monthly trends of solar radiation, and checking for feature collinearity.
3. **Preprocessing & Feature Engineering**: 
   - Extracting time-of-day and seasonality (hours and months) from timestamps.
   - Performing standard scaling on numerical data (e.g., Temperature, Relative Humidity) and creating one-hot encodings where necessary.
4. **Train/Validation Split**: Segmenting the dataset sequentially to preserve the temporal aspects of the weather data.
5. **Model Training**: Constructing the regression models and fitting them to the processed dataset.
6. **Evaluation**: Generating and comparing quantitative regression metrics (RMSE, MAE, R²).
7. **Interpretability**: Applying state-of-the-art global and local explanation techniques to demystify our black-box models.

## 🧠 Algorithms Used

To predict incoming solar radiation ($W/m^2$), we evaluated three distinct regression models, each offering unique strengths:

1. **Decision Tree Regressor**: A highly interpretable algorithm that naturally splits data into regions. While it tends to overfit, it provides an excellent baseline and complete transparency.
2. **Random Forest Regressor**: An ensemble approach that builds multiple decision trees and aggregates them. This naturally mitigates the overfitting of standalone decision trees, producing robust and strong predictions.
3. **Feed-Forward Neural Network (MLP)**: A deep learning artificial neural network (Multi-Layer Perceptron) that captures deeply non-linear relationships by shifting and distributing feature importance across neurons.

> After the models were created, we utilized **SHAP** for *global interpretability* (understanding which features were most universally dominant), and **LIME** for *local interpretability* (explaining why the models predicted specific short-term spikes in radiation). Both techniques emphasized the profound impact of the 'time of day' and 'temperature' features!

## 📊 Evaluation Metrics

Below are the final regression metrics derived from evaluating our models on the held-out validation dataset:

| Model | Root Mean Squared Error (RMSE) | Mean Absolute Error (MAE) | R² Score |
|-------|--------------------------------|---------------------------|----------|
| **Random Forest** | 91.72 | 44.75 | 0.897 |
| **Feed-Forward Neural Network** | 93.59 | 52.22 | 0.893 |
| **Decision Tree** | 110.32 | 55.64 | 0.851 |

**Conclusion**: The Random Forest cleanly outperformed the other models, explaining approximately 89.7% of the variance (R²) in our validation target. The Decision Tree was predictably the least accurate, but remains the easiest to visually interpret.

## 📂 Repository Contents

* `Solar_Radiation_Prediction.ipynb`: The main execution notebook.
* `dataset_data_dictionary.csv`: A dictionary explaining all variables.
* `Third coursework.pdf`: Project instructions and requirements.
* Large CSVs are ignored via `.gitignore` to keep bounds strict.

## 🚀 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Robotics1025/solar-radiatuion-prediction.git
   ```
2. Manually position your downloaded `Train.csv` and `Test.csv` within the root directory.
3. Launch `Solar_Radiation_Prediction.ipynb` in a Jupyter Notebook, Google Colab, or VS Code environment.
