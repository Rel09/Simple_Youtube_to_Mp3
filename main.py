from pytube import YouTube
import easygui, os

if __name__ == '__main__':
    while True:

        #Opening the app
        output = easygui.enterbox("Enter the youtube link", "Rel_Youtube to Mp3")
        if output:

            # Open youtube link as YT
            yt = YouTube(output, on_complete_callback=print("Done"))

            # Extract Audio
            video = yt.streams.filter(only_audio=True).first()

            # Save the files
            out_file = video.download(output_path="")

            # Split the name and the file extension to actually changes it
            x, _y = os.path.splitext(out_file)

            # Set variable to rename file
            new_file = x + '.mp3'

            # If the file already exist, delete it
            if os.path.exists(new_file):
                os.remove(new_file)

            # Rename the file
            os.rename(out_file, new_file)

            # Completed message box
            easygui.msgbox(yt.title + " has been successfully downloaded.")

        #if the user closed the app
        else: break

