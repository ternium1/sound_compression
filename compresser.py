import ffmpeg, os, time
from matplotlib import pyplot as plt
#GSM bitrate: 13kbit/s
bitrates = ["8k", "16k", "32k", "64k", "96k", "128k", "160k", "192k"] #kbit/s
file_names = []
file_sizes = []

input_file = ffmpeg.input("uncompressed.wav", f="wav")
start = time.perf_counter()
for i in bitrates:
    filename = f'{i}bps.mp3'
    ffmpeg.output(input_file.audio, filename, f="mp3", audio_bitrate=i).run()
    file_names.append(filename)
    f_size = os.stat(filename).st_size / 1000
    file_sizes.append(f_size)
    print(f"Successfully encoded file using {i}kbit/s bitrate. Filename: {filename} ;; size: {f_size}")
end = time.perf_counter()
print(f"finished compression job in {end - start}s") 

plt.plot(bitrates, file_sizes)  

plt.show()
