from pytube import YouTube
from pathlib import Path
from pynput import keyboard

downloads_path = str(Path.home() / "Downloads")

def on_press(key):
	if key == keyboard.Key.enter:
		return False

finish = False
while not(finish):
	print("~~Youtube Video Downloader~~\n")
	url = str(input("Enter video link : "))

	try:
		print("\nProcessing...\n")
		youtube = YouTube(url)
	except:
		print("Video Unknown")

	length = youtube.length

	video = youtube.streams.filter(progressive=True)
	resolutions = [i.resolution for i in video]
	print("Available Resolutions:")
	for i in range (len(resolutions)):
		print(f"\t{i+1}. {resolutions[i]}")

	while(True):
		choice = int(input("\nYour choice : "))
		if (0 < choice <= len(resolutions)):
			break
		elif (choice == -1):
			exit()
		else:
			print("Wrong input! Please try again (Type -1 to exit)\n")
	vid_choice = youtube.streams.get_by_resolution(resolutions[choice-1])

	print("\nVideo Details :")
	print(f"\tVideo Title : \"{youtube.title}\"")
	print(f"\tVideo Author : {youtube.author}")
	if (length >= 3600):
		hour = int(length/3600)
		minute = int((length-hour*3600)/60)
		second = int(length-hour*3600-minute*60)
		length = f"{hour} hour(s) {minute} minute(s) {second} second(s)"
	elif (60 <= length < 3600):
		minute = int(length/60)
		second = int(length-minute*60)
		length = f"{minute} minute(s) {second} second(s)"
	else:
		second = int(length)
		length = f"{second} second(s)"
	print(f"\tVideo Length : {length}")
	print(f"\tVideo Publish Date : {youtube.publish_date}")
	print(f"\tVideo Resolution : {resolutions[choice-1]}")
	print(f"\tVideo Size : {vid_choice.filesize} bytes\n")

	print("Do you want to download this video? (yes/no)")
	while (True):
		confirmation = str(input())
		if (confirmation.lower() == 'y' or confirmation.lower() == 'yes' or confirmation.lower() == 'n' or confirmation.lower() == 'no'):
			break
		else:
			print("Wrong input! Please try again")

	if (confirmation.lower() == 'y' or confirmation.lower() == 'yes'):
		print("\nDo you want to change video's title?")
		while (True):
			confirmation2 = str(input())
			if (confirmation2.lower() == 'y' or confirmation2.lower() == 'yes' or confirmation2.lower() == 'n' or confirmation2.lower() == 'no'):
				break
			else:
				print("Wrong input! Please try again")

		if (confirmation2.lower() == 'yes' or confirmation2.lower() == 'y'):
			new_name = str(input("\nEnter the new video title : "))
			print("\nDownloading...\n")
			vid_choice.download(output_path=downloads_path, filename=new_name)
			print(f"Video has been downloaded on {downloads_path}")
			finish = True
		elif (confirmation2.lower() == 'n' or confirmation2.lower() == 'no'):
			print("\nDownloading...\n")
			vid_choice.download(output_path=downloads_path)
			print(f"Video has been downloaded on {downloads_path}")
			finish = True

	elif (confirmation.lower() == 'n' or confirmation.lower() == 'no'):
		print("\nCancelled\n")
		print("Do you want to exit? (yes/no)")
		while (True):
			out = str(input())
			if (out.lower() == 'y' or out.lower() == 'yes' or out.lower() == 'n' or out.lower() == 'no'):
				break
			else:
				print("Wrong input! Please try again")

		if (out.lower() == 'y' or out.lower() == 'yes'):
			finish = True
		elif (out.lower() == 'n' or out.lower() == 'no'):
			print()

print("\nGoodbye~\n")
print("Press ENTER to exit...")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
