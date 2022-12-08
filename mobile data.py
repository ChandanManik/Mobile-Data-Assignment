import random

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

datas = mobile_data.get('data')
exchnage_rate = mobile_data.get('exchnage_rate')

for i in datas:
    name = i.get('name')
    made = i.get('made')
    price = i.get('price')
    price_parts = price.split(" ")
    price_int = float(price_parts[0])*exchnage_rate
    price_BDT = round(price_int)
    sen1 = 'is made in', 'is manufactured in', 'is produced in'
    mades = random.choice(sen1)
    sen2 = 'The Price is', 'The value is', 'The amount is'
    price_sen =random.choice(sen2)
    sen3 = 'which is almost the same as','which is almost equivalent to' ,'which is almost comparable to'
    sen_almost = random.choice(sen3)

    sentences = (f"{name} {mades} {made}. {price_sen} {price} {sen_almost} {price_BDT} BDT")
    print(sentences)