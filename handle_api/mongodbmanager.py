from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.kqfpimw.mongodb.net/managerusingmongo",tlsAllowInvalidCertificates=True)

db = client["managerusingmongo"]
video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name:{video['name']}, Time:{video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def delete_video(id):
    video_collection.delete_one({'_id': ObjectId(id)})

def update_video(name, time, id):
    video_collection.update_one(
        {'_id': ObjectId(id)},
        {"$set": {'name': name, 'time': time}}
    )

def main():
    while True:
        print("welcome to Your Youtube Data-Manager")
        print("1. list all videos")
        print("2. add new video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit the app")

        x = input("enter your choice: ")

        if x == '1':
            list_videos()
        elif x == '2':
            name = input("enter video name: ")
            time = input("enter video time: ")
            add_video(name, time)
        elif x == '3':
            id = input("enter videoid to update: ")
            name = input("enter new video name: ")
            time = input("enter new video time: ")
            update_video(name, time, id)
        elif x == '4':
            id = input("enter videoid to delete: ")
            delete_video(id)
        elif x == '5':
            break
        else:
            print("enter valid choice")

        print("============================================================")

if __name__ == "__main__":
    main()
