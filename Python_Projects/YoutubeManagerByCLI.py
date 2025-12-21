import sqlite3
import csv
connection = sqlite3.connect('YoutubeManager.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL                   
               )
           ''')

def All_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def Add_video(video_name, video_time, video_id):
    try:
        cursor.execute("INSERT INTO videos (name, time, id) VALUES (?, ?, ?)", (video_name, video_time, video_id))
        connection.commit()
    except sqlite3.IntegrityError:
        print("Video alredy exists")
        
def Update_video(video_id, new_video_name, new_video_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_video_name, new_video_time, video_id))
    connection.commit()
    
def Delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    connection.commit()

def Search_video(video_name):
    cursor.execute("SELECT * FROM videos WHERE name = ?",(video_name,))
    result = cursor.fetchone()
    if result:
        print(result)
    else:
        print("Invalid video name")

def Sort_video():
    sorted_time = cursor.execute("SELECT * FROM videos ORDER BY time ASC")
    for s_t in sorted_time:
        print(s_t)

def Export_to_csv(filename="videos.csv"):
    cursor.execute("SELECT * FROM videos")
    row = cursor.fetchall()
    with open(filename, mode="w", newline="", encoding="utf8") as file:
        write = csv.writer(file)
        write.writerow(["ID", "Name", "Time"])
        write.writerows(row)
        print(f"Data exported to {"videos.csv"}")
    
def main():
    while True:
        list_choice = ["1. All videos", "2. Add video", "3. Update video", "4. Delete video", "5. Search video", "6. Sort by time", "7. Export CSV file", "8. Exit"]
        for choices in list_choice:
            print(choices)
            
        choice = int(input("Enter the choice from below: "))
        
        if choice == 1:
            All_videos()
        elif choice == 2:
            video_id = int(input("Enter the video id: "))
            video_name = input("Enter the video name: ")
            video_time =input("Enter the video time in the MM:SS: ")
            Add_video(video_name, video_time, video_id)
        
        elif choice == 3:
            video_id = int(input("Enter the video id: "))
            video_name = input("Enter the video name: ")
            video_time = input("Enter the video time: ")
            Update_video(video_id, video_name, video_time)
        
        elif choice == 4:
            video_id = int(input("Enter the video id: "))
            Delete_video(video_id)
        
        elif choice == 5:
            video_name = input("Enter the video name you want to search: ")
            Search_video(video_name)
        
        elif choice == 6:
            Sort_video()
        
        elif choice == 7:
            Export_to_csv()
        
        elif choice == 8:
            break
        
        else:
            print("Invalid choice choose correct")
            
if __name__ == "__main__":
    main()