import random
post_data = [
    {
        "userId":  "Alex Gates",
        "id": 1,
        "title": "sunt aut facere repellat provident",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId":  "Alex Gates",
        "id": 2,
        "title": "qui est esse ",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId":  "Alex Gates",
        "id": 3,
        "title": "ea molestias quasi exercitationem ",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId":  "Alex Gates",
        "id": 4,
        "title": "eum et est occaecati ",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId":  "Alex Gates",
        "id": 5,
        "title": " nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    },
    {
        "userId":  "Alex Gates",
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia ",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
    }, ]



id_valu = [post['id'] for post in post_data]
random_id = random.choice(id_valu)
idsss = random_id
user_post_id = post_data[idsss].get('title')
words = user_post_id.split()
words = [word.strip() for word in words]
first_three_words = words[:3]
remove_word = [word.replace("[", "").replace("]", "").replace("\"", "").replace(",", "") for word in first_three_words]
single_word = " ".join(remove_word)


def slugify (text):
    slug = text.strip().lower().replace(' ','-')
    while '--' in slug:
        slug = slug.replace('--','-')
    return slug
title = single_word
slugs = slugify(title)

usersIds = post_data[idsss].get('userId')
ids_users = post_data[idsss].get('id')
titleing_users = post_data[idsss].get('title')
content_body = post_data[idsss].get('body')
slug = slugs

print(f"""
{{
    'userId': '{usersIds}',
     'id': {ids_users}, 
     'title': '{titleing_users}', 
     'body': '{content_body}', 
     'slug': '{slug}'
}}
""")