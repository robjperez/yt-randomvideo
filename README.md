# Youtube random video generator

Very simple application that given a list of channels, will open a new tab with a random video of a chosen channel.

It uses

- Python
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) for _backend_
- [preact](https://preactjs.com/) for _frontend_
- [Bulma](https://bulma.io) for CSS and styling
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for interacting with youtube (fetching all videos in a channel)

## How to run it

Edit `channels.ini` file and add your favourite YT channels.
Format should follow

```
[CHANNELS]
ChannelId = "https://....channel-url"
```

Then run

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```




