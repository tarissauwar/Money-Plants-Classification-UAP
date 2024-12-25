# 🌿 Money-Plants-Classification

Proyek ini adalah implementasi berbasis Python untuk aplikasi pembelajaran mesin pada klasifikasi citra. Proyek ini menggunakan model CNN yang telah dilatih sebelumnya (VGG16 dan VGG19) untuk mengklasifikasikan gambar ke dalam kategori yang berbeda.

## 📂 Dataset

Dataset yang digunakan dalam proyek ini diambil dari Kaggle. Dataset ini berjudul **DiseaseClassifier: Money Plant Dataset** dan dapat diakses melalui [tautan berikut](https://www.kaggle.com/datasets/mdhasanahmad/diseaseclassifier-money-plant-dataset).

## 📚 Struktur Proyek

```
notebooks/
├── UAP_VGG16.ipynb                    # Notebook untuk melatih model menggunakan VGG16
├── UAP_VGG19.ipynb                    # Notebook untuk melatih model menggunakan VGG19
web/
├── app.py                             # Skrip aplikasi utama
├── klasifikasi_citra.py               # Logika klasifikasi
README.md                              # Dokumentasi proyek
requirements.txt                       # Dependensi Python
```

### Penjelasan Struktur:
1. **notebooks/**: Folder yang berisi file Jupyter Notebook untuk melatih model. Terdapat dua file:
   - **UAP_VGG16.ipynb**: File untuk melatih model dengan arsitektur VGG16.
   - **UAP_VGG19.ipynb**: File untuk melatih model dengan arsitektur VGG19.

2. **web/**: Folder yang berisi kode aplikasi utama, seperti:
   - **app.py**: Skrip utama untuk menjalankan aplikasi.
   - **klasifikasi_citra.py**: Berisi logika klasifikasi citra berdasarkan model yang telah dilatih.

3. **README.md**: File ini berisi deskripsi proyek dan dokumentasi.

4. **requirements.txt**: Daftar dependensi Python yang dibutuhkan untuk menjalankan proyek.

## 📦 Instalasi

1. **Klon repositori:**
   ```bash
   git clone <repository-url>
   cd Money-Plants-Classification-UAP
   ```

2. **Buat virtual environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate   # Di Windows: myenv\Scripts\activate
   ```

3. **Install dependensi:**
   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Penggunaan
### Melatih Model
Jika Anda ingin melatih model sendiri, Anda dapat melakukannya di Colab atau di lingkungan lokal Anda dengan mengikuti langkah-langkah di bawah ini.

1. **Melatih model VGG16:**
   - Buka file `UAP_VGG16.ipynb` di Jupyter Notebook atau di Google Colab.
   - Jalankan setiap sel untuk melatih model.

2. **Melatih model VGG19:**
   - Buka file `UAP_VGG19.ipynb` di Jupyter Notebook atau di Google Colab.
   - Jalankan setiap sel untuk melatih model.

   **Catatan:** Jika Anda lebih memilih untuk tidak menjalankan notebook secara lokal, Anda dapat menjalankannya langsung di [Google Colab](https://colab.research.google.com/). Cukup unggah file `.ipynb` dan jalankan di sana.

### Menggunakan Model yang Telah Dilatih
Jika Anda tidak ingin melatih model, Anda dapat menggunakan model yang sudah dilatih dan disimpan di folder **`model/`**. Anda bisa mengunduh model yang sudah dilatih dari [Google Drive](https://drive.google.com/drive/folders/1K4qxh9spP0Ubu6TguFoUPVIOV0PCEx7a) dan menyimpannya di folder `model/` dengan nama file `.keras`.

Setelah mengunduh model, Anda dapat langsung menjalankan aplikasi klasifikasi citra menggunakan model tersebut.

### Menjalankan Aplikasi Streamlit
Skrip utama aplikasi adalah `app.py`. Untuk menjalankan aplikasi Streamlit, gunakan perintah berikut:

```bash
streamlit run web/app.py
```

Aplikasi ini akan berjalan di localhost dan dapat diakses melalui browser di alamat `http://localhost:8501`.

## 📊 Hasil Pelatihan

### Model VGG16
**Hasil Grafik Akurasi dan Loss:**

![image](https://github.com/user-attachments/assets/2b8916ca-3475-4c03-9a66-d78bdae46917)

**Classification Report:**

![image](https://github.com/user-attachments/assets/ba4b0273-8207-43ab-819e-02aad7f2124a)

**Confussion Matrix:**

![image](https://github.com/user-attachments/assets/4bac51bd-0dc7-4515-a4fb-b71e11b53167)


### Model VGG19
**Hasil Grafik Akurasi dan Loss:**

![image](https://github.com/user-attachments/assets/4c5464c6-5196-4e30-a4db-148bf198f019)

**Classification Report:**

![image](https://github.com/user-attachments/assets/cbbe7329-0653-4cf3-b223-9cdff1ddc0da)

**Confussion Matrix:**

![image](https://github.com/user-attachments/assets/06c3bc9a-dd67-4513-8e99-d43c73a10f6a)

## 🔍 Model yang Digunakan

Proyek ini menggunakan dua arsitektur CNN yang telah dilatih sebelumnya:

1. **VGG16:**
   - Model ini terdiri dari 16 lapisan, termasuk lapisan convolutional dan pooling.
   - Dirancang untuk tugas klasifikasi citra umum, tetapi disesuaikan dengan dataset spesifik dalam proyek ini.

2. **VGG19:**
   - Mirip dengan VGG16, tetapi memiliki tiga lapisan tambahan, memberikan model lebih banyak kapasitas representasi.

Model dilatih menggunakan dataset gambar tanaman uang (money plants) untuk mengklasifikasikan jenis-jenis tanaman tersebut.

## 👨‍💻 Author

Proyek ini dikembangkan oleh **[Tarissa Rizky](https://github.com/tarissauwar)**.
