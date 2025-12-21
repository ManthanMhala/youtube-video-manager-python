import json

def Load_data():
    try:
        with open('yt.txt','r') as file:
            test = json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open('yt.txt','w') as file:
        json.dump(videos, file)

def All_videos(videos):
    print("\n")
    print("*" * 70)
    for index, videp in enumerate(videos, start=1):
        print(f"{index}. Name: {videp['name']}, Duration: {videp['time']} ")
    print("*" * 70)

def Add_videos(videos):
    name = input("enter the video name: ")
    time = input("enter the video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def Update_videos(videos):
    All_videos(videos)
    index = int(input("Enter the video num to update"))
    if 1<= index <=len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def Delete_videos(videos):
    All_videos(videos)
    index = int(input("Enter the video num to be deleted"))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else: 
        print("Invaldi video index slected")

def main():

    videos = Load_data()
    while True:
        print("\n Youtubes video manager | choos option")
        print("1. List all videos")
        print("2. Add a youtubes video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube videos")
        print("5. Exit")
        choice = input("Enter your choice")
        print(videos)
        match choice:
            case '1': 
                All_videos(videos)
            case "2":
                Add_videos(videos)
            case '3':
                Update_videos(videos)
            case '4':
                Delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice")
                


if __name__ == "__main__":
    main()