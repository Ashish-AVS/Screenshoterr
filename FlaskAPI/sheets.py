import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import cloudinary
import cloudinary.uploader

          
cloudinary.config( 
  cloud_name = "dw9w4uzxk", 
  api_key = "649219127577599", 
  api_secret = "jROGR3SicpVts2qCUNtme6f13Ys" 
)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive.file', "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(creds)



def addPhoto(timestamp, imageURL):
    sheet = client.open('WebsiteScreenshots').sheet1

    data = sheet.get_all_records()

    # Code to upload base64 image to cloudinary
    image_cloudinary = cloudinary.uploader.upload(imageURL, public_id = timestamp)
    cloudinary_url = image_cloudinary['url']


    numRows = sheet.row_count
    activeRows = len(data)
    insertRow = [timestamp, cloudinary_url]
    sheet.append_row(insertRow)
    print(numRows)


