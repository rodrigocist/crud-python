from databse.db import get_connection
from .entities.Movie import Movie


class MovieModel():
    SELECT_SQL="select id, title, duration, released from movies order by title asc"


    @classmethod
    def get_movies(self):
        try:
            connection=get_connection()
            movies=[]

            with connection.cursor() as cursor:
                cursor.execute("select id, title, duration, released from movies order by title asc")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    print("movie: " + row[1])
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())

            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_movie(self, id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("select id, title, duration, released from movies where id = %s", (id,))
                row=cursor.fetchone()
                #print("row: id " + id)
                movie = None
                if row != None:
                    print("movie: " + row[1])
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movie = movie.to_JSON()

            connection.close()
            return movie
        except Exception as ex:
            print ("Error add: " + ex)
            raise Exception(ex)



    @classmethod
    def add_movie(self, movie):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""insert into movies(title, duration, released) 
                            values (%s, %s, %s)""",(movie.title, movie.duration, movie.released))
                
                affected_row=cursor.rowcount
                print("affected_row:  " +str(affected_row))
                connection.commit()

            connection.close()
            return affected_row
        except Exception as ex:
            print ("Error add: " , ex)
            raise Exception(ex)            