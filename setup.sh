#!/usr/bin/env bash
set -e
echo "[setup] creating venv..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
echo "[setup] installing python deps..."
pip install -r requirements.txt
echo "[setup] installing hardhat deps..."
(cd blockchain/hardhat && npm install)
cp .env.template .env || true
echo "[setup] done. Use 'make start' to run docker-compose"
