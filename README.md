Project ini dibuat untuk praktikum **Pengolahan Citra Digital (Pekan 7)**  
Materi: *Segmentasi Lanjut (Edge-based & Region-based)*  
Dosen: **DR ARYA ADHYAKSA WASKITA S.SI.,M.SI**  

---

## 📌 Deskripsi Singkat

Repositori ini berisi implementasi segmentasi citra menggunakan metode:
1. **Edge-based Segmentation**
   - Sobel Operator  
   - Canny Edge Detector
2. **Region-based Segmentation**
   - Region Growing  
   - Watershed Algorithm
3. **Perbandingan Hasil Segmentasi**

Program menampilkan hasil visual untuk tiap metode menggunakan `matplotlib`.

---

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  
- Matplotlib  

---

1. **Clone atau download repo ini:**
   ```bash
   git clone https://github.com/username/segmentasi-citra.git
   cd segmentasi-citra
   ```

2. **Instal library yang dibutuhkan:**
   ```bash
   pip install opencv-python numpy matplotlib
   ```

3. **Jalankan di PyCharm atau terminal:**
   ```bash
   python segmentation_blog_demo.py
   ```

4. **Ubah nama file gambar:**
   Di dalam `segmentation_blog_demo.py`, ganti baris:
   ```python
   image_path = 'contoh.jpg'
   ```
   dengan nama file gambar kamu, misalnya:
   ```python
   image_path = 'daun.png'
   ```

5. **Lihat hasil:**
   Hasil visualisasi (Sobel, Canny, Region Growing, dan Watershed) akan muncul di jendela matplotlib.

---


### 1️⃣ `sobel_edge_detection(image_path)`
Mendeteksi tepi berdasarkan gradien menggunakan operator Sobel.  
- Menghitung turunan arah X dan Y.  
- Menggabungkan hasil jadi magnitude.  
- Menampilkan hasil dalam 3 subplot (Sobel X, Y, Magnitude).

### 2️⃣ `canny_edge_detection(image_path)`
Menggunakan algoritma Canny untuk deteksi tepi.  
- Melibatkan Gaussian blur, perhitungan gradien, non-maximum suppression, dan hysteresis thresholding.  
- Memberikan hasil tepi yang halus dan bersih.

### 3️⃣ `region_growing(image, seed, threshold)`
Melakukan segmentasi berbasis kemiripan.  
- Dimulai dari titik awal (seed).  
- Menambahkan piksel tetangga jika selisih intensitas < threshold.

### 4️⃣ `watershed_segmentation(image_path)`
Menggunakan algoritma Watershed berdasarkan topografi gradien.  
- Menerapkan threshold dan distance transform.  
- Memisahkan region foreground dan background.  
- Garis batas ditandai dengan warna merah.

### 5️⃣ `compare_segmentation_methods(image_path)`
Menjalankan semua metode (Otsu, Canny, Watershed) dan menampilkan hasil perbandingan.

---

| Metode | Cocok Untuk | Kelebihan | Kekurangan |
|---------|--------------|------------|-------------|
| **Thresholding (Otsu)** | Citra kontras tinggi | Cepat & mudah | Tidak cocok untuk pencahayaan tidak merata |
| **Edge-based (Canny/Sobel)** | Objek dengan batas jelas | Akurat mendeteksi tepi | Tidak membentuk region utuh |
| **Region-based (Watershed/Region Growing)** | Objek homogen | Segmentasi menyeluruh | Sensitif terhadap noise dan seed point |

---

1. Membaca gambar (`image_path`)
2. Menjalankan deteksi Sobel dan Canny
3. Melakukan segmentasi Watershed
4. Menampilkan perbandingan hasil

```python
if __name__ == "__main__":
    image_path = 'contoh.jpg'
    sobel_edge_detection(image_path)
    canny_edge_detection(image_path)
    watershed_segmentation(image_path)
    compare_segmentation_methods(image_path)
```

---

## 📸 Contoh Output
| Metode | Hasil |
|:-------|:------|
| Sobel Edge | ![sobel](images/sobel_example.png) |
| Canny Edge | ![canny](images/canny_example.png) |
| Watershed | ![watershed](images/watershed_example.png) |

---

## 👨‍💻 Penulis
**Nama:** Ferdi Zandio
**Mata Kuliah:** Pengolahan Citra Digital  
**Topik:** Segmentasi Lanjut (Edge-based & Region-based)

---

## 📬 Cara Upload ke GitHub

1. Buka [https://github.com](https://github.com) dan login.
2. Klik **New Repository** → beri nama `UTSFerdiZandio7`
3. Upload file:
   - `UTSFerdiZandio7.py`
   - `README.md`
   - Gambar uji (misal: `img2.jpg`)
4. Atau gunakan perintah Git:
   ```bash
   git init
   git add .
   git commit -m "Upload final project segmentasi citra"
   git branch -M main
   git remote add origin https://github.com/<username>/segmentasi-citra.git
   git push -u origin main
   ```

5. Link GitHub hasil upload:
   ```
   https://github.com/<username>/UTSFerdiZandio7
   ```
   Kirim link ini sebagai tugas kamu.

---

Proyek ini bersifat open-source untuk keperluan pembelajaran akademik.
