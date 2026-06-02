import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_db = [
    {"title": "Inception", "genre": "Sci-Fi Thriller Action", "description": "Dreams within dreams and mind-bending action"},
    {"title": "Interstellar", "genre": "Sci-Fi Drama Space", "description": "Space exploration and human emotions across dimensions"},
    {"title": "The Dark Knight", "genre": "Action Crime Thriller", "description": "Batman fights joker to save Gotham city"},
    {"title": "The Notebook", "genre": "Romance Drama", "description": "A classic love story that lasts a lifetime"},
    {"title": "The Hangover", "genre": "Comedy", "description": "A crazy bachelor party in Las Vegas goes wrong"},
    {"title": "Avengers: Endgame", "genre": "Action Sci-Fi Superhero", "description": "Superheroes team up to save the universe"}
]
movie_texts = [movie["genre"] + " " + movie["description"] for movie in movies_db]
print("Welcome to the AI recommendation engine!")

while True:
    print("\n[Options: Type your favourite genre or type 'exit' to quit]")
    user_input = input("Please enter a movie title or genre you like: ").strip().lower()
    
    if user_input == 'exit':
        print("\nThank you for using DecodeLabs Recommendation Engine.")
        break  
        
    if not user_input:
        print("Please enter something so we recommend you!")
        continue
    vectorizer = TfidfVectorizer()
    all_texts = movie_texts + [user_input]
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    movie_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]

    similarity_scores = cosine_similarity(user_vector, movie_vectors).flatten()

    recommendations = []
    for index, score in enumerate(similarity_scores):
        if score > 0:
            recommendations.append({
                "title": movies_db[index]["title"],
                "genre": movies_db[index]["genre"],
                "score": score
            })

    recommendation = sorted(recommendations, key=lambda x: x['score'], reverse=True)
    
    print("\nRecommended movies based on your input:")
    if len(recommendation) == 0:
        print("No recommendations found. Please try a different input.")
    else:
        for index, movie in enumerate(recommendation, start=1):
            print(f"{index}. {movie['title']} - Genre: {movie['genre']} (Score: {movie['score']})")
            
    print("-" * 50) 