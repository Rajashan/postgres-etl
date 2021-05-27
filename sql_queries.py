# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay 
(
    songplay_id serial PRIMARY KEY, 
    start_time timestamp REFERENCES time(start_time), 
    user_id int NOT NULL REFERENCES users(user_id), 
    level text, 
    song_id text REFERENCES song(song_id), 
    artist_id text REFERENCES artist(artist_id), 
    session_id int, 
    location text, 
    user_agent text
    );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(
    user_id int PRIMARY KEY,
    first_name text,
    last_name text,
    gender text CHECK (gender IN ('M','F', null)), 
    level text CHECK (level IN ('paid', 'free'))
    );
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song 
(
    song_id text PRIMARY KEY, 
    title text, 
    artist_id text, 
    year int, 
    duration numeric
    );
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist 
(
    artist_id text PRIMARY KEY, 
    name text, 
    location text, 
    latitude numeric, 
    longitude numeric
    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time 
(
    start_time timestamp PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday text
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay

(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

VALUES 

(%s, %s, %s, %s, %s, %s, %s, %s, %s)

ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users

(user_id, first_name, last_name, gender, level)

VALUES

(%s, %s, %s, %s, %s)

ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO song 

(song_id, title, artist_id, year, duration)

VALUES

(%s, %s, %s, %s, %s)

ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artist

(artist_id, name, location, latitude, longitude)

VALUES

(%s, %s, %s, %s, %s)

ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time

(start_time, hour, day, week, month, year, weekday)

VALUES

(%s, %s, %s, %s, %s, %s, %s)

ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, artist.artist_id FROM song JOIN artist ON song.artist_id=artist.artist_id WHERE song.title=%s AND artist.name=%s AND song.duration=%s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]