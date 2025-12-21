import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb+srv://db_user123:Piyush@youtube.diajxuv.mongodb.net/?appName=youtube", tlsAllowInvalidCertificates=True)
# print(client)
db = client["ytmanager"]
video_collection = db["videos"]
print(client.list_database_names())

# print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"Id:{video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, v_time):
    video_collection.insert_one({"name": name, "time": v_time})
    

def update_video(video_id,newname,newtime):
    video_collection.update_one(
            {'_id': ObjectId(video_id)}, 
            {"$set": {"name":newname, "time": newtime}})

def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})


def main():
    while True:
        print("\n Youtube manager app")
        print("1. list all videos")
        print("2. add new video")
        print("3. update the video")
        print("4. delete the video")
        print("5. exit the app")
        choice = input("Enter your chioce")
        if choice =="1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name")
            time = input("Enter the video time")
            add_video(name,time)
        elif choice == "3":
            video_id = input("Enter the video id to updated")
            name = input("Enter the updated video name")
            time = input("Enter the updated video time")
            update_video(video_id,name,time)
        elif choice == "4":
            video_id = input("Enter the video id to updated")
            delete_video(video_id)
        elif choice =="5":
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()