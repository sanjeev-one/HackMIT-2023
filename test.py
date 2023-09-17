from OpenAILink import OpenAI_Connector
from YouTubeLink import YoutubeConnector
import os

openAI = OpenAI_Connector(api_key="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")
yt = YoutubeConnector(api_key="AIzaSyDlwroGPDdJRBiURxbwAXcIsjWE9CDv2u0")

playlists = yt.search_playlists("Best civil war playlists")

for playlist in playlists:
    print(playlist["title"])
    print(playlist["description"])
    print("")
