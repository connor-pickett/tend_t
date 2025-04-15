## Python 3.11.7 ##

## mp4 ##

# load libraries
import os
import whisper
import moviepy.editor as mpe

# load whisper model
print("Loading Whisper model...")
model = whisper.load_model("medium")

# change directory pathname here below
directory = '###'
os.chdir(directory)
print(f"Changed directory to: {directory}")

# convert .m4v to mp3
print("Converting .mp4 files to .mp3...")
for file in os.listdir():
    if file.endswith(".mp4"):
        try:
            print(f"Processing video file: {file}")
            video = mpe.VideoFileClip(file)
            audio = video.audio
            audio_filename = os.path.splitext(file)[0] + ".mp3"
            audio.write_audiofile(audio_filename)
            audio.close()
            video.close()
            
            print(f"Converted {file} to {audio_filename}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

# transcribe .mp3 files
print("Transcribing .mp3 files...")
for file in os.listdir():
    if file.endswith(".mp3"):
        try:
            print(f"Transcribing audio file: {file}")
            result = model.transcribe(file, fp16=False)
            with open(f"{file}.txt", "w") as f:
                f.write(result["text"])
            print(f"Transcription for {file} completed")
        except Exception as e:
            print(f"Error transcribing {file}: {e}")

# enjoy :3!
print("Transcribed successfully!")