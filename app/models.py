import sqlalchemy.orm as orm
import sqlalchemy as sql 
import datetime
import uuid
import db
from . import choices

class Country(db.Base):
    # Table
    __tablename__ = "countries"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4))
    # Body
    title = sql.Column(sql.String(250), nullable=False)
    # Links
    movies = orm.relationship("Movie", back_populates="country", cascade="all, delete-orphan")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class User(db.Base):
    # Table
    __tablename__ = "users"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    tg_id = sql.Column(sql.BigInteger, unique=True, nullable=False)
    # Body
    username = sql.Column(sql.String(250), unique=True, nullable=False)
    name = sql.Column(sql.String(250), nullable=False)
    surname = sql.Column(sql.String(250), nullable=True)
    phone = sql.Column(sql.String(250), nullable=True)
    # Links
    reviews = orm.relationship("Review", back_populates="user", cascade="all, delete-orphan")
    profiles = orm.relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    # More
    is_superuser = sql.Column(sql.Boolean, default=False, nullable=True)
    is_staff = sql.Column(sql.Boolean, default=False, nullable=True)
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Director(db.Base):
    # Table
    __tablename__ = "directors"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    first_name = sql.Column(sql.String(250), nullable=False)
    last_name = sql.Column(sql.String(250), nullable=False)
    # Links 
    movie_directors = orm.relationship("MovieDirector", back_populates="director", cascade="all, delete-orphan")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Actor(db.Base):
    # Table
    __tablename__ = "actors"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    first_name = sql.Column(sql.String(250), nullable=False)
    last_name = sql.Column(sql.String(250), nullable=False)
    # Links
    movie_actors = orm.relationship("MovieActor", back_populates="actor", cascade="all, delete-orphan")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Genre(db.Base):
    # Table
    __tablename__ = "genres"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4())) 
    # Body
    title = sql.Column(sql.String(250), nullable=False)
    # Links
    movie_genres = orm.relationship("MovieGenre", back_populates="genre", cascade="all, delete-orphan")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Movie(db.Base):
    # Table
    __tablename__ = "movies"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    title = sql.Column(sql.String(250), nullable=False)
    short_description = sql.Column(sql.Text, nullable=False)
    description = sql.Column(sql.Text, nullable=False)
    video_path = sql.Column(sql.String(500), nullable=False)
    thumbnail_path = sql.Column(sql.String(500), nullable=False)
    rating = sql.Column(sql.Enum(choices.RatingChoice), default=choices.RatingChoice.UNRATED, nullable=False)
    country_uuid = sql.Column(sql.String(36), sql.ForeignKey('countries.uuid'), nullable=False)
    duration = sql.Column(sql.Float, default=0.0, nullable=False)
    url = sql.Column(sql.String(550), nullable=False)
    # Links
    reviews = orm.relationship("Review", back_populates="movie", cascade="all, delete-orphan")
    trailers = orm.relationship("Trailer", back_populates="movie", cascade="all, delete-orphan")
    country = orm.relationship("Country", back_populates="movies")
    movie_genres = orm.relationship("MovieGenre", back_populates="movie", cascade="all, delete-orphan")
    movie_directors = orm.relationship("MovieDirector", back_populates="movie", cascade="all, delete-orphan")
    movie_actors = orm.relationship("MovieActor", back_populates="movie", cascade="all, delete-orphan")
    # More
    released_at = sql.Column(sql.Date, nullable=False)
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class MovieGenre(db.Base):
    # Table
    __tablename__ = "movie_genres"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))   
    # Body
    movie_uuid = sql.Column(sql.String(36), sql.ForeignKey('movies.uuid'), nullable=False)
    genre_uuid = sql.Column(sql.String(36), sql.ForeignKey('genres.uuid'), nullable=False)
    # Links
    movie = orm.relationship("Movie", back_populates="movie_genres")
    genre = orm.relationship("Genre", back_populates="movie_genres")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class MovieDirector(db.Base):
    # Table
    __tablename__ = "movie_directors"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))   
    # Body
    movie_uuid = sql.Column(sql.String(36), sql.ForeignKey('movies.uuid'), nullable=False)
    director_uuid = sql.Column(sql.String(36), sql.ForeignKey('directors.uuid'), nullable=False)
    # Links
    movie = orm.relationship("Movie", back_populates="movie_directors")
    director = orm.relationship("Director", back_populates="movie_directors")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class MovieActor(db.Base):
    # Table
    __tablename__ = "movie_actors"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))   
    # Body
    movie_uuid = sql.Column(sql.String(36), sql.ForeignKey('movies.uuid'), nullable=False)
    actor_uuid = sql.Column(sql.String(36), sql.ForeignKey('actors.uuid'), nullable=False)
    # Links
    movie = orm.relationship("Movie", back_populates="movie_actors")
    actor = orm.relationship("Actor", back_populates="movie_actors")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Review(db.Base):
    # Table
    __tablename__ = "reviews"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    user_uuid = sql.Column(sql.String(36), sql.ForeignKey("users.uuid"), nullable=False)
    movie_uuid = sql.Column(sql.String(36), sql.ForeignKey('movies.uuid'), nullable=False)
    rating = rating = sql.Column(sql.Enum(choices.RatingChoice), default=choices.RatingChoice.UNRATED, nullable=False)
    comment = sql.Column(sql.Text, nullable=False)
    # Links
    user = orm.relationship("User", back_populates="reviews")
    movie = orm.relationship("Movie", back_populates="reviews")
    # More
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Trailer(db.Base):
     # Table
    __tablename__ = "trailers"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    movie_uuid = sql.Column(sql.String(36), sql.ForeignKey('movies.uuid'), nullable=False)
    title = sql.Column(sql.String(250), nullable=False)
    video_path = sql.Column(sql.String(500), nullable=False)
    description = sql.Column(sql.Text, nullable=False)
    likes = sql.Column(sql.BigInteger, default=0)
    comments = sql.Column(sql.BigInteger, default=0)
    url = sql.Column(sql.String(550), nullable=False)
    # Links
    movie = orm.relationship("Movie", back_populates="trailers")
    # More
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Profile(db.Base):
    # Table
    __tablename__ = "profiles"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    user_uuid = sql.Column(sql.String(36), sql.ForeignKey('users.uuid'), unique=True, nullable=False)
    # Links
    user = orm.relationship("User", back_populates="profiles")
    searches = orm.relationship("Search", back_populates="profile")
    # More
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)

class Search(db.Base):
    # Table
    __tablename__ = "searches"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    # Body
    profile_uuid = sql.Column(sql.String(36), sql.ForeignKey('profiles.uuid'), unique=True, nullable=False)
    # Links
    profile = orm.relationship("Profile", back_populates="searches")
    # More
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)