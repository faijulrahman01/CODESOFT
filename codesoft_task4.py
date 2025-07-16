import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = {
    'title': ['The Matrix', 'John Wick', 'Avengers', 'The Notebook', 'Inception', 'Interstellar'],
    'description': [
        'A hacker discovers the world is a simulation',
        'An ex-hitman seeks revenge',
        'Superheroes team up to save the world',
        'A romantic love story',
        'Dreams within dreams in sci-fi world',
        'Astronauts travel through wormholes to save humanity'
    ]
}

df = pd.DataFrame(data)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def recommend(title, num_recommendations=3):
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

class RecommenderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🎬 Movie Recommendation System")
        self.master.geometry("500x400")
        self.master.config(bg="#f0f0f0")

        tk.Label(master, text="Select a movie:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

        self.movie_combo = ttk.Combobox(master, values=df['title'].tolist(), font=("Arial", 12), width=40, state="readonly")
        self.movie_combo.pack(pady=5)
        self.movie_combo.set("Inception")

        self.recommend_button = tk.Button(master, text="Get Recommendations", font=("Arial", 12, "bold"),
                                          bg="#007bff", fg="white", command=self.show_recommendations)
        self.recommend_button.pack(pady=15)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="#f0f0f0", justify="left")
        self.result_label.pack(pady=20)

    def show_recommendations(self):
        selected_movie = self.movie_combo.get()
        recommendations = recommend(selected_movie)
        if recommendations:
            result_text = "\n".join(f"• {movie}" for movie in recommendations)
        else:
            result_text = "No recommendations found."
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecommenderGUI(root)
    root.mainloop()