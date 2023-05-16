import json
import uuid
import random
from random_word import RandomWords

r = RandomWords()

pinterest_boards_uuid_list = [
    {"id": uuid.uuid4().int, "name": r.get_random_word()} for i in range(15)
]

tumblr_blogs_names_uuid_list = [
    {"id": uuid.uuid4().int, "name": r.get_random_word()} for i in range(25)
]

images_tags_list = [r.get_random_word() for i in range(10)]


def generate_pinterest_board_messages():
    for i in range(1000):
        choice = random.choice(pinterest_boards_uuid_list)
        message = {
            "message_id": uuid.uuid4().int,
            "status_code": random.choice([200, 201, 404]),
            "message_body": {
                "board_id": choice["id"],
                "board_name": choice["name"],
                "img_url": f"https://pinterest.com/{uuid.uuid4().hex}.png",
                "img_tag": random.choice(images_tags_list)
                }
        }
        with open(f"/home/illia/work/beetrot-academy/Module_2/Lesson 8/fake_parsing_messages/{uuid.uuid4().hex}.json",
                  "w") as f:
            f.write(json.dumps(message))


def generate_tumblr_messages():
    for i in range(1000):
        choice = random.choice(tumblr_blogs_names_uuid_list)
        message = {
            "message_id": uuid.uuid4().int,
            "status_code": random.choice([200, 201, 404]),
            "message_body": {
                "blog_name": choice["name"],
                "blog_id": choice["id"],
                "images":
                        [{"image_url": f"https://tumblr.io/{uuid.uuid4()}",
                          "image_tags": random.choice(images_tags_list)} for i in range(random.randint(1, 23))]
                }
        }
        with open(f"/home/illia/work/beetrot-academy/Module_2/Lesson 8/fake_parsing_messages/{uuid.uuid4().hex}.json",
                  "w") as f:
            f.write(json.dumps(message))


def generate_gettyimages_messages():
    for i in range(1000):
            message = {
                "message_id": uuid.uuid4().int,
                "status_code": random.choice([200, 201, 404]),
                "message_body": {
                    "img_url": f"https://gettyimages.com/{uuid.uuid4().hex}.png",
                    "img_tag": [random.choice(images_tags_list) for i in range(3)]
                    }
            }
            with open(f"/home/illia/work/beetrot-academy/Module_2/Lesson 8/fake_parsing_messages/{uuid.uuid4().hex}.json", "w") as f:
                f.write(json.dumps(message))


generate_gettyimages_messages()
generate_pinterest_board_messages()
generate_tumblr_messages()
