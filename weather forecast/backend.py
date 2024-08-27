import requests

api_key="928a8dfeabcf284627145de9550237ff"
def retrieve_data(location,days=None,mode=None):

    url=f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data['list'][:8*days]
    dates=[dict['dt_txt'] for dict in filtered_data]
    if mode == 'Temperature':
        filtered_data=[dict['main']['temp']/10 for dict in filtered_data]
    elif mode == 'Sky':
        filtered_data=[dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data,dates

if __name__ == "__main__":
    print(retrieve_data(location='Queenstown',days=2,mode='Sky'))
