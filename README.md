# PortScanner Pro

A modern Flask-based web port scanner built for cybersecurity learning, portfolio demonstration, and authorized network testing.

## Features

- Scan TCP ports across custom ranges
- Quick presets for top ports, web ports, database ports, remote-access ports, and full scan
- Full range support from 1 to 65535
- Clean dashboard-style UI
- Learning Hub with important ports and service descriptions
- Recent scan history
- Responsive design for desktop and mobile

## Project Structure

```bash
Web-Based-Port-Scanner-main/
├── app.py
├── scanner.py
├── learning_data.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   ├── learning.html
│   └── history.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── images/
```

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Run the Flask app

```bash
git clone <your-repo-url>
cd Web-Based-Port-Scanner-main
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Usage

- Open `http://127.0.0.1:5000`
- Enter a target IP address or domain
- Select a scan mode
- Review open ports and service mappings
- Explore the Learning Hub for important ports

## Important Note

This project is for educational and authorized security testing purposes only. Do not scan systems without permission.

## Future Improvements

- Export scan results as CSV or PDF
- Add database-backed persistent history
- Add service banners and risk scoring
- Add UDP scan simulation page
- Add authentication and user dashboards