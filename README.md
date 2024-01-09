## YouTube Downloader Bot

### Abilities

- **Fast YouTube Video Downloader:**
  - The bot allows users to download YouTube videos quickly by sending the video link.

### Getting Started

To use the YouTube Downloader Bot, follow these steps:

1. **Start the Bot:**
   - Start a chat with the bot by searching for it on Telegram or clicking on the provided link.

2. **Send YouTube Video Links:**
   - Send YouTube video links directly to the bot. It supports links in various formats, including full YouTube URLs or video IDs.

3. **Download Options:**
   - Once a valid YouTube link is sent, the bot will process it and provide download options. Users can choose from available formats.

4. **Download Video:**
   - After selecting a download option, the bot will generate a download link for the chosen video format. Users can click on the link to download the video.

### Code Overview

#### `loader.py`
   - Initializes the Telegram bot, Dispatcher, and connects to the SQLite database.

#### `main.py`
   - Configures logging, creates database tables, and starts the bot's polling.

#### `handlers/`
   - Contains different modules for handling specific tasks.

#### `handlers/start_handler.py`
   - Handles the "/start" command and welcomes users. Inserts or updates user information in the database.

#### `handlers/message_handler.py`
   - Handles all other incoming messages by providing a generic instruction to send a YouTube link.

#### `handlers/url_handler.py`
   - Processes messages containing YouTube links. Retrieves video details, saves information to the database, and provides download options.

#### `handlers/format_handler.py`
   - Handles callback queries related to downloading videos. Creates an inline keyboard with different video formats for users to choose from.

### Dependencies

- `aiogram`: A powerful and flexible framework for building Telegram bots in Python.
- `pytube`: A lightweight, dependency-free Python library for downloading YouTube videos.

### Running the Bot

1. Install the required dependencies:

   ```bash
   pip install aiogram pytube
   ```

2. Set up your Telegram bot token and database connection in the `loader.py` file.

3. Run the `main.py` script to start the bot:

   ```bash
   python main.py
   ```

### Contribution

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE).
```
