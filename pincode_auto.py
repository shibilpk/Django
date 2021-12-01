def get_pincode_by_name(request):
    places = []

    name = request.GET.get('name')

    print("name====>>", name)

    baseurl_1 = f"https://api.postalpincode.in/pincode/691559"
    baseurl_place = f"https://api.postalpincode.in/postoffice/{name}"
    baseurl_2 = f"https://maps.googleapis.com/maps/api/geocode/json?address=691559&key={SETTINGS.PLACES_MAPS_API_KEY}"
    postofficeapi_response = requests.get(baseurl_1).json()
    googleapi_response = requests.get(baseurl_2).json()

    place_name_response = requests.get(baseurl_place).json()

    print(googleapi_response)

    if postofficeapi_response[0]["Status"] == 'Success' and googleapi_response['status'] == 'OK':

        if 'PostOffice' in postofficeapi_response[0] and 'postal_code' in googleapi_response['results'][0]['types']:
            for post_offices in postofficeapi_response[0]['PostOffice']:
                response = post_offices
                print(googleapi_response['results'][0]['geometry']['location']['lng'])

        places = []
        for name in place_name_response[0]["PostOffice"]:
            print(name['Name'])
            data = {
                "name": name['Name'],
                "pincode": name['Pincode']
            }
            places.append(data)

    response_data = {
        "status": "true",
        "values": json.dumps(places),
    }

    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
