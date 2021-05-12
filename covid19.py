import requests


def Covid19(pincode):
    pincode = input('Enter the pincode :')
    current = 'https://api.postalpincode.in/pincode/'
    url = current + pincode
    json_data = requests.get(url).json()
    print(json_data)
    return json_data


def pincode(args):
    pass


print(Covid19(pincode)[0]['PostOffice'][0]['State'])
