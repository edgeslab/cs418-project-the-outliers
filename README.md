# cs418-project-the-outliers

Siham Hussein: shusse6@uic.edu, seehamrun@

Fatima Qarni: fqarni2@uic.edu, qarni@

Zaynab Almoujahed: zalmou2@uic.edu, zalmoujahed@ 

Amit Panthi: apanth2@uic.edu, apanth2@

David Qiao: dqiao4@uic.edu, chowsterr@


# Setup and Running

Run the Jupyter notebook with 

```
$ cd spotify-analysis
$ jupyter notebook &
``` 

this will run Jupyter in a Browser window and from there you can view the contents of our notebook under  
SpotifyAnalysis.ipynb.

To run the python application you will need to obtain an API Key from the Spotify Developer API. 
Copy the API key and secret into a file called `api_key.py` under the spotify-analysis folder.
You can use the template `api_key_template.py` for reference. 


## Running the demo

To run the demo locally, install all the requirements and then simply run the main.py file

```
$ cd spotify-analysis
$ pip install -r requirements.txt
$ python main.py
```

After this is complete, you can visit `localhost:8080` on a web browser to access the web application demo. 

# How the demo works

The demo is able to access any playlist or song given it's ID and predict the year and genre that the song is in.
You can find the ID of any Spotify playlist from it's URL. For example, my 2018 top hits playlist has the URL 
https://open.spotify.com/playlist/37i9dQZF1EjfqxFAXDW9WK. The playlist ID is then 37i9dQZF1EjfqxFAXDW9WK. 

For individual songs, you will have to click on the 3 dots about a song and get the song link. For example: 
https://open.spotify.com/track/5L95vS64rG1YMIFm1hLjyZ is the song Rollercoaster by Bleachers, and it's ID is 
5L95vS64rG1YMIFm1hLjyZ

Our deployed demo is available at https://https:spotify-outliers.appspot.com
