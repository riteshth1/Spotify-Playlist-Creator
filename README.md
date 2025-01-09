# Spotify Playlist Generator

This project allows users to create a Spotify playlist featuring the top songs from the Billboard Hot 100 chart for a specific date.

## Features

- Scrape the Billboard Hot 100 chart for a specific date using web scraping.
- Search for songs on Spotify using their API.
- Create a private playlist in Spotify and add the top songs.

## Requirements

- Python 3.7 or later
- Required Python Libraries:
  - `spotipy`
  - `requests`
  - `beautifulsoup4`
- A Spotify Developer Account

## Setup Instructions

1. **Clone or Download the Project**  
   Clone this repository to your local machine or download the ZIP file.

2. **Install the Required Python Libraries**  
   Run the following command to install the required libraries:
   ```bash
   pip install spotipy requests beautifulsoup4
   ```

3. **Create a Spotify Developer Application**  
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app and note the **Client ID** and **Client Secret**.
   - Set the redirect URI to: `https://open.spotify.com/`.

4. **Update the Python Script**  
   Open the Python script and update the following variables with your Spotify app credentials:
   ```python
   CLIENT_ID = "your_client_id"
   CLIENT_SECRET = "your_client_secret"
   REDIRECT_URI = "https://open.spotify.com/"
   ```

5. **Run the Script**  
   Execute the script in your terminal:
   ```bash
   python script_name.py
   ```

6. **Authenticate with Spotify**  
   - Follow the authentication prompts to link your Spotify account.
   - Provide a date in the format `YYYY-MM-DD` to fetch the Billboard Hot 100 for that week.

## Usage

1. Enter a date (e.g., `2023-01-01`) to retrieve the Billboard Hot 100 chart for that week.
2. The script will scrape the Billboard website to fetch the song titles.
3. It will search Spotify for the songs and create a private playlist in your account with the matched tracks.

## Output

The script generates:
- A list of the top songs from the specified Billboard Hot 100 chart.
- Spotify URIs for the matched songs.
- A new private playlist in your Spotify account with the retrieved songs.

## Notes

- Some songs might not be found on Spotify due to differences in naming or availability.
- The playlist is created as private by default.
- Ensure that your Spotify account is properly linked during the OAuth process.

## Author

Developed by **Ritesh**.
