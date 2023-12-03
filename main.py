import feedparser
import sqlite3
from urllib.parse import urlparse, parse_qs
import subprocess
from sqlite3 import Error

# Parse the RSS feed
url = "https://freshrss.haijin666.top/i/?a=rss&user=youtube&token=youtube666&hours=168"
feed = feedparser.parse(url)

# SQLite database filename
db_file = "rss_feed.db"

# Create a connection to SQLite database
# If the database does not exist, it will be created
conn = None
try:
    conn = sqlite3.connect(db_file)
except Error as e:
    print(e)

# Create cursor object
cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS feed (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        link TEXT NOT NULL,
        vid TEXT,
        description TEXT,
        updated TEXT,
        author TEXT,
        published TEXT,
        downloaded TEXT DEFAULT 'false'
    )
""")

# Insert general feed information into the database
cur.execute("""
    INSERT INTO feed (title, link, description, updated)
    VALUES (?, ?, ?, ?)
""", (feed.feed.title, feed.feed.link, feed.feed.description, feed.feed.updated))

# Iterate through each item in the feed
for entry in feed.entries:
    # Insert each entry into the database
    cur.execute("""
        INSERT INTO feed (title, link, description, author, published)
        VALUES (?, ?, ?, ?, ?)
    """, (entry.title, entry.link, entry.description, entry.get("author", "N/A"), entry.published))

# Commit the changes
conn.commit()

# Query the database for entries where downloaded is not 'true'
cur.execute("SELECT link FROM feed WHERE downloaded != 'true'")
rows = cur.fetchall()

# Print the link of each entry that has not been downloaded
for row in rows:
    row = str(row)
    print(row)
    # Use urlparse to break down the URL into components
    parsed_url = urlparse(row)

    # Use parse_qs to turn the query string into a dictionary
    query_string_dict = parse_qs(parsed_url.query)

    # Extract the 'v' parameter from the dictionary
    v_param = query_string_dict.get('v', None)

    subprocess.run(['/root/yt-dlp_linux', row , '-P /r2/'+v_param+'.mp4'])

# Close the connection to the database
conn.close()
