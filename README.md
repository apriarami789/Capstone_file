# SleepWell AI – Prediksi & Edukasi Kesehatan Tidur Berbasis AI

**Website:** [capstone-file.vercel.app](https://capstone-file.vercel.app)

---

## 🛌 Overview

**SleepWell AI** adalah aplikasi web berbasis Artificial Intelligence untuk memprediksi, memantau, dan meningkatkan kualitas tidur masyarakat Indonesia. Platform ini memanfaatkan teknologi machine learning, visualisasi interaktif, serta edukasi kesehatan berbasis CBT-I (Cognitive Behavioral Therapy for Insomnia). Semua dirancang untuk memberikan insight dan solusi personal agar pengguna dapat mencapai tidur yang optimal—dengan antarmuka profesional, gratis, dan menjaga privasi data.

---

## 🎯 Fitur Utama

* **Prediksi Tidur Otomatis:**
  Input data harian (aktivitas fisik, stres, detak jantung, langkah), SleepWell AI secara otomatis menganalisis kualitas tidur, durasi, serta mendeteksi potensi gangguan (insomnia, sleep apnea, atau normal) dengan model ML terkini.

* **Saran Personal & CBT-I:**
  Pengguna mendapat rekomendasi personal (tips tidur, sleep hygiene, hingga CBT-I) yang disesuaikan dengan hasil prediksi, serta panduan tindakan sesuai profil risiko.

* **Visualisasi Riwayat & Progress:**
  Riwayat dan tren tidur divisualisasikan dalam grafik interaktif untuk memantau progress kesehatan tidur pengguna secara mudah.

* **Privasi & Manajemen Data:**
  Seluruh data pengguna dienkripsi (Supabase), dapat diunduh dalam format CSV, dan tidak pernah dijual ke pihak ketiga.

* **Multi-user & Onboarding Mudah:**
  Registrasi, login, serta profil pengguna yang personal, dengan proses yang mudah dan modern.

---

## 🚀 Demo Langsung

Aplikasi SleepWell AI dapat diakses melalui:
[https://capstone-file.vercel.app](https://capstone-file.vercel.app)

---

## 🏗️ Arsitektur & Teknologi

* **Frontend:**

  * HTML5, CSS3, JavaScript (Vanilla, Responsive UI)
  * Chart.js (visualisasi data interaktif)
  * Custom CSS + variable design system

* **Backend & Database:**

  * [Supabase](https://supabase.com/) — otentikasi, database, storage
  * Machine Learning API: Hugging Face Spaces (endpoint public)

* **Deployment:**

  * [Vercel](https://vercel.com/) (static hosting, CI/CD support)

---

## 📁 Struktur Project

```
├── index.html              # Landing page & penjelasan produk
├── login-user.html         # Login pengguna
├── sign-up.html            # Registrasi akun
├── main-menu.html          # Menu utama (navigasi)
├── form-input.html         # Input data tidur harian
├── hasil-prediksi.html     # Hasil prediksi, tips, & saran CBT-I
├── riwayat.html            # Riwayat & grafik kualitas tidur
├── style/                  # CSS, gambar logo, icon
├── cbti/                   # Edukasi/solusi CBT-I (opsional)
```

---

## ⚡ Cara Install & Deploy (di Vercel/GitHub Pages)

1. **Clone Repository**

   ```bash
   git clone https://github.com/username/sleepwell-ai.git
   cd sleepwell-ai
   ```

2. **(Opsional) Edit konfigurasi Supabase atau ML endpoint jika perlu**
   Semua credential dan endpoint sudah hardcoded untuk demo di file JS (tidak perlu backend custom).

3. **Deploy di Vercel**

   * Login ke [Vercel](https://vercel.com/)
   * Klik **New Project** → pilih repo ini → deploy
     *(Atau upload zip static HTML/JS/CSS)*

4. **Akses aplikasi**
   Web siap digunakan di link Vercel yang diberikan (contoh: `https://capstone-file.vercel.app`).

---

## 🔐 Keamanan & Privasi

* Data pengguna **dienkripsi** di Supabase, hanya bisa diakses oleh user yang bersangkutan.
* Tidak ada cookies tracking pihak ketiga.
* Semua kode bersifat open-source dan audit-able.

---

## 👨‍💻 Tim & Kontribusi

* Developer: \[Nama Anda], \[Nama Anggota]
* Mentor: \[Nama Mentor, jika ada]
* Powered by: DevAcademy.id, Supabase, Hugging Face, Chart.js, Vercel

Jika ingin berkontribusi, silakan fork repository dan submit Pull Request.

---

## 📝 Lisensi

Aplikasi ini bersifat open-source, bebas digunakan untuk riset dan edukasi.
Hak cipta © 2025 SleepWell AI Team.

---

## 📧 Kontak

* Email: [support@sleepwellai.id](mailto:support@sleepwellai.id)
* Instagram: [@sleepwellai.id](#)
* Website: [https://capstone-file.vercel.app](https://capstone-file.vercel.app)

---

