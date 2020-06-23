from twitter import Twitter
import time
from media import Media

tw = Twitter()
media = Media()
def start():
    print("Starting...")
    dms = list()
    while True:
        if len(dms) != 0:
            print(len(dms))
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                screen_name = tw.get_user_screen_name(sender_id)
                id = dms[i]['id']
                if screen_name != "nyobafhp" and "mf" in message:
                    file = open("list.txt", "a")

                    if len(message) != 0 and len(message) <= 500:
                        if "https://" not in message and "http://" not in message:
                            if "--s" in message:
                                message = message.replace("--s", "")
                                tw.post_tweet(message)
                                print("somethinga")
                                tw.delete_dm(id)
                                file.write("(" + screen_name + ", " + id + ", " + message + ")\n")

                            else:
                                tw.post_tweet(message)
                                print("somethingb   ")
                                tw.delete_dm(id)
                                file.write("(" + screen_name + ", " + id + ", " + message + ")\n")
                        else:
                            tw.delete_dm(id)
                    file.close()
                else:
                    tw.delete_dm(id)

            dms = list()

        else:
            print("DM is empty")
            dms = tw.read_dm()
            if len(dms) == 0:
                # time.sleep(60)
                break


if __name__ == "__main__":
    start()