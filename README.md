# Links Bio Rafnix Guzmán

## Installation

```bash
git clone https://github.com/rafnixg/links.git
cd links
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
reflex run
```

## Export

```bash
reflex export
```

## Production
    
```bash
reflex run --env prod
```

## Using Docker

```bash
docker build -t reflex-links:latest .
docker run -it --rm -p 8000:8000 -p 3000:3000 --name links reflex-links:latest
```