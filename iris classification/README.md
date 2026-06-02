# Project 2: Iris Flower Classification (Machine Learning) 🌸

This project demonstrates a complete Machine Learning workflow to classify Iris flower species based on their sepal and petal measurements using the K-Nearest Neighbors (KNN) algorithm.

## 🧠 Core Features & ML Pipeline
* **Dataset Utilization:** Uses the classic **Iris Dataset** from `sklearn.datasets`, featuring 150 samples across 3 distinct classes (*Setosa, Versicolor, and Virginica*).
* **Data Splitting:** Implements a robust 80-20 Train-Test split (`train_test_split`) with active shuffling to ensure unbiased model evaluation.
* **Feature Scaling:** Utilizes `StandardScaler` to perform Z-score normalization on the training and testing features, preventing attributes with larger scales from dominating the distance calculations.
* **KNN Algorithm:** Implements the `KNeighborsClassifier` configured with $K=5$ neighbors to classify the test data based on distance metrics.
* **Comprehensive Evaluation:** Measures model performance using **Weighted F1-Score**, a **Confusion Matrix** to track misclassifications, and a detailed **Classification Report** (Precision, Recall).

## 🛠️ Tech Stack & Libraries
* **Language:** Python 🐍
* **Data Manipulation:** NumPy, Pandas
* **Machine Learning Framework:** Scikit-Learn (sklearn)
