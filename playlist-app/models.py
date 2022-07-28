"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, default="No description given")

    def __repr__(self):
        return f"<Playlist {self.id} {self.name} {self.description}>"


class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))

    playlists = db.relationship('Playlist', backref='songs')
    
    def __repr__(self):
        return f"<Song {self.id} {self.title} {self.artist}>"


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
