# Project 3: AI Movie Recommendation Engine 

This project is part of the DecodeLabs AI Industrial Training. It features a professional content-based recommendation system that maps user preferences against a movie corpus using Natural Language Processing (NLP) and vector space modeling.

## 🧠 Core Features & AI Architecture
* **Text Feature Engineering:** Dynamically combines movie metadata (`genre` and `description`) into a unified text corpus for semantic feature analysis.
* **TF-IDF Vectorization:** Utilizes `TfidfVectorizer` to construct a high-dimensional term-document matrix. This mathematically weights distinct context terms while automatically penalizing ubiquitous, generic words (such as *the, to, in*).
* **Vector Space Modeling:** Appends the dynamic user string query to the movie matrix, dividing the transformed space into distinct `movie_vectors` and a singular `user_vector`.
* **Cosine Similarity Metric:** Employs `cosine_similarity` to calculate the exact dot product normalization (geometric angle) between user and item vectors, outputting continuous metrics ranging between $0.0$ (orthogonal/no match) and $1.0$ (identical mapping).
* **Dynamic Ranking Engine:** Filters out items with a score of $0$ and implements an optimized sort using lambda keys to dynamically position top recommendations at the apex of the console interface.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 🐍
* **Mathematical Operations:** NumPy
* **Machine Learning Pipeline:** Scikit-Learn (`TfidfVectorizer`, `cosine_similarity`)

## 🚀 How to Run the Script
1. Navigate to this `project3` folder.
2. Install the production dependencies:
   ```bash
   pip install scikit-learn numpy
