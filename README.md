# StuntingApp

StuntingApp adalah sebuah aplikasi berbasis Django untuk informasi dan pemantauan stunting pada anak.

## Cara Menjalankan Aplikasi

```bash
# 1. Pastikan Python sudah terinstal di komputer Anda. Anda dapat mengunduhnya di [Python.org](https://www.python.org/downloads/).

# 2. Clone repositori StuntingApp ke direktori lokal Anda:
git clone https://github.com/username/stunting_app.git

# 3. Pindah ke direktori proyek:
cd stunting_app

# 4. Buat dan aktifkan virtual environment:
python -m venv env
source env/bin/activate

# 5. Instal dependencies yang dibutuhkan:
pip install -r requirements.txt

# 6. Jalankan migrasi database:
python manage.py migrate

# 7. Jalankan server lokal:
python manage.py runserver
