void main() {
  Movie interstellar = Movie("Interstellar", 169);
  Movie tenet = Movie("Tenet", 150, movie_watched: true, movie_review: 10);
  Series breaking_bad = Series("Breaking Bad");
  Series better_call_saul = Series("Better Call Saul", series_watched: true);
  print(interstellar);
  print(tenet);

  Episode bb_ep1 = Episode("BB Episode 1", 48);
  Episode bb_ep2 = Episode("BB Episode 2", 45, episode_watched: true, episode_review: 8);
  Episode bcs_ep1 = Episode("BCS Episode 1", 60);
  Episode bcs_ep2 = Episode("BCS Episode 2", 46, episode_watched: true, episode_review: 9);

  breaking_bad.addEpisode(bb_ep1);
  breaking_bad.addEpisode(bb_ep2);
  better_call_saul.addEpisode(bcs_ep1);
  better_call_saul.addEpisode(bcs_ep2);
  print(breaking_bad);
  print(better_call_saul);

  Collection my_collection = Collection();
  my_collection.addMovie(interstellar);
  my_collection.addMovie(tenet);
  my_collection.addSeries(breaking_bad);
  my_collection.addSeries(better_call_saul);
  print(my_collection);
}


class Collection {
  List<Movie> _movie_list = [];
  List<Series> _series_list = [];

  int get total_movies => _movie_list.length;
  int get total_series => _series_list.length;
  List get movies_list => _movie_list;
  List get series_list => _series_list;

  void addMovie(Movie movie) {
    _movie_list.add(movie);
  }

  void addSeries(Series series) {
    _series_list.add(series);
  }

  void removeMovie(Movie movie) {
    _movie_list.remove(movie);
  }

  void removeSeries(Series series) {
    _series_list.remove(series);
  }

  String toString() {
    String output = "Collection contains $total_movies movies and $total_series series.\n";
    output += "Movies: $movies_list \nSeries: $series_list";
    return output;
  }

}


class Movie {
  String movie_name;
  int movie_length;
  bool movie_watched;
  int? movie_review;

  Movie(this.movie_name, this.movie_length, {this.movie_watched = false, this.movie_review});

  void setWatched() {
    if (movie_watched == false) {
      movie_watched = true;
    } else {
      movie_watched = false;
    }
  }

  void leaveReview(int score) {
    if (score <= 10) {
      movie_review = score;
    } else {
      print("Score must be from 0-10.");
    }
  }

  String toString() {
    String output = "Movie($movie_name, $movie_length minutes, watched: $movie_watched, score: $movie_review)";
    return output;
  }
}


class Series {
  String series_name;
  bool series_watched;
  int? series_review;
  List<Episode> episode_list = [];

  Series(this.series_name, {this.series_watched = false, this.series_review});

  int get series_length => episode_list.length;

  void setWatched() {
    if (series_watched == false) {
      series_watched = true;
    } else {
      series_watched = false;
    }
  }

  void leaveReview(score) {
    if (score <= 10) {
      series_review = score;
    } else {
      print("Score must be from 0-10.");
    }
  }

  void addEpisode(episode) => episode_list.add(episode);
  void removeEpisode(episode) => episode_list.remove(episode);

  String toString() {
    String output = "Series($series_name, $series_length episodes, watched: $series_watched, score: $series_review)\n";
    output += "Episodes:\n $episode_list";
    return output;
  }
}


class Episode {
  String episode_name;
  int episode_length;
  bool episode_watched;
  int? episode_review;

  Episode(this.episode_name, this.episode_length, {this.episode_watched = false, this.episode_review});

  void setWatched() {
    if (episode_watched == false) {
      episode_watched = true;
    } else {
      episode_watched = false;
    }
  }

  void leaveReview(score) {
    if (score <= 10) {
      episode_review = score;
    } else {
      print("Score must be from 0-10.");
    }
  }

  String toString() {
    String output = "Episode($episode_name, $episode_length minutes, watched: $episode_watched, score: $episode_review)";
    return output;
  }
}