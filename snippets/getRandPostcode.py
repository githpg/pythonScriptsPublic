def get_rand_postcode():
    URL = f'https://api.postcodes.io/random/postcodes'
  
    r = requests.get(URL)
    data = r.json()
    postcode = data.get('result',[]).get('postcode')
    print(postcode)
    
    return postcode


count = 0
postcode_list = []

while count < 11:
    postcode = get_rand_postcode()
    
    postcode_list.append(postcode)
    count = count + 1  
    
print(postcode_list)
