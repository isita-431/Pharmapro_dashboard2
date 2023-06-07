# import streamlit as st
# import gspread
# from gspread.service_account import ServiceAccountCredentials

# # Manually provide the credentials
# credentials = {
#     "type": "service_account",
#     "project_id": "your-project-id",
#     "private_key_id": "your-private-key-id",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nYour Private Key\n-----END PRIVATE KEY-----\n",
#     "client_email": "your-client-email",
#     "client_id": "your-client-id",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "your-client-cert-url"
# }

# # Set up Google Sheets credentials
# creds = ServiceAccountCredentials.from_service_account_info(credentials)
# client = gspread.authorize(creds)

# # Access the Google Sheet
# sheet = client.open('Your Google Sheet Name').sheet1

# # Read data from the sheet
# data = sheet.get_all_records()

# # Display data in Streamlit
# st.write(data)

# import streamlit as st
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# # Manually provide the credentials
# credentials = {
#   "type": "service_account",
#   "project_id": "scraper-project-372415",
#   "private_key_id": "9205570bc230bacd2cf1809d58372635d012e331",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDGiuummK6CTD8H\nAV9zcJKzg5BqviZL3/Qi9SmBIhVTljMKoE4kcz8mEI8GxXJj9XRrYWqRHihOEKyg\npaz3SNcErVsYImQWXt8+7QGHoZJYWfwG5Cv+ZC/PbFMVDMBe4IzlyfPHrXlUD3Bz\nO6zb2LFPNYmxxLVeXL6aWmAsK1PfhQQwsNqcv7zzHSnrc8RaQnYtPNJiubWMQlsR\nu6jcG6jaBl70Cou7WkLtXqrkrwDCf592hRy/5Qn/g2N3H9CMJNe+UShQ5zPedmVE\nJbmCTA9JPhdntHbdpcGIkcoqUyGJiJ360cU9pobpYvFul2b3T3UzJ5sHDQ2UiyEY\nF0qMxZjzAgMBAAECggEAVv6P+tNzw4v9IeisFj0BSr8fDGZ9CUn8A0VBBmAU0CdD\n/if3lWkaBmfDA8iIMtxeQp7Qvv1j07DisxFlFIVKEbaT76NCD7tKPpxCy1c0dJoZ\nIDviOvlTKaPhU5vevrPNiPJQavHL89VABH3lY/8y0e43gzkZ71rb+W4YLcJeYdV1\nMclWV6PVrVbFXoRCrwLqJ4hFVD9iN0ySuLAw38DFTu8lrodvtq7HLbRn0X0qibGE\nPHTjZ3z6djc/XtMBo5RagmCEtDHGWUPKbw1PF5X1TLyDpQUTYmwWZZt1hlWoxdaM\n9ClFWASRoSPrSuvJGa/uQ6rMaMvXJ6HUM5nQSMJ/wQKBgQDooTuUyZLihJwvco4G\npeepEfcAwHi/iGIGVKdN5ivxOP3TuqtGaSxSQ3tInJ7eaiuIQwTj1No24iNAN/IN\nYi83q/GfXgKDLcyWNyPdMfyLkQt34i6Uz1y2O0LL/xhejgMsBHzS6IxJJx2ItX1L\nOBbvVozpZRkPwZ/PvLOVbTggmwKBgQDafQkCWSoYgSZX44pn/EQKPamfUEQc3DKv\nxCZZdqca30p5DvaExrFUOIe5qovD///PVF50N3USobFkRXgk4jr26gPl6Cxg/+E5\n9+9Ma13pwM+qGUovcQgHiuloD9CKLmna/bqrgETpOwAngxYB4XHdKPEhyRrlgj+e\nVU80TEfSiQKBgQDPk6dlsaSGycvQLsj6t6mKXMRqAFT+m4TUn08WnK9TNQaRmnzg\nfFKXKS3l8hN05Ynosdy4K6N327uWvxUWyijV5XDaQvm88e4fkB5JbyQpqYhxNftY\nv9u7pA+Llhm5rcC401xKmkUrtWKOLVwa9XbJpBJi5NpDDAQ9SuV4DZhKxwKBgAmM\nTUh8/Qn1GufcWcARliecaj08FL3uIYjs2YAvXz4dY/PGY5+Jz1YO4l+KxHDcTyGQ\nXlBV3BfkWQw4vPdfq5P+xgzWCJp0lDMkUqDUUFZWxrx4PnW0StWJjImvpz1iqd2Y\nGQBFqr1GhsszP1L1tzQjBeakEzjUaFNTBxMSAlGBAoGAG6gnGC2lxVQvnIfH0Y+Y\nYnLmWhhfhpbSj/x47pGbj5Q8Fe7SNbZW+pkFmrQDb9Me5wRfmsszJxGAZoAJoVOd\nEtGHd4+1wweJ10Cfae8e37oJbA/iIHxZgiPrwTDXvgJo66SZyqBRa4pOJD2hJLoD\nJB8SMFThpMUZ6Y+AhlV+uQM=\n-----END PRIVATE KEY-----\n",
#   "client_email": "bio-scraper@scraper-project-372415.iam.gserviceaccount.com",
#   "client_id": "113537510657830910120",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bio-scraper%40scraper-project-372415.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }


# # # Set up Google Sheets credentials
# # creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
# # client = gspread.authorize(creds)

# # # Access the Google Sheet
# # sheet = client.open('final merged').sheet1

# # # Read data from the sheet
# # data = sheet.get_all_records()

# # # Display data in Streamlit
# # st.write(data)
# # Set up Google Sheets credentials
# # creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
# # client = gspread.authorize(creds)

# # # Fetch the names of all spreadsheets
# # spreadsheet_files = client.list_spreadsheet_files()
# # spreadsheet_names = [file['name'] for file in spreadsheet_files]

# # # Display the names of the spreadsheets in Streamlit
# # st.write("Spreadsheet Names:")
# # for name in spreadsheet_names:
# #     st.write(name)

# # Set up Google Sheets credentials
# creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
# client = gspread.authorize(creds)

# # Get all spreadsheets accessible to the service account
# spreadsheets = client.openall()

# # Extract and display the names of the spreadsheets
# spreadsheet_names = [spreadsheet.title for spreadsheet in spreadsheets]
# st.write(spreadsheet_names)

# import streamlit as st
# import gspread
# from google.auth import credentials
# from oauth2client.service_account import ServiceAccountCredentials

# # Manually provide the credentials
# credentials = {
#   "type": "service_account",
#   "project_id": "keen-quest-388604",
#   "private_key_id": "daf2a808a49576b6b990c50d08297eb1b85c5003",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXU1+ZJDf7GybW\n+lGUYE8WFuDuwSOPpBtWZvl1dfTRVZxPjWnc6ZVRvCxc5/g2Xonl3t0W3J/JvUeg\nKmBSX3HN051EcM0awihYSo2f35sKAx/aDDrHzEp6LJ7zuCqEUnggnX9uI6dfS9cV\nLi9z90oqZU3xtcn2ywTVB81bSXCZAWuEjBf1sb4kV6OEiF4rpbYhijFU0M+ls2nF\nTjKhS7a8VAEnfkWDy7fTt+0MQ2iS7/YAS+Kvd8uP60aW1ohXN/mqYuT+St27HdyX\nI5lOfpsu+2Nyk2zeiSfMWlI5ZZmpQfBHic/k6pf8jk5dEkgVoI2Khh0rIISsBNhR\nnpwptrkhAgMBAAECggEARMnBQhKkgadAZrAsLKsByOxBKnTwD9zc0OLvsZsfvVpM\np8tk9Op4RdbIE1wV2wSjqBhk5/9OWqwJvDydbeNI33jJhopEs9Yv/li+2sKb7Hxo\nCggbJSX56wLjOrfseT5BWyYFhiGEwDhhu0X4aeMnwdiAKIYrQZjE7+tgqteQzYfk\nvRh4Dw10ETVwSVhXu7spRa9cy208H1VWJI2EWAxWTqQokXmcEFuFPnlOhrKCGw9E\nkfJ9H/4yS343tmnDcRi5KAu5bAihinTJTziu/Omh+JfY9VpkBWquIcfEZJAxAdU5\ny1a9C3zn9LeT0A+xNMh9h8t7080roFqC4UcgOiJN4wKBgQD7aUPzeDxbbWpfrbTo\n+s7lBue7NryJur1qTyeTBYUrRoBkedtnmqq4Y5vJHTgmPkdL/1rgE7Zrr9i9qmLX\n5SGfKUMa/drJxUSaKVklOaKrmw7uKdUfYDIJKm0kltWhdmN+MWo4pR96W0MOEFKS\npjrGYwpjoa1pBQddPnmDLJw1lwKBgQDbQX8Ed1OJ3vi9knqmGxToYxGBVrj1OmDz\nogCu1kT8BsPd2uTYfoqLPZRRXvSOHZgVAnNosIN+db4KaSXSDGO863rgurjsDhRY\na3rcxyC0VtTYp3ik+7fWk58g2nDX/DWZ8nYuUQp0Yd6oqM2bqoVgPplf9INiNeQD\npU/Qa/UOBwKBgANr/1zE+i1UY+pBdwDkyQQc//JwYEiPnhxgT22U2acpIn47mlzi\nogg4ctpd53G9z0KdiyMZoZX9ormSJB5EJB0CdsNbSSsN4E0o2unCyxAC4EUllJ0E\ntimhxjKFSwsTjW8eRQ/YT4Fe1J7QYg9U69/fYTjR7oZLZzpBq225obapAoGBAJd1\nbyDOrU6YUIvkHAWSv6aoiPcnySzd3wtt5brhGVZf9f3TsDI9d8coCsULKzThDKW2\nw7KV/L/m5hia+h1Xoa5nnMKROh0WvMc3t++7PsRVF0NyrMyLdjssTsiLHViWSRDH\nhQwJv4cV9JHdyeq2qNwLYjf+2KOHRrOeBrybVvURAoGAAyWhfiMMM51xLw+NQqHa\nyOUiPCLTdihG8IREF0d1n8hugVKUDG+jlsIXZZmu5Nq2fvcbnL89f7RMPjG1lbGS\nZs/wkQJpBvIjMNsqfnvRGg4X2x66Joz2g+42WSkUuPmDf+bkb2Rzx+GzXltpxnPP\nzOdQhCxrwCDiiyUH3R+8gE8=\n-----END PRIVATE KEY-----\n",
#   "client_email": "serviceacc1@keen-quest-388604.iam.gserviceaccount.com",
#   "client_id": "104037426221423372910",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/serviceacc1%40keen-quest-388604.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }

# # Set up Google Sheets credentials
# creds = ServiceAccountCredentials.from_service_account_info(credentials)
# client = gspread.authorize(creds)

# # Set up Google Sheets credentials
# # client = gspread.Client(auth=credentials)

# # Connect to Google Sheets
# client.connect()

# # Open the desired spreadsheet
# spreadsheet = client.open('urologist')


# # Access the first sheet
# sheet = spreadsheet.sheet1

# # Read data from the sheet
# data = sheet.get_all_records()

# # Display data in Streamlit
# st.write(data)




import streamlit as st
import gspread
import pandas as pd
from geopy.geocoders import Nominatim
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from urllib3.exceptions import ReadTimeoutError
from geopy.exc import GeocoderTimedOut
import plotly.express as px
import pandas as pd


# Manually provide the credentials
credentials = {
  "type": "service_account",
  "project_id": "keen-quest-388604",
  "private_key_id": "daf2a808a49576b6b990c50d08297eb1b85c5003",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXU1+ZJDf7GybW\n+lGUYE8WFuDuwSOPpBtWZvl1dfTRVZxPjWnc6ZVRvCxc5/g2Xonl3t0W3J/JvUeg\nKmBSX3HN051EcM0awihYSo2f35sKAx/aDDrHzEp6LJ7zuCqEUnggnX9uI6dfS9cV\nLi9z90oqZU3xtcn2ywTVB81bSXCZAWuEjBf1sb4kV6OEiF4rpbYhijFU0M+ls2nF\nTjKhS7a8VAEnfkWDy7fTt+0MQ2iS7/YAS+Kvd8uP60aW1ohXN/mqYuT+St27HdyX\nI5lOfpsu+2Nyk2zeiSfMWlI5ZZmpQfBHic/k6pf8jk5dEkgVoI2Khh0rIISsBNhR\nnpwptrkhAgMBAAECggEARMnBQhKkgadAZrAsLKsByOxBKnTwD9zc0OLvsZsfvVpM\np8tk9Op4RdbIE1wV2wSjqBhk5/9OWqwJvDydbeNI33jJhopEs9Yv/li+2sKb7Hxo\nCggbJSX56wLjOrfseT5BWyYFhiGEwDhhu0X4aeMnwdiAKIYrQZjE7+tgqteQzYfk\nvRh4Dw10ETVwSVhXu7spRa9cy208H1VWJI2EWAxWTqQokXmcEFuFPnlOhrKCGw9E\nkfJ9H/4yS343tmnDcRi5KAu5bAihinTJTziu/Omh+JfY9VpkBWquIcfEZJAxAdU5\ny1a9C3zn9LeT0A+xNMh9h8t7080roFqC4UcgOiJN4wKBgQD7aUPzeDxbbWpfrbTo\n+s7lBue7NryJur1qTyeTBYUrRoBkedtnmqq4Y5vJHTgmPkdL/1rgE7Zrr9i9qmLX\n5SGfKUMa/drJxUSaKVklOaKrmw7uKdUfYDIJKm0kltWhdmN+MWo4pR96W0MOEFKS\npjrGYwpjoa1pBQddPnmDLJw1lwKBgQDbQX8Ed1OJ3vi9knqmGxToYxGBVrj1OmDz\nogCu1kT8BsPd2uTYfoqLPZRRXvSOHZgVAnNosIN+db4KaSXSDGO863rgurjsDhRY\na3rcxyC0VtTYp3ik+7fWk58g2nDX/DWZ8nYuUQp0Yd6oqM2bqoVgPplf9INiNeQD\npU/Qa/UOBwKBgANr/1zE+i1UY+pBdwDkyQQc//JwYEiPnhxgT22U2acpIn47mlzi\nogg4ctpd53G9z0KdiyMZoZX9ormSJB5EJB0CdsNbSSsN4E0o2unCyxAC4EUllJ0E\ntimhxjKFSwsTjW8eRQ/YT4Fe1J7QYg9U69/fYTjR7oZLZzpBq225obapAoGBAJd1\nbyDOrU6YUIvkHAWSv6aoiPcnySzd3wtt5brhGVZf9f3TsDI9d8coCsULKzThDKW2\nw7KV/L/m5hia+h1Xoa5nnMKROh0WvMc3t++7PsRVF0NyrMyLdjssTsiLHViWSRDH\nhQwJv4cV9JHdyeq2qNwLYjf+2KOHRrOeBrybVvURAoGAAyWhfiMMM51xLw+NQqHa\nyOUiPCLTdihG8IREF0d1n8hugVKUDG+jlsIXZZmu5Nq2fvcbnL89f7RMPjG1lbGS\nZs/wkQJpBvIjMNsqfnvRGg4X2x66Joz2g+42WSkUuPmDf+bkb2Rzx+GzXltpxnPP\nzOdQhCxrwCDiiyUH3R+8gE8=\n-----END PRIVATE KEY-----\n",
  "client_email": "serviceacc1@keen-quest-388604.iam.gserviceaccount.com",
  "client_id": "104037426221423372910",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/serviceacc1%40keen-quest-388604.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Set up Google Sheets credentials
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
client = gspread.authorize(creds)

# Access the Google Sheet
sheet = client.open('urologist').sheet1

# # Read data from the sheet
data = sheet.get_all_records()


# # Display data in Streamlit
# st.write(data)
# Convert data to pandas DataFrame
st.markdown('# Urologist data : ')
st.write(' A urologist is a medical doctor specializing in conditions that affect the urinary tract in men, women and children, and diseases that affect the reproductive system. These conditions range from peeing too much or too little to being unable to father a child. ')

df = pd.DataFrame(data)

# Handle the conversion issue in 'Cost2' column
df['Cost2'] = pd.to_numeric(df['Cost2'], errors='coerce')
df['Experience(years)'] = pd.to_numeric(df['Experience(years)'], errors='coerce')

st.write()


# Display data in Streamlit
# Create empty lists to store coordinates
# latitudes = []
# longitudes = []

# # Create a geocoder object
# def get_coordinates(city):
#     geolocator = Nominatim(user_agent="my-app")
#     location = geolocator.geocode(city)
#     if location:
#         latitude = location.latitude
#         longitude = location.longitude
#         return latitude, longitude
#     else:
#         return None, None

# # Example usage
# for city in df['Location']:
#     latitude, longitude = get_coordinates(city)
#     if latitude and longitude:
#         latitudes.append(latitude)
#         longitudes.append(longitude)
#         print(f"The coordinates of {city} are: Latitude={latitude}, Longitude={longitude}")
#     else:
#         latitudes.append(' ')
#         longitudes.append(' ')
#         print(f"Failed to retrieve coordinates for {city}")

# # Lookup coordinates for each city
# # for city in df['Location']:
# #     location = geolocator.geocode(city)
# #     if location:
# #         latitudes.append(location.latitude)
# #         longitudes.append(location.longitude)

# # Lookup coordinates for each city
# # for city in df['Location']:
# #     lat, lon = geocode_city(city)
# #     if lat and lon:
# #         latitudes.append(lat)
# #         longitudes.append(lon)

# # Create a DataFrame with the city names and coordinates
# data = {'City': df['Location'], 'Latitude': latitudes, 'Longitude': longitudes}
# df2 = pd.DataFrame(data)
fig = px.histogram(df, x='Cost2')

# Customize the layout (optional)
fig.update_layout(
    title='Distribution of Average fee of the doctor',
    xaxis_title='fee',
    yaxis_title='Count'
)

# # Display the histogram
fig.show(config = dict(displayModeBar = False))
# Display the histogram in Streamlit
st.plotly_chart(fig,config = dict(displayModeBar = False))

fig = px.histogram(df, x='Experience(years)',color_discrete_sequence=['#FFA500'])

# Customize the layout (optional)
fig.update_layout(
    title='Distribution of experience of the doctors',
    xaxis_title='Experience in years',
    yaxis_title='Count',
)
fig.show(config = dict(displayModeBar = False))
st.plotly_chart(fig,config = dict(displayModeBar = False))
st.markdown('## Statistics about urologists in India : ')
st.write(df.describe())

# fig = px.scatter(df, x='Location', color='Location')

# # Customize the layout
# fig.update_layout(
#     title='Categorical Plot of Cities',
#     xaxis_title='Location',
#     yaxis_title='Count',
# )

# # Display the scatter plot in Streamlit
# st.plotly_chart(fig)
city_counts = df['Location'].value_counts()

# Get the top 10 cities by count
top_10_cities = city_counts.head(10)

st.markdown('## Top 10 cities where the count of oncologists is highest : ')

st.write(top_10_cities)
# st.write(top_10_cities.columns)

# Create a bar plot using Plotly Express
fig = px.bar(top_10_cities, x=top_10_cities.index, y=top_10_cities.values,color=top_10_cities.index)

# Customize the layout
fig.update_layout(
    title='Top 10 Occurring Cities',
    xaxis_title='City',
    yaxis_title='Count',
)

# Display the bar plot in Streamlit

fig.show(config = dict(displayModeBar = False))
st.plotly_chart(fig,config = dict(displayModeBar = False))
st.write('Map plot')

# df['latitude'] = df['latitude'].astype(float)
# df['longitude'] = df['longitude'].astype(float)
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')


fig = px.scatter_mapbox(df, lat='latitude', lon='longitude',hover_data={'latitude': False, 'longitude': False},text = df['Location'] ,zoom=6, height=500,size_max = 20, 
                                        color='Location')
#       # color_discrete_sequence=['red']
fig.update_layout(mapbox_style='open-street-map', mapbox_zoom=6,
                      mapbox_center={'lat': 21.1458, 'lon': 79.0882})
fig.show(config = dict(displayModeBar = False))
st.plotly_chart(fig,config = dict(displayModeBar = False))
# Display the DataFrame
# st.write(df2.head())

# # Print the coordinates
# for city, lat, lon in zip(df['Location'], latitudes, longitudes):
#     print(f"{city}: Latitude={lat}, Longitude={lon}")


# st.write(df)
