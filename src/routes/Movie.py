from flask import Blueprint, jsonify, request

#Models
from models.MovieModel import MovieModel

from models.entities.Movie import Movie


main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_movies():
    try:
        movies=MovieModel.get_movies()
        return jsonify(movies) 
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500


@main.route('/<id>')
def get_movie(id):
    try:
        movie=MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        print(request.json)
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']

        #print(title + duration + released)

        movie = Movie("", title, duration, released)
        affected_row = MovieModel.add_movie(movie)
        if affected_row == 1:
            return jsonify({'message' : 'add successfuly'})
        else:
            return jsonify({'message' : 'Error on insert'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500        