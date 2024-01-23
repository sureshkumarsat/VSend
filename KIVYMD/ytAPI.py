import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


api_key = 'AIzaSyAsYeEdylujBaJ6AmOapBY16_i1xDRSNuE'
YOUTUBE_API_KEY = os.environ.get('Youtube-API')


# flow = InstalledAppFlow.from_client_secrets_file("YouTubeClientSecretsOATH.json", scopes = ["https://www.googleapis.com/auth/youtube.readonly"])

# request = flow.Subscriptions().list('contentDetails', id='UCgVaUw8YLugxl74ZDcoQ_VQ')
# response = request.execute()
# print(response)
# youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)
# request = youtube.Subscriptions().list('contentDetails', channelId='UCgVaUw8YLugxl74ZDcoQ_VQ')
# response = request.execute()
# print(response)
# request = youtube.channels().list(part='contentDetails', id='UCgVaUw8YLugxl74ZDcoQ_VQ')
# response = request.execute()

# print(response)