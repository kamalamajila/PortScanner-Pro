# 🚀 PortScanner Pro

Modern Flask web-based TCP port scanner with learning hub, scan history, and cybersecurity dashboard UI. Built for portfolio showcase and SOC analyst prep.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0.3-brightgreen.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/PortScanner_Pro?style=social)](https://github.com/YOUR_USERNAME/PortScanner_Pro)

## ✨ Features

- **Multi-threaded TCP scanning** (1-65535 full range)
- **Smart presets** (Top 100, Web, Database, Remote Access)
- **Service identification** + risk hints
- **Learning hub** (40+ important ports categorized)
- **Scan history dashboard**
- **Graphite & Ice UI** (responsive, mobile-first)
- **Production-ready** Flask architecture

## 🎯 Live Demo

[![Demo](https://img.shields.io/badge/DEMO-PortScanner_Pro-blue?style=for-the-badge)](https://portscanner-pro.onrender.com)




https://github.com/user-attachments/assets/d7a84191-8575-4932-869e-8ae62f0210d4





## 📁 Structure
PortScanner_Pro/
├── app.py # Flask app
├── scanner.py # Threaded scanner engine
├── learning_data.py # Port knowledge base
├── requirements.txt # pip install -r requirements.txt
├── templates/ # HTML templates
└── static/ # CSS + JS

text

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/PortScanner_Pro.git
cd PortScanner_Pro
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

pip install -r requirements.txt
python app.py
```

**Open:** http://127.0.0.1:5000

## 🛠️ Presets Available

| Mode | Range | Typical Use |
|------|-------|-------------|
| Top 100 | 1-100 | Quick recon |
| Top 1000 | 1-1000 | Standard scan |
| Web | 80,443,8080 | Web services |
| Database | 3306,5432,1433 | DB exposure |
| Remote | 22,23,3389 | Admin access |
| Full | 1-65535 | Complete audit |

## 📊 Sample Results
Target: scanme.nmap.org
Mode: Top 1000
Open Ports: 22(SSH), 80(HTTP), 9929(Nping)
Duration: 2.8s

text

## 🎨 Design System

- **Graphite & Ice palette** - Clean, professional, non-generic
- **Responsive grid** - Desktop + mobile
- **Modern dashboard layout**
- **Accessible dark mode**

## 🏢 For Recruiters

Demonstrates:
✅ Flask web development  
✅ Multithreaded networking  
✅ Modern responsive UI  
✅ Cybersecurity knowledge  
✅ Production architecture  
✅ Clean code structure  

## 🚀 Deploy (Free)

**Render.com** (Recommended):
1. Connect GitHub repo
2. `Build Command`: `pip install -r requirements.txt`
3. `Start Command`: `python app.py`

**Railway/Heroku** also supported.

## 📈 Future Roadmap

- CSV/PDF export
- Persistent history (SQLite)
- Service banner grabbing
- UDP scan simulation
- Multi-target batch scanning

## 📄 License

MIT - Free to use, modify, deploy.

---

⭐ **Star if helpful for your SOC journey!**
