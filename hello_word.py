import json
def list_all_videos(video):
    for ind,video in enumerate(video,start=1):
        print(f"{ind}-{video['name']}")
def add_video(video):
    name=input("add the name of the video: ")
    time=input("enter video time: ")
    video.append({'name':name,'time':time})
    save_data_helper(video)
def update_video(video):
    pass
def delete_video(video):
    pass
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(video):
    with open('youtube.txt','w') as file:
        json.dump(video,file)
def main():
    videos=load_data()
    while(True):
        print("YoutubeMangaer")
        print("1. list all the videos")
        print("2. Add a youtube video")
        print("3. update a videos detail")
        print("4. Delete A video")
        print("5.  Exit App")
        choice=input("enter choice here: ")
        if(choice=='1'):
            list_all_videos(videos)
        elif(choice=='2'):
            add_video(videos)
        elif(choice=='3'):
            update_video(videos)
        elif(choice=='4'):
            delete_video(videos)
        elif(choice=='5'):
            break
        else:
            print("INVALID CHOICE")

if __name__ =="__main__":
    main()