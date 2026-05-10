# Titanic Survival Predictor 🚢

Aplikasi web sederhana untuk memprediksi kemungkinan selamat penumpang Titanic menggunakan Machine Learning.

## 📊 Dataset
Dataset yang digunakan adalah [Titanic Dataset](https://www.kaggle.com/competitions/titanic/data) dari Kaggle.

| Variable | Definition | Key |
|:---:|:---:|:---|
| Survived | Survival | 0 = No, 1 = Yes |
| Pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd |
| Sex | Sex | |
| SibSp | # of siblings / spouses aboard | |
| Parch | # of parents / children aboard | |
| Fare | Passenger fare | |
| Embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton |

## 🤖 Model
- Algorithm: **Random Forest Classifier**
- Hyperparameter Tuning: **RandomizedSearchCV** dengan 5-Fold Cross Validation
- Preprocessing: **Scikit-learn Pipeline** (Imputer, OneHotEncoder, MinMaxScaler, RobustScaler)

## 🚀 How to Run Locally

1. Clone repository
```bash
git clone https://github.com/Salwa-Syaharani/advanced-assignments-4-5.git
cd advanced-assignments-4-5
```

2. Buat dan aktifkan virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi
```bash
python -m streamlit run app.py
```

## 📦 Dependencies
- Streamlit
- Scikit-learn
- XGBoost
- Pandas
- Joblib
- Matplotlib

## 🌐 Demo
[Titanic Survival Predictor](https://advanced-assignments-4-5-j4vnwgwcwf2zhgqc7kfibb.streamlit.app/)