import json
from typing import List, Dict, Optional
import random

class MovieRecommender:
    def __init__(self):
        # Sample movie database with genres
        self.movies = [
            {"title": "The Shawshank Redemption", "genres": ["Drama"], "rating": 9.3, "year": 1994},
            {"title": "The Godfather", "genres": ["Crime", "Drama"], "rating": 9.2, "year": 1972},
            {"title": "Pulp Fiction", "genres": ["Crime", "Drama"], "rating": 8.9, "year": 1994},
            {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"], "rating": 9.0, "year": 2008},
            {"title": "Fight Club", "genres": ["Drama"], "rating": 8.8, "year": 1999},
            {"title": "Inception", "genres": ["Action", "Adventure", "Sci-Fi"], "rating": 8.8, "year": 2010},
            {"title": "The Matrix", "genres": ["Action", "Sci-Fi"], "rating": 8.7, "year": 1999},
            {"title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"], "rating": 8.6, "year": 2014},
            {"title": "The Lion King", "genres": ["Animation", "Adventure", "Drama"], "rating": 8.5, "year": 1994},
            {"title": "Titanic", "genres": ["Drama", "Romance"], "rating": 7.9, "year": 1997},
            {"title": "La La Land", "genres": ["Comedy", "Drama", "Musical"], "rating": 8.0, "year": 2016},
            {"title": "Get Out", "genres": ["Horror", "Mystery", "Thriller"], "rating": 7.7, "year": 2017},
            {"title": "The Grand Budapest Hotel", "genres": ["Comedy", "Drama"], "rating": 8.1, "year": 2014},
            {"title": "Mad Max: Fury Road", "genres": ["Action", "Adventure", "Sci-Fi"], "rating": 8.1, "year": 2015},
            {"title": "The Martian", "genres": ["Adventure", "Drama", "Sci-Fi"], "rating": 8.0, "year": 2015}
        ]
        
        # Few-shot examples for genre matching
        self.few_shot_examples = {
            "Drama": [
                "User likes emotional storytelling and character development",
                "Recommend: The Shawshank Redemption, The Godfather, Fight Club"
            ],
            "Action": [
                "User enjoys fast-paced sequences and thrilling scenes",
                "Recommend: The Dark Knight, The Matrix, Mad Max: Fury Road"
            ],
            "Sci-Fi": [
                "User is interested in futuristic concepts and technology",
                "Recommend: Inception, The Matrix, Interstellar"
            ],
            "Comedy": [
                "User prefers light-hearted and humorous content",
                "Recommend: La La Land, The Grand Budapest Hotel"
            ],
            "Horror": [
                "User enjoys suspenseful and scary content",
                "Recommend: Get Out"
            ]
        }
    
    def get_genre_recommendations(self, preferred_genre: str, num_recommendations: int = 3) -> List[Dict]:
        """
        Recommend movies based on user's preferred genre using few-shot prompting approach.
        
        Args:
            preferred_genre (str): The genre the user prefers
            num_recommendations (int): Number of movies to recommend
            
        Returns:
            List[Dict]: List of recommended movies with their details
        """
        # Convert to title case for better matching
        preferred_genre = preferred_genre.title()
        
        # Get few-shot context for the genre
        genre_context = self.few_shot_examples.get(preferred_genre, [])
        
        # Find movies that match the preferred genre
        matching_movies = []
        for movie in self.movies:
            if preferred_genre in [genre.title() for genre in movie["genres"]]:
                matching_movies.append(movie)
        
        # Sort by rating (highest first) and then by year (newest first)
        matching_movies.sort(key=lambda x: (x["rating"], x["year"]), reverse=True)
        
        # Apply few-shot learning logic
        if genre_context:
            # Use few-shot examples to enhance recommendations
            enhanced_movies = self._apply_few_shot_learning(matching_movies, preferred_genre, genre_context)
            recommendations = enhanced_movies[:num_recommendations]
        else:
            # Fallback to standard recommendations
            recommendations = matching_movies[:num_recommendations]
        
        return recommendations
    
    def _apply_few_shot_learning(self, movies: List[Dict], genre: str, context: List[str]) -> List[Dict]:
        """
        Apply few-shot learning to enhance movie recommendations.
        
        Args:
            movies (List[Dict]): List of movies matching the genre
            genre (str): The preferred genre
            context (List[str]): Few-shot examples for the genre
            
        Returns:
            List[Dict]: Enhanced list of movies
        """
        enhanced_movies = movies.copy()
        
        # Apply genre-specific logic based on few-shot examples
        if genre == "Drama":
            # Drama movies: prioritize emotional depth and character development
            enhanced_movies.sort(key=lambda x: (x["rating"], len(x["genres"]) == 1, x["year"]), reverse=True)
        elif genre == "Action":
            # Action movies: prioritize high energy and visual appeal
            enhanced_movies.sort(key=lambda x: (x["rating"], "Adventure" in x["genres"], x["year"]), reverse=True)
        elif genre == "Sci-Fi":
            # Sci-Fi movies: prioritize innovative concepts and modern effects
            enhanced_movies.sort(key=lambda x: (x["rating"], x["year"], "Action" in x["genres"]), reverse=True)
        elif genre == "Comedy":
            # Comedy movies: prioritize humor and entertainment value
            enhanced_movies.sort(key=lambda x: (x["rating"], "Musical" in x["genres"], x["year"]), reverse=True)
        elif genre == "Horror":
            # Horror movies: prioritize suspense and psychological elements
            enhanced_movies.sort(key=lambda x: (x["rating"], "Mystery" in x["genres"], x["year"]), reverse=True)
        
        return enhanced_movies
    
    def get_multi_genre_recommendations(self, preferred_genres: List[str], num_recommendations: int = 5) -> List[Dict]:
        """
        Recommend movies based on multiple preferred genres.
        
        Args:
            preferred_genres (List[str]): List of genres the user prefers
            num_recommendations (int): Number of movies to recommend
            
        Returns:
            List[Dict]: List of recommended movies
        """
        # Find movies that match any of the preferred genres
        matching_movies = []
        for movie in self.movies:
            movie_genres = [genre.title() for genre in movie["genres"]]
            if any(genre.title() in movie_genres for genre in preferred_genres):
                # Calculate genre match score
                match_score = sum(1 for genre in preferred_genres if genre.title() in movie_genres)
                movie["genre_match_score"] = match_score
                matching_movies.append(movie)
        
        # Sort by genre match score, then by rating, then by year
        matching_movies.sort(key=lambda x: (x["genre_match_score"], x["rating"], x["year"]), reverse=True)
        
        # Remove the temporary score field
        for movie in matching_movies:
            movie.pop("genre_match_score", None)
        
        return matching_movies[:num_recommendations]
    
    def get_personalized_recommendations(self, user_preferences: Dict[str, float], num_recommendations: int = 5) -> List[Dict]:
        """
        Get personalized recommendations based on user genre preferences with weights.
        
        Args:
            user_preferences (Dict[str, float]): Dictionary mapping genres to preference weights (0.0 to 1.0)
            num_recommendations (int): Number of movies to recommend
            
        Returns:
            List[Dict]: List of recommended movies
        """
        scored_movies = []
        
        for movie in self.movies:
            total_score = 0.0
            for genre, weight in user_preferences.items():
                if genre.title() in [g.title() for g in movie["genres"]]:
                    total_score += weight
            
            if total_score > 0:
                # Normalize score by number of genres and add rating bonus
                normalized_score = (total_score / len(movie["genres"])) + (movie["rating"] / 10.0)
                movie_copy = movie.copy()
                movie_copy["personalized_score"] = normalized_score
                scored_movies.append(movie_copy)
        
        # Sort by personalized score
        scored_movies.sort(key=lambda x: x["personalized_score"], reverse=True)
        
        # Remove the temporary score field
        for movie in scored_movies:
            movie.pop("personalized_score", None)
        
        return scored_movies[:num_recommendations]
    
    def display_recommendations(self, recommendations: List[Dict], genre: str = None):
        """
        Display movie recommendations in a formatted way.
        
        Args:
            recommendations (List[Dict]): List of recommended movies
            genre (str): The genre used for recommendations
        """
        if not recommendations:
            print(f"No movies found for genre: {genre}")
            return
        
        print(f"\n🎬 Movie Recommendations for {genre or 'your preferences'}:")
        print("=" * 60)
        
        for i, movie in enumerate(recommendations, 1):
            genres_str = ", ".join(movie["genres"])
            print(f"{i}. {movie['title']} ({movie['year']})")
            print(f"   Genres: {genres_str}")
            print(f"   Rating: ⭐ {movie['rating']}/10")
            print()


def main():
    """Main function to demonstrate the movie recommendation system."""
    recommender = MovieRecommender()
    
    print("🎭 Movie Recommendation System with Few-Shot Learning")
    print("=" * 60)
    
    # Example 1: Single genre recommendation
    print("\n1️⃣ Single Genre Recommendation:")
    drama_movies = recommender.get_genre_recommendations("Drama", 3)
    recommender.display_recommendations(drama_movies, "Drama")
    
    # Example 2: Multi-genre recommendation
    print("\n2️⃣ Multi-Genre Recommendation:")
    action_sci_fi = recommender.get_multi_genre_recommendations(["Action", "Sci-Fi"], 4)
    recommender.display_recommendations(action_sci_fi, "Action & Sci-Fi")
    
    # Example 3: Personalized recommendation
    print("\n3️⃣ Personalized Recommendation:")
    user_prefs = {"Drama": 0.8, "Comedy": 0.6, "Romance": 0.4}
    personalized = recommender.get_personalized_recommendations(user_prefs, 4)
    recommender.display_recommendations(personalized, "Personalized")
    
    # Interactive demo
    print("\n🎯 Interactive Demo:")
    print("Enter a genre to get recommendations (or 'quit' to exit):")
    
    while True:
        user_input = input("\nEnter genre: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thanks for using the Movie Recommendation System! 🎬")
            break
        
        if user_input:
            recommendations = recommender.get_genre_recommendations(user_input, 5)
            recommender.display_recommendations(recommendations, user_input)
        else:
            print("Please enter a valid genre.")


if __name__ == "__main__":
    main()
