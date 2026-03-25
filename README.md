# ⚽ AI Football Scout System

An automated, AI-driven football scouting tool built with Python. This system extracts raw player statistics from external APIs, processes the data using Pandas, and leverages Google's Gemini Generative AI to automatically write professional scouting reports on young prospects.

## 🎯 The Problem it Solves
In modern football, data teams deal with massive amounts of raw statistics. Finding actionable insights manually is time-consuming. This project automates the data pipeline—from extraction to insight—acting as a virtual scout that filters noise and highlights potential talent based on hard data.

## 🛠️ Technologies & Tools
* **Python (OOP):** Core logic structured using Object-Oriented Programming for modularity and scalability.
* **Pandas:** Used for data manipulation, cleaning, and filtering (e.g., isolating U-24 players).
* **Requests:** Handling HTTP requests to the API-Sports REST API.
* **Google Gemini AI (genai):** Prompt engineering to generate natural language scouting reports from tabular data.
* **Git & GitHub:** Version control and repository management.

## ⚙️ Architecture
The system is built around the `ScoutCorinthians` class (easily adaptable to any team ID worldwide), which contains three main specialized methods:
1. `buscar_dados_api()`: Connects to the API and fetches raw JSON data.
2. `processar_dados_pandas()`: Converts JSON to a structured DataFrame and applies scouting filters.
3. `gerar_relatorio_ia()`: Compiles the filtered data into a prompt and calls the Gemini LLM to generate the final text report.

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/FGotz/scout-dados-futebol.git