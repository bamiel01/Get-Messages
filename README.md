
# Get Messages

A Python script that retrieves the specified messages from the archive of text messages on a Mac. The output is a CSV called `data.csv` that has the following schema in table form:

| author        | text        |
|---------------|-------------|
| Person's id | The message |
| Person's id | The message |
| Person's id | The message |
| Person's id | The message |



## Documentation

To use the script, you need the `chat.db` file that all of the messages are stored in.

Retrieve this file from `~/Library/Messages/chat.db`.

You will need to navigate through the database. Use the [DB Browser for SQLite](https://sqlitebrowser.org/) to find the value of `cache_roomnames` for the group chat you want to use. You can also find what phone number corresponds to what `handle_id`.





In the script itself, replace `ENTER ROOM NAME HERE` with the value you retrieved for `cache_roomnames`.

```python
cur.execute("SELECT handle_id, text FROM message WHERE cache_roomnames = 'ENTER ROOM NAME HERE'")
```

