# Project 1: Rule-Based AI Chatbot 🤖

This project is part of the DecodeLabs AI Industrial Training. It focuses on building core programming logic, conditional conversation flows, and handling basic user queries using string manipulation.

## 🧠 Core Features & Logic
* **Deterministic Responses:** Uses a pre-defined dictionary mapping specific user intents and keywords to custom bot responses.
* **String Preprocessing:** Implements `.lower()` and `.strip()` functions to clean up raw inputs, preventing matching failures caused by accidental trailing spaces or case differences.
* **Fallback Mechanism:** Includes an elegant default fallback reply (*"I don't understand, can you please say again?"*) utilizing Python's `.get()` dictionary method when no predefined rule is triggered.
* **Continuous Conversation Loop:** Features an interactive `while True` console loop with a dedicated termination keyword (`exit`).

## 💻 Tech Stack
* **Language:** Python 🐍
* **Data Structure:** Python Dictionaries (for intent mapping)

## 🚀 How to Run the Script
1. Clone the repository or navigate to this folder.
2. Run the script using terminal:
   ```bash
   python project1.py
