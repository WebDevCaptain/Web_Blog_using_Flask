import uuid
import datetime
from common.database import Database


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.date = date

    def save_to_mongo(self):
        Database.insert(collection="posts", data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "blog_id": self.blog_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "date": self.date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': blog_id})]

# Deleted from `from_mongo` method
# blog_id=post_data['blog_id'], title=post_data['title'], content=post_data['content'],
#                    author=post_data['author'], date=post_data['date'], _id=post_data['_id']
