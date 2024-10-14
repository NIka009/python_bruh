#from chai aur code
import json 


def load_videos():
    try:
       with  open("youtube.txt", 'r') as file:
          return json.load(file)#loads the file and returns it
    except FileNotFoundError:
            return []

def save_videos(videos):
    with open("youtube.txt" ,'w') as file:
        json.dump(videos, file)# changes the original file 

def add_videos(videos):
    name= input("Enter video name: ")
    time= input("Enter video time: ")
    print("\n")
    videos.append({'name':name , 'time': time})
    save_videos(videos)
def update_videos(videos):
        List_videos(videos)
        index=int(input("Choose a video to be updated."))
        if 1<= index <= len(videos):
            name= input("Update video name: ")
            time= input("Update video time: ")
            videos[index-1]={'name':name ,'time':time}
        else: print("Invalid index selected")
            
        save_videos(videos)
def Delete_videos(videos):
        index=int(input("Choose a video number to be Deleted."))
        if 1<= index <= len(videos):
            del videos[index-1]
            save_videos(videos)
        else:
            print("Invalid syntax selected")

def List_videos(videos):
    print("\n")
    print("*"*70)
    for index , video in enumerate(videos, start=1):
        print(f"{index}.{video['name']},{video['time']} ")
        print("\n")
        print("*"*70)



def main():
    videos=load_videos()
    while True:
        print('Welcome To Youtube Manager')
        print("1.List all Videos.")
        print("2.Add Videos.")
        print("3.Update Videos.")
        print("4.Delete Videos.")
        print("5.Exit the app")
        char=int(input("Choose an option. "))
        
        
        match char:
            case 1:
                List_videos(videos)
            case 2:
                add_videos(videos)    
            case 3:
                update_videos(videos)    
            case 4:
                Delete_videos(videos)
            case 5:
                break
            case _:
                print("Invalid Choice")
            
        
            
            
    
if __name__=="__main__":
    main()
    