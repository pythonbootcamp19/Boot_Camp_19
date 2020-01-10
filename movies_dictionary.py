movie_name = input("Enter Movie Name: ")
year = int(input("Year of Release: "))
actors = input("Enter Actor Name: ")
rating = float(input("Enter Rating: "))
    
movies = {}

movies[movie_name] = {"Year": year, "Actors": actors, "Rating": rating}

movies_year = movies[movie_name]

print(movies)

print(movies_year)