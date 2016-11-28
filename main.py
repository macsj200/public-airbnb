import requests, json
temp = "https://www.airbnb.co.uk/search/search_results?guests=1&checkin=05-01-2017&checkout=07-01-2017&ss_id=bp105fju&ss_preload=true&source=bb&page=1&allow_override%5B%5D=&location=London&ne_lat=51.562340239897146&ne_lng=-0.03984353941632435&sw_lat=51.50586246311683&sw_lng=-0.22386453551007435&zoom=12&search_by_map=true"

# Look at docs for params values
'''
r = requests.get(BASE_URL, params={guests:1, checkin:05-01-2017})
'''
r = requests.get(BASE_URL, params={})

responseJSON = json.loads(r.text)
print(responseJSON)
