#!/usr/bin/sh

echo "[+] Installing Requirements.."

pip3 install tkintertable
echo "[+] tkintertable installed successfully.."
echo "[+] Starting gui.."

sleep 2
sudo python3 macchanger-gui.py
