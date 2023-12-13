# from datetime import datetime
# import moviepy.editor as mp 
# import speech_recognition as sr 
# import os
# import soundfile as sf
# import sys


# def convert_to_wav(input_file, output_file):
#     data, sample_rate = sf.read(input_file)
#     sf.write(output_file, data, sample_rate, format="WAV")

# def audio_to_text(audio_file):
#     r = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio_data = r.record(source)
#     # text_file_name = f"output_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

#     try:
#         audio_text = r.recognize_google(audio_data)
#         print("\nThe resultant text from audio is from python: \n")
#         with open("recognized_text.txt", "w") as text_file:
#             text_file.write(audio_text)
#     except sr.UnknownValueError:
#         print("Google Web API could not understand the audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Web API; {0}".format(e))
#         return audio_to_text

# if __name__ == "__main__":
#     file_path = sys.argv[1]
#     print(file_path)
#     # if is_audio_file(file_path):
#     input_file='audio.mp3'
#     output_file = "output.wav"
#     convert_to_wav(file_path, output_file)
#     text=audio_to_text(output_file)
#     print("its my")
#     print(text)
#     # elif is_video_file(file_path):
#         # video_to_text(file_path)
# else:
#     print(f"is neither an audio nor a video file.")



# from datetime import datetime
# import os
# import sys
# import soundfile as sf
# import speech_recognition as sr
# import moviepy.editor as mp

# def aud_vid_to_text(filename):
#     def is_audio_file(filename):
#         audio_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.aac']
#         file_extension = os.path.splitext(filename)[1].lower()
#         return file_extension in audio_extensions

#     def is_video_file(filename):
#         video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
#         file_extension = os.path.splitext(filename)[1].lower()
#         return file_extension in video_extensions

#     def convert_to_wav(filename, output_file):
#         data, sample_rate = sf.read(filename)
#         sf.write(output_file, data, sample_rate, format="WAV")

#     if is_audio_file(filename):
#         output_file = "output.wav"
#         convert_to_wav(filename, output_file)
#         r = sr.Recognizer()

#         # Recognize speech from the audio file
#         with sr.AudioFile(output_file) as source:
#             audio_data = r.record(source)

#         # Convert audio to text using Google Web API
#         try:
#             audio_text = r.recognize_google(audio_data)
#             with open("recognized_text.txt", "w") as text_file:
#                 text_file.write(audio_text)
#         except sr.UnknownValueError:
#             print("Google Web API could not understand the audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Web API; {e}")
#             # return aud_vid_to_text
#     elif is_video_file(filename):
#         video = mp.VideoFileClip(filename)

#         # Extract the audio from the video
#         audio_file = "output.wav"
#         video.audio.write_audiofile(audio_file)

#         # Initialize recognizer
#         r = sr.Recognizer()

#         # Load the audio file
#         with sr.AudioFile(audio_file) as source:
#             audio_data = r.record(source)

#         # Convert audio to text using Google Web API
#         try:
#             audio_text = r.recognize_google(audio_data)        
#             with open("recognized_text.txt", "w") as text_file:
#                 text_file.write(audio_text)
#         except sr.UnknownValueError:
#             print("Google Web API could not understand the audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Web API; {e}")
#             # return aud_vid_to_text

# if __name__ == "__main__":
#     file_path = sys.argv[1]
#     res = aud_vid_to_text(file_path)
# else:
#     print(f"is niether file or audio")


from datetime import datetime
import os
import sys
import soundfile as sf
import speech_recognition as sr
import moviepy.editor as mp


def aud_vid_to_text(filename):
    def is_audio_file(filename):
        audio_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.aac']
        file_extension = os.path.splitext(filename)[1].lower()
        return file_extension in audio_extensions

    def is_video_file(filename):
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
        file_extension = os.path.splitext(filename)[1].lower()
        return file_extension in video_extensions

    def convert_to_wav(filename, output_file):
        data, sample_rate = sf.read(filename)
        sf.write(output_file, data, sample_rate, format="WAV")

    if is_audio_file(filename):
        output_file = "output.wav"
        convert_to_wav(filename, output_file)
        r = sr.Recognizer()

        # Recognize speech from the audio file
        with sr.AudioFile(output_file) as source:
            audio_data = r.record(source)

        # Convert audio to text using Google Web API
        try:
            audio_text = r.recognize_google(audio_data)
            with open("recognized_text.txt", "w") as text_file:
                text_file.write(audio_text)
                exit(0)
            # Return the recognized text
        except sr.UnknownValueError:
            print("Google Web API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web API; {e}")
    elif is_video_file(filename):
        video = mp.VideoFileClip(filename)

        # Extract the audio from the video
        audio_file = "output.wav"
        video.audio.write_audiofile(audio_file)

        # Initialize recognizer
        r = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

        # Convert audio to text using Google Web API
        try:
            audio_text = r.recognize_google(audio_data)
            with open("recognized_text.txt", "w") as text_file:
                text_file.write(audio_text) 
                exit(0)# Return the recognized text
        except sr.UnknownValueError:
            print("Google Web API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web API; {e}")

if __name__ == "__main__":
    file_path = sys.argv[1]
    # file_path = "video.mp4"
    res = aud_vid_to_text(file_path)
    print(res)
    exit(0)