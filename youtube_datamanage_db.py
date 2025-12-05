import sqlite3
con=sqlite3.connect('videos.db')
cursor=con.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_video(video,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES(?,?)",(video,time))
    con.commit()
def update_video(id,name,time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(name,time,id))
    con.commit()
def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id=?",(id,))
    con.commit()
def main():
    while True:
        print("\n Youtube Manager with db")
        print("1. List videos")
        print("2. add video")
        print("3. update video")
        print("4. delte video")
        print("5. exit")
        x=input("enter a choice: ")
        if x=='1':
            list_videos()
        elif x=='2':
            vid=input("enter the video name: ")
            tim=input("enter the video time: ")
            add_video(vid,tim)
        elif x=='3':
            id=input("enter the video id")
            vid=input("enter the video name: ")
            tim=input("enter video time: ")
            update_video(id,vid,tim)
        elif x=='4':     
            id=input("enter the video id: ")
            delete_video(id)
        elif x=='5':
            break
        else:
            print("enter a valid choice")
        print("===============================================================================================")
    con.close()
if __name__=="__main__":
    main()