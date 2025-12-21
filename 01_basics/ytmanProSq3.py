import sqlite3

con = sqlite3.connect("yt.db")
cur = con.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )
            ''')


def all_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name,time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    
def update_video(video_id,new_name, new_time ):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos where id = ?",(video_id,))
    con.commit()
    
def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update Videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")
        
        if choice =='1':
            all_videos()
        elif choice == '2':
            name = input("Enter the video name")
            time = input("Enter the video time")
            add_video(name, time)
        elif choice == '3':
            video_id= input("Enter the video id to update")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id= input("Enter the video id to delete")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
            
    con.close()

if __name__ == "__main__":
    main()
