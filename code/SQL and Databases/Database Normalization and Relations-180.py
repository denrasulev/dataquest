## 4. Querying a normalized database ##

c = conn.cursor()
portman_movies = c.execute('\
SELECT ceremonies.year, nominations.movie FROM nominations \
INNER JOIN ceremonies \
ON nominations.ceremony_id == ceremonies.id \
WHERE nominations.nominee == "Natalie Portman";').fetchall()
print(portman_movies)

conn.close()

## 7. Join table ##

c = conn.cursor()

five_join_table = c.execute('SELECT * FROM movies_actors LIMIT 5;').fetchall()
five_actors = c.execute('SELECT * FROM actors LIMIT 5;').fetchall()
five_movies = c.execute('SELECT * FROM movies LIMIT 5;').fetchall()

print(five_join_table, "\n", five_actors, "\n", five_movies)

#conn.close()

## 9. Querying a many-to-many relation ##

c = conn.cursor()
kings_actors = c.execute('\
SELECT actors.actor, movies.movie FROM movies \
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id \
INNER JOIN actors ON movies_actors.actor_id == actors.id \
WHERE movies.movie == "The King\'s Speech";').fetchall()
print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

c = conn.cursor()
portman_joins = c.execute('\
SELECT movies.movie, actors.actor FROM movies \
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id \
INNER JOIN actors ON movies_actors.actor_id == actors.id \
WHERE actors.actor == "Natalie Portman";').fetchall()
print(portman_joins)