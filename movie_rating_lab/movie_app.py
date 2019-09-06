class Movie(object):

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title(self):
        return self.movie_data["title"]

    def get_movie_rating(self):
        return self.movie_data["rating"]

def return_single_movie_object(movie_title, movie_rating):
    return Movie({'title': movie_title, 'rating': movie_rating})        

def list_search_results(movie_titles):
    for title in movie_titles:
        print(f"     {title}")

def print_single_movie_rating(movie_query):
    movie_1 = return_single_movie_object(movie_query, 7)
    print('The rating for', movie_1.get_movie_title(), 'is', movie_1.get_movie_rating())

def print_all_ratings(movie_list):
    for movie in movie_list:
        movie_object = return_single_movie_object(movie, 4)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())


search_or_ratings = 1

def main():
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]
    print_all_ratings(default_movie_list)

    if search_or_ratings == 1:
        list_search_results(default_movie_list)
    elif search_or_ratings == 2:
        print_single_movie_rating("Moana")
    else:
        print("Error: Your input must be 1 or 2!")






# if search_or_ratings = 1:
#     movie_title = "Back to the Future"
# elif search_or_ratings = 2:

if __name__ == "__main__":
    main()