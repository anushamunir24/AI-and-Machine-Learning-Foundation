# Project 1: Rule-Based AI Chatbot 🤖

This project implements a lightweight, deterministic conversation bot built using exact keyword-matching architectures and Python dictionaries. It focuses on executing reliable, predefined responses without the overhead of heavy language models.

## 🧠 Core Features & Logic
* **Deterministic Responses:** Uses a structured dictionary mapping specific user intents and keywords to custom bot responses.
* **String Preprocessing:** Implements `.lower()` and `.strip()` functions to clean up raw inputs, preventing matching failures caused by accidental trailing spaces or case differences.
* **Fallback Mechanism:** Includes an elegant default fallback reply (*"I don't understand, can you please say again?"*) utilizing a stateful console loop with a dedicated termination keyword (`exit`).

## 🛠️ Tech Stack
* **Language:** Python 🐍
* **Core Libraries:** Standard Library (built-in string functions, dictionaries)
