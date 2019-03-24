class User:
    def __init__(self, username):
        self.name = username
        self.posts = []

    def addPost(self, title, body):
        self.posts.append(Post(title, body))


class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body
