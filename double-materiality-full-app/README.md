# Double Materiality Measurement App

Questo repository contiene l'applicazione Python per misurare la **doppia materialità** secondo quattro fasi:
1. Document Collection
2. Double Materiality Analysis
3. KPI Standards Selection
4. Automation of Reporting

## Setup

```bash
git clone https://github.com/Stevolto/double-materiality-full-app.git
cd double-materiality-full-app
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run locally

```bash
flask run --host=0.0.0.0 --port=5000
```

## Testing

```bash
pytest
```

## Deployment

Build command: `pip install -r requirements.txt`

Start command: `gunicorn app:app`
