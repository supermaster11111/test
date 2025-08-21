@echo off
py -3.11 -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements_311.txt
