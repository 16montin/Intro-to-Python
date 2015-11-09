'''IMDB has "common cast/crew between two titles" and "two people working
together" search facilities: http://www.imdb.com/search/common . In this
assignment, you will write your own versions. The design of your program
is up to you. The only requirement is that you have store the movie
information in a dictionary.'''


'''Input the database file'''

def get_input():
    input_file = input('Enter File Input: ')
    with open(input_file, 'r') as file: #to read the file
        file_lines = file.read().splitlines() #sorts the file into lines
    new_file = tuple(file_lines) #makes file into a tuple
    return new_file

'''Take the information from the input file above and turn it into a
dictionary.'''

def create_dictionary():
    movie_dictionary = {} #will give us movies as dict values
    actor_dictionary = {} #will give us actors as dict values
    file_content = get_input() #to get input text
    for content in file_content:
        line = content.split(',') #break up all the values
        actors = line.pop(0) #split the actor values from the movie values
        movies = [] #empty list to append movies to
        for movie in line:
            movie = movie.lstrip() #get rid of leading whitespace
            movies.append(movie) #put movies in empty movie list
            if actor_dictionary.get(movie, False) == False:
                actor_dictionary[movie] = []
            actor_dictionary[movie].append(actors) #append the actors
        movie_dictionary[actors] = movies #set the key, value paris
    return movie_dictionary, actor_dictionary #to access dictionaries later

'''List and print of the actors (names) in the database by pulling them
from the dictionary.'''

def all_actors(current_dictionary):
    print ('**All actors in the database: ')
    my_sorted_dict = sorted(current_dictionary) #sorts the actors
    for actors in my_sorted_dict:
        print('  ' + actors) #to get indent and actor values
    print('')
    return

'''List and print all of the movies (keys) in the database.'''

def all_movies(current_dictionary):
    print ('**All movies in the database: ')
    my_sorted_dict = sorted(current_dictionary) #sorts the movies
    for movies in my_sorted_dict:
        print('  ' + movies) #to get indent and movie values
    print('')
    return
     
'''Get a list of all the movies separate of the actors'''

def actor_combinations(movie_dictionary):
    combinations = list() #set combinations as empty list
    for i in range(0,len(movie_dictionary)):
        for j in range(i+1,len(movie_dictionary)):
            combinations.append([movie_dictionary[i],movie_dictionary[j]])
    return combinations #to get all possible movie combinations

'''For any pair of actors, list the movie or movies they are both in
together.'''

def appeared_with(movie_dictionary, actor_dictionary):
    print('**These actor pairs have appeared together: ')
    pairs_of_actors = actor_combinations(sorted(list(movie_dictionary.keys())))
    for actor_pairs in pairs_of_actors:
        actors_in_movie = [] #set the empty list
        for movie_key in actor_dictionary.keys():
            if actor_pairs[0] in actor_dictionary[movie_key] and \
               actor_pairs[1] in actor_dictionary[movie_key]:
                actors_in_movie.append(movie_key) #append unique movies to list
        if len(actors_in_movie) > 0: #so it doesn't print empty values
            print('  ' + actor_pairs[0] + ' and ' + actor_pairs[1] + \
                  ' both appeared in \n    ' + '\n    '.join (sorted\
                                                      (actors_in_movie)))
    print('')        
    return

'''For any set of two movies, find the actor or actors that appear(s) in
both.'''

def actors_in_common(movie_dictionary, actor_dictionary):
    print('**These movie pairs share cast members: ')
    pairs_of_movies = actor_combinations(sorted(list(actor_dictionary.keys())))
    for movie_pairs in pairs_of_movies:
        common_actors = [] #set the empty list
        for actor_key in movie_dictionary.keys():
            if movie_pairs[0] in movie_dictionary[actor_key] and \
               movie_pairs[1] in movie_dictionary[actor_key]:
                common_actors.append(actor_key) #add unique actors to the list
        if len(common_actors) > 2:
            common_actors = sorted(common_actors)
            last_common_actor = common_actors.pop()
            print('  ' + movie_pairs[0] + ' & ' + movie_pairs[1] + ':\n    '+ \
                  ', '.join(common_actors) + ', and ' + last_common_actor \
                  +' were all in them')
        elif len(common_actors) > 1:
            common_actors = sorted(common_actors) #to put them in order
            second_common_actor = common_actors.pop() #remove last actor
            print('  ' + movie_pairs[0] + ' & ' + movie_pairs[1] + \
                  ':\n    ' + ''.join(common_actors) + ' and ' + \
                  second_common_actor + ' were both in them')
        elif len(common_actors) >  0:
            print('  ' + movie_pairs[0] + ' & ' + movie_pairs[1] + \
                  ':\n    ' + ''.join(sorted(common_actors)) + ' was in them')
        #this outer if statement is to print each possible outcome
    print('')
    return

'''Find every instance that each actor shares a movie with another actor
and create a list of every actor who has worked with the actor they are
being matched to.'''

def worked_with(movie_dictionary, actor_dictionary):
    print('**Who has each actor worked with?')
    for actor_key in sorted(movie_dictionary.keys()):
        actors_worked_with = [] #blank list to append values to
        for movie_key in actor_dictionary.keys():
            if actor_key in actor_dictionary[movie_key]:
                for actor in actor_dictionary[movie_key]:
                    if not actor_key == actor:
                        actors_worked_with.append(actor) #appends the actors
        sorted_list = sorted(list(set(actors_worked_with))) #makes it a list
        last_movie = sorted_list.pop() #splits last movie from sorted_list
        print('  ' + actor_key, 'has appeared with ' +', '.join(sorted_list) \
              +', and' , last_movie) #all this mess prints the results
    print('')
    return

'''Call all of the functions above in the proper order so that
they match the output files.'''

def main():
    movie_dictionary, actor_dictionary = create_dictionary() #for dictionaries
    all_actors(movie_dictionary) #calls all_actors function
    all_movies(actor_dictionary) #calls all_movies function
    appeared_with(movie_dictionary, actor_dictionary) #calls appeared_with
    actors_in_common(movie_dictionary, actor_dictionary) #calls actors_in_common
    worked_with(movie_dictionary, actor_dictionary) #calls worked_with
    return

main() #calls the main function, runs program
