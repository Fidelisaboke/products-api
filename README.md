# Products API
A simple products API created using the fastAPI web framework. It performs simple CRUD operations
using a dictionary.

## Installation Requirements
1. [Python 3](https://www.python.org/downloads/)
2. An IDE that supports Python

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/Fidelisaboke/products-api.git
cd products-api
```

2. Create a Python virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- on macOS/Linux:
```bash
source .venv/bin/activate
```
- on Windows:
```bash
.venv\Scripts\activate
```
4. Install the required packages
- on Linux/macOS:
```bash
pip install -r requirements.txt
```
- Some of the packages listed in `requirements.txt` may fail to install on Windows because the packages were installed in a Linux environment. For Windows, install `fastapi` afresh:
```bash
pip install "fastapi[standard]"
```

## Basic Usage
- Run the main.py file:
```bash
fastapi dev main.py
```
- Use the URL provided to access the API. You can use the`docs` URL to access the documentation.