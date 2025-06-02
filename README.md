# ⚖️ Jura Modular

Willkommen bei **Jura Modular**, einem modernen, modularen Verwaltungssystem für Kanzleien, Hausverwaltungen und digitale Rechtsservices. Unser Projekt zielt darauf ab, juristische und verwaltungstechnische Abläufe effizient und benutzerfreundlich zu digitalisieren – für Kanzleien, Mandanten und Partner.

<p align="center">
  <img src="https://github.com/SCHEIDOMAT/overview/blob/main/assets/images/jura-modular.png" alt="Jura-Modular Logo" width="50%"/>
</p>

---

## 🚀 Projektübersicht

**Jura Modular** besteht aus zwei Hauptkomponenten:

* 🧠 **Backend**: Modular aufgebautes Django-System mit spezialisierten Apps
* 💻 **Frontend**: Angular-Anwendung für eine moderne Benutzeroberfläche

---

## 🗂️ Projektstruktur

```bash
jura-modular.org/
├── backend/
│   ├── kanzlei_apps/
│   │   ├── accounts/
│   │   ├── appointments/
│   │   ├── cases/
│   │   ├── hausverwaltung_app/
│   │   ├── kanzlei_app/
│   │   ├── scheidomat_app/
│   │   ├── users/
│   │   └── verwaltung_app/
│   ├── kanzlei_backend/ (Projektsettings)
│   ├── static/
│   └── manage.py
├── frontend/ (Angular App)
│   └── dist/
├── README.md
└── requirements.txt
```

---

## 🛠️ Verwendete Technologien

### Backend (🐍 Python / Django)

* Django 4+
* SQLite (für Entwicklung)
* Modularisierte Apps für unterschiedliche Domänen

### Frontend (⚡ Angular)

* Angular 17+
* REST-Anbindung via HTTPClient
* Responsive Design & UI-Komponenten

### DevOps & Tools (🔧)

* Git / GitHub
* PEP8-konformer Code
* Icon-Unterstützung via [Simple Icons](https://simpleicons.org/) oder [Twemoji](https://twemoji.twitter.com/)

---

## 📦 Installation (Entwicklungsumgebung)

### 1. Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 2. Frontend (Angular)

```bash
cd frontend
npm install
ng serve
```

---

## 👥 Mitwirkende

* 🧑‍💻 Projektleitung & Backend: \[Sascha Gebel / livednoiz]
* 🎨 Frontend & UI: \[optional]
* 📘 Dokumentation: \[optional]

---

## 💡 Vision

Jura Modular soll langfristig als Open-Source-Plattform wachsen – mit Erweiterbarkeit für weitere juristische Teilbereiche, API-Integration, mehrsprachigem Interface und AI-basierten Automatisierungen.

---

## 📜 Lizenz

Dieses Projekt verwendet eine [AGPLv3-Lizenz](./LICENSE) für nicht-kommerzielle Nutzung.

📌 Für kommerzielle Nutzung:
- Lizenzvereinbarung: [LICENSE-commercial.txt](./LICENSE-commercial.txt)
- Preisübersicht & Leistungen: [COMMERCIAL-OFFER.md](./COMMERCIAL-OFFER.md)

---

> **Hinweis:** Dieses Repository befindet sich aktuell in der aktiven Entwicklung. Pull Requests und Vorschläge sind herzlich willkommen! 🚧
