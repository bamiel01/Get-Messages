import sqlite3
import csv



def is_valid_utf8(s):
    try:
        s.encode('utf-8').decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False


conn = sqlite3.connect('chat.db')
conn.execute("PRAGMA encoding='UTF-8';")
cur = conn.cursor()


#Enter the room name of the chat you want to train on
cur.execute("SELECT handle_id, text FROM message WHERE cache_roomnames = 'ENTER ROOM NAME HERE'")

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in cur.fetchall():
        handle_id, text = row

        # Uncomment to filter by the handle IDs of the people you want to train on
        # allowed_handle_ids = [If you want to only use specific people, put their handle IDs here]
        # if handle_id not in allowed_handle_ids:
        #     continue



        # Check if text is not null
        # Check if text is not whitespace
        # Check if text is valid UTF-8
        # Check if text starts with a word that is not a message (Tapback); ignore typo corrections; ignore shared links
        # Ignore certain unicode artifacts
        if text is None or text.isspace() or is_valid_utf8(text) == False or text.startswith(('Emphasized', 'Loved', 'Liked', 'Disliked', 'Questioned', 'Laughed', '*', 'http', 'www')) or text.endswith('*') or '\uFFFC' in text or '🫡' in text:
            continue

        writer.writerow(row)

conn.close()
