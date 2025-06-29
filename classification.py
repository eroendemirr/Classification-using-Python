# Gerekli kütüphaneler
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# Verileri oku (Index sütunu artık veri değil, satır etiketi olur)
veriler = pd.read_csv('veriler.csv', index_col=0)
print("Veri çerçevesi:\n", veriler)

# Cinsiyet sütununu al (hedef - y)
y = veriler[['cinsiyet']].values
print("Cinsiyet (orijinal):\n", y)

# Cinsiyeti sayısal hale getir (k=0, e=1)
le = preprocessing.LabelEncoder()
y = le.fit_transform(y.ravel())  # ravel() ile 1D diziye çevir
print("Cinsiyet (sayısal):\n", y)

# Giriş verisi olarak boy, kilo, yaş sütunlarını al
X = veriler[['boy', 'kilo', 'yas']].values
print("Giriş verisi (X):\n", X)

# Eğitim ve test verilerine ayır
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Çıktıları kontrol et
print("x_train:\n", x_train)
print("x_test:\n", x_test)
print("y_train:\n", y_train)
print("y_test:\n", y_test)
