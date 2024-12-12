import sqlalchemy.orm as orm
import sqlalchemy as sql 
import datetime
import uuid
import db
import enum

class Country(db.Base):
    # Table
    __tablename__ = "countries"
    # ID's
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    uuid = sql.Column(sql.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4))
    # Body
    title = sql.Column(sql.String(250), nullable=False)
    # Links
    movie = orm.relationship("Movie", back_populates="country", cascade="all, delete-orphan")
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
    tg_id = sql.Column(sql.Integer, unique=True, nullable=False)
    # Body
    username = sql.Column(sql.String(250), unique=True, nullable=False)
    first_name = sql.Column(sql.String(250), nullable=False)
    last_name = sql.Column(sql.String(250), nullable=True)
    phone = sql.Column(sql.String(250), nullable=True)
    # Links
    profile = orm.relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")
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
    movie_director = orm.relationship("MovieDirector", back_populates="director", cascade="all, delete-orphan")
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
    movie_actor = orm.relationship("MovieActor", back_populates="actor", cascade="all, delete-orphan")
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
    movie_genre = orm.relationship("MovieGenre", back_populates="genre", cascade="all, delete-orphan")
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
    # Choices
    class RatingChoice(enum.Enum):
        UNRATED = 0.0
        TERRIBLE = 0.5
        BAD = 1.0
        DULL = 1.5
        BORING = 2
        FINE = 2.5
        AVERAGE = 3
        GOOD = 3.5
        EXCELLENT = 4
        AMAZING = 4.5
        PERFECT = 5.0
    # Body
    title = sql.Column(sql.String(250), nullable=False)
    short_description = sql.Column(sql.Text, nullable=False)
    description = sql.Column(sql.Text, nullable=False)
    video_path = sql.Column(sql.String(500), nullable=False)
    thumbnail_path = sql.Column(sql.String(500), nullable=False)
    rating = sql.Column(sql.Enum(RatingChoice), default=RatingChoice.UNRATED, nullable=False)
    country_uuid = sql.Column(sql.String(36), sql.ForeignKey('countries.uuid'), nullable=False)
    duration = sql.Column(sql.Float, default=0.0, nullable=False)
    # Links
    trailer = orm.relationship("Trailer", back_populates="movie", cascade="all, delete-orphan")
    country = orm.relationship("Country", back_populates="movie")
    movie_genre = orm.relationship("MovieGenre", back_populates="movie", cascade="all, delete-orphan")
    movie_director = orm.relationship("MovieDirector", back_populates="movie", cascade="all, delete-orphan")
    movie_actor = orm.relationship("MovieActor", back_populates="movie", cascade="all, delete-orphan")
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
    movie = orm.relationship("Movie", back_populates="movie_genre")
    genre = orm.relationship("Genre", back_populates="movie_genre")
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
    movie = orm.relationship("Movie", back_populates="movie_director")
    director = orm.relationship("Director", back_populates="movie_director")
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
    movie = orm.relationship("Movie", back_populates="movie_actor")
    actor = orm.relationship("Actor", back_populates="movie_actor")
    # More
    is_active = sql.Column(sql.Boolean, default=True, nullable=True)
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
    # Links
    movie = orm.relationship("Movie", back_populates="trailer")
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
    user = orm.relationship("User", back_populates="profile")
    search = orm.relationship("Search", back_populates="profile")
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
    profile = orm.relationship("Profile", back_populates="search")
    # More
    updated_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = sql.Column(sql.DateTime, default=datetime.datetime.utcnow)