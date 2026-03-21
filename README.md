# 🛡️ Cloudflare Infrastructure OSINT Analysis

This project performs a **passive reconnaissance** analysis of Cloudflare's infrastructure, utilizing data collection tools and Python automation scripts for asset consolidation.

## 🚀 Technologies & Toolstack
* **Reconnaissance:** Sublist3r, WhatWeb, HTTPX.
* **Processing:** Python 3.x (Regex, OS).
* **Data Visualization:** CSVKit (csvlook).

## 📂 Project Structure
* `evidencia/`: Contains raw logs obtained from scanning tools.
* `scripts/`: Python scripts for data filtering and normalization (ETL).
* `reportes/`: Final CSV master report with unique identified assets.

## 🛠️ How to Run the Processor
To generate the master report from the collected evidence, execute:
```bash
python3 scripts/procesar_evidencia.py

---

## ⚠️ Disclaimer

**This project is for educational and passive auditing purposes only.**

No intrusion attacks, active scanning, or denial-of-service tests 
were performed against Cloudflare's infrastructure. 

The author (Sic4ri0) is not responsible for any misuse 
of this information or the tools provided in this repository. 

Always ensure you have explicit permission before 
conducting any security assessment.
