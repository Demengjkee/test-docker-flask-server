import pymongo
import os
import datetime
import logging


def connect():
    try:
        mongo_host = os.environ["MONGODB_HOST"]
        mongo_port = os.environ["MONGODB_PORT"]
        mongo_user = os.environ["MONGODB_USER"]
        mongo_password = os.environ["MONGODB_PASSWORD"]
    except KeyError as e:
        logging.error(str(e))
    mongo_url = "mongodb://{}:{}@{}:{}".format(
        mongo_user, mongo_password, mongo_host, mongo_port
    )
    client = pymongo.MongoClient(mongo_url)
    return client

def get_db(conn):
    try:
        db_name = os.environ['MONGODB_DATABASE']
    except KeyError as e:
        logging.error(str(e))
    db = conn[db_name]
    return db

def post_document(post, db):
    post = {"text": post, "date": datetime.datetime.utcnow()}
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    return post_id

def get_documents(db):
    posts = db.posts
    return posts.find({})

def main():
    conn = connect()
    db = get_db(conn)
    post_document("test", db)
    print(get_documents(db))
    return 0

if __name__ == "__main__":
    main()
