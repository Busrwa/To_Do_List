# 📝 To-Do List / Notes App

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)](https://github.com/Busrwa/ToDo_List)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

---

## 🇹🇷 Türkçe

### 🔹 Proje Açıklaması
Bu proje, kullanıcıların not ekleyip, görüntüleyip, silebileceği **Python + Flask tabanlı bir To-Do List uygulamasıdır**.  
Kullanıcı yönetimi Flask-Login ile sağlanır ve veriler SQLite veritabanında tutulur. Modern web arayüzü ile kullanıcı dostudur.

### ⚙️ Teknik Detaylar
- **Ana Dosya:** `main.py` (projeyi başlatır)  
- **Web Arayüzü:** Flask + Bootstrap HTML (`templates/`)  
- **Veritabanı:** SQLite (`database.sqlite`)  
- **Kullanıcı Yönetimi:** Flask-Login  
- **Notlar:** Kullanıcıya özel; ekleme ve silme işlemleri desteklenir  
- **Kütüphaneler:** `flask`, `flask-login`, `flask-sqlalchemy`, `flask-bcrypt`  

### 💡 Kullanım Senaryoları
- Günlük görevleri ve notları yönetmek  
- Özel listeler oluşturmak ve takip etmek  
- Hızlı not ekleme ve silme  

### 🛠️ Kurulum ve Kullanım
```bash
git clone https://github.com/Busrwa/ToDo_List.git
cd ToDo_List
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
python -m pip install -r requirements.txt
python main.py
```

### 📤 Proje Çıktısı
- `/sign-up` ile kullanıcı oluşturma  
- Giriş yaparak not ekleme ve silme  
- Notlar kullanıcıya özel olarak görüntülenir  
- Flash mesajlar ile ekleme ve silme işlemleri bildirilir  

---

## 🇬🇧 English

### 🔹 Project Description
This is a **Python + Flask To-Do List app** where users can add, view, and delete notes.  
User management is handled with Flask-Login, and data is stored in an SQLite database. The interface is modern and user-friendly.

### ⚙️ Technical Details
- **Main File:** `main.py` (starts the project)  
- **Web Interface:** Flask + Bootstrap HTML (`templates/`)  
- **Database:** SQLite (`database.sqlite`)  
- **User Management:** Flask-Login  
- **Notes:** User-specific notes with add and delete functionality  
- **Libraries:** `flask`, `flask-login`, `flask-sqlalchemy`, `flask-bcrypt`  

### 💡 Use Cases
- Manage daily tasks and notes  
- Create and track personal lists  
- Quickly add or delete notes  

### 🛠️ Installation & Usage
```bash
git clone https://github.com/Busrwa/ToDo_List.git
cd ToDo_List
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
python -m pip install -r requirements.txt
python main.py
```

### 📤 Output
- Create a user via `/sign-up`  
- Log in to add and delete notes  
- Notes are displayed per user  
- Flash messages notify about add/delete actions
