# Gender Classification from Physical Attributes using Python

This project demonstrates a basic machine learning workflow that uses physical attributes — height, weight, and age — to predict gender (male or female) based on labeled data.

## 📁 Dataset

The dataset (`veriler.csv`) contains the following columns:

- `Index`: Row number (used as DataFrame index)
- `cinsiyet`: Gender (categorical: "e" for male, "k" for female)
- `boy`: Height (in cm)
- `kilo`: Weight (in kg)
- `yas`: Age (in years)

## ⚙️ Preprocessing

- The gender column is label-encoded:  
  `"k"` → `0` (female), `"e"` → `1` (male)
- Features used for training: `boy`, `kilo`, `yas`
- The data is split into training and test sets using `train_test_split`

## 📌 Requirements

- Python 3.x
- pandas
- scikit-learn

You can install dependencies via pip:

```bash
pip install pandas scikit-learn
