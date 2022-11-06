import streamlit as st
import requests
import json


def get_image(lat, lon, zoom):
    url = 'https://api.openaerialmap.org/tiles/preview'
    params = {'lat': lat, 'lon': lon, 'zoom': zoom}
    response = requests.get(url, params=params)
    return response.json()['url']

def main():
    st.title("Get satellite images of a given location")
    st.markdown("Github Copilot test")

    st.header("Location")

    lat = st.text_input("Lat", '44.405013')
    lon = st.text_input("Lon", '8.949161')
    zoom = st.text_input("Zoom", '15')

    st.write(f"lat: {lat}, lon: {lon} - zoom: {zoom}")

if __name__ == '__main__':
    main()  