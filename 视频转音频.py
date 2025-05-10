# 导入所需的库
import speech_recognition as sr
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# 设置视频的长度（单位为秒）
num_seconds_video = 52 * 60
print("The video is {} seconds".format(num_seconds_video))

# 将视频长度转换为列表
l = list(range(0, num_seconds_video + 1, 60))

# 创建一个字典用于存储每个视频切片的识别结果
diz = {}

# 对视频进行切片并提取音频
for i in range(len(l) - 1):
    # 使用ffmpeg提取视频的每个切片，并将音频保存为.wav文件
    ffmpeg_extract_subclip("大家不必紧张，我本身呢是的汽车维修员。这个扳手呢，是我上螺丝用的，很合理吧？.mp4", l[i] - 2 * (l[i] != 0), l[i + 1], targetname="chunks/cut{}.mp4".format(i + 1))
    clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i + 1))
    clip.audio.write_audiofile(r"converted/converted{}.wav".format(i + 1))

    # 使用Google Speech Recognition识别音频并存储结果
    r = sr.Recognizer()
    audio = sr.AudioFile("converted/converted{}.wav".format(i + 1))
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    diz['chunk{}'.format(i + 1)] = result

# 将识别结果列表存储为文本文件
l_chunks = [diz['chunk{}'.format(i + 1)] for i in range(len(diz))]
text = '\n'.join(l_chunks)

with open('recognized.txt', mode='w') as file:
    file.write("Recognized Speech:\n")
    file.write(text)
    print("Finally ready!")