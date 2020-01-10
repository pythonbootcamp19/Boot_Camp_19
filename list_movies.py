movies_text = """
2018 The Equalizer 2 
Robert McCall
 2017 Roman J. Israel, Esq. 
Roman J. Israel, Esq.
 2016 Fences 
Troy Maxson
 2016 The Magnificent Seven 
Chisolm
 2014 The Equalizer 
Robert McCall
 2013 2 Guns 
Bobby
 2012/I Flight 
Whip Whitaker
 2012 Safe House 
Tobin Frost
 2010 Unstoppable 
Frank
 2010 The Book of Eli 
Eli
 2009 The Taking of Pelham 123 
Walter Garber
 2007 The Great Debaters 
Melvin B. Tolson
 2007 American Gangster 
Frank Lucas
 2006 Deja Vu 
Doug Carlin
 2006 Inside Man 
Detective Keith Frazier
 2004 The Manchurian Candidate 
Ben Marco
 2004 Man on Fire 
John W. Creasy
 2003/I Out of Time 
Matt Lee Whitlock
 2002 Antwone Fisher 
Dr. Jerome Davenport
 2002 John Q 
John Quincy Archibald
 2001 Training Day 
Alonzo
 2000 Remember the Titans 
Coach Herman Boone
 1999 The Hurricane 
Rubin Carter
 1999 The Bone Collector 
Lincoln Rhyme
 1998 The Siege 
Anthony Hubbard
 1998 He Got Game 
Jake Shuttlesworth
 1998 Fallen 
John Hobbes
"""

clean_movie_line_list = []

movies_test_splitted = movies_text.split("\n")
for movie_line in movies_test_splitted:
    if movie_line != '':
        clean_movie_line_list.append(movie_line.strip())
    else:
        pass

#print(clean_movie_line_list[::2])

list_len = len(clean_movie_line_list)

dict_of_movies = {}
for i in range(0,list_len,2):
    #print(i)
    year_movie_name = clean_movie_line_list[i]
    character_name = clean_movie_line_list[i+1]
    
   # print(year_movie_name, character_name)
    year = year_movie_name.split()[0]
    movie_name_splitted = year_movie_name.split()[1:]
    movie_name = " ".join(movie_name_splitted)

    #print(movie_name, character_name, year)
    movie_dict = {"movie_name": movie_name,
                "year": year,
                "character": character_name}
    dict_of_movies[movie_name] = movie_dict


print(dict_of_movies)