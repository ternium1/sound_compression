import ffmpeg, os, time
from matplotlib import pyplot as plt
from mosqito.sq_metrics import sharpness_din_st
from mosqito.utils import load

#GSM bitrate: 13kbit/s
bitrates = ["8k", "16k", "32k", "48k", "64k", "96k", "128k", "160k", "192k"] #kbit/s
file_names = []
file_sizes = []
sharpness_din = []
sharpness_aures = []
sharpness_bismarck = []
sharpness_fastl = []

input_file = ffmpeg.input("./uncompressed.wav", f="wav")
start = time.perf_counter()
for i in bitrates:
    filename = f'{i}bps'
    ffmpeg.output(input_file.audio, f'{filename}.mp3', f="mp3", audio_bitrate=i).run() #compress the wave file to the selected bitrate in mp3
    ffmpeg.input(f'{filename}.mp3', f="mp3").output(f'{filename}.wav', f="wav").run() #convert the compressed mp3 file to wav
    file_names.append(filename)
    f_size = os.stat(f'{filename}.mp3').st_size / 1000 #get the mp3 file size in kB
    file_sizes.append(f_size)
    print(f"Successfully encoded file using {i}kbit/s bitrate. Filename: {filename} ;; size: {f_size}")
end = time.perf_counter()
print(f"finished compression job in {end - start}s")
print("File list:")


plt.plot(bitrates, file_sizes)  #plot the file sizes against the bitrate
plt.savefig("size.png")
plt.show()

for i in file_names:
    print(f"Computing sharpness for {i}.wav")
    sig, fs = load(f'{i}.wav', wav_calib=2 * 2 **0.5)
    sharpness_din.append(sharpness_din_st(sig, fs, weighting="din"))
    sharpness_aures.append(sharpness_din_st(sig, fs, weighting="aures"))
    sharpness_bismarck.append(sharpness_din_st(sig, fs, weighting="bismarck"))
    sharpness_fastl.append(sharpness_din_st(sig, fs, weighting="fastl"))

plt.plot(bitrates, sharpness_din, label='DIN sharpness')#plot the sharpness against the bitrate
plt.plot(bitrates, sharpness_aures, label='aures sharpness')#plot the sharpness against the bitrate
plt.plot(bitrates, sharpness_bismarck, label='bismarck sharpness')#plot the sharpness against the bitrate
plt.plot(bitrates, sharpness_fastl, label='fastl sharpness')#plot the sharpness against the bitrate
plt.savefig("sharpness.png")
plt.show()
