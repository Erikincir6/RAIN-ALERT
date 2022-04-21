import requests
from twilio.rest import Client

account_sid = 'AC50ec95c0dd11b927888bf2bb611a5ea5'
auth_token = '693bc1b28204087ba61e6409d0a17a04'

own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "72424a121772ae37eeca573e2845ea20"

weather_params = {
    "lat": "52.505489",
    "lon": "-2.106550",
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(url= own_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    #print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Remmeber to bring umbrela.",
        from_='+18124135961',
        to='+7792012033'
    )

    print(message.status)


#print(weather_data["hourly"][0]["weather"][0]["id"])



