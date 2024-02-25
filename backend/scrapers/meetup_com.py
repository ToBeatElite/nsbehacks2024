headers = {
    'authority': 'www.meetup.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

import requests, bs4, json, sys

def get_events_from_meetup_com(cityname):

    params = {
        'location': f'ca--on--{cityname}',
        'source': 'EVENTS',
    }

    response = requests.get('https://www.meetup.com/find/', params=params, headers=headers)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    my_json = str(soup.find_all('script')[2]).split('>')[1].split('<')[0] + '"}]'

    json_parser = json.loads(my_json)

    for event in json_parser:
        name = event.get("name")
        url = event.get("url")
        description = event.get("description")[:80]
    
        data = f'title="{name}"&description="{url, description}"&city="{cityname}"'

        response = requests.post(
            'http://localhost:8000/events/create',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=data
        )

        print(f'[+] {response.status_code} populated api')

get_events_from_meetup_com(sys.argv[1])