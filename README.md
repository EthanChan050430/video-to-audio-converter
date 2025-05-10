# 视频转音频与语音识别工具

这是一个简单的Python工具，用于将视频文件转换为音频并使用Google Speech Recognition进行语音识别，将识别结果保存为文本文件。

## 功能特点

- 将视频文件切分为较小的片段
- 从视频片段中提取音频（WAV格式）
- 使用Google Speech Recognition API进行语音识别
- 将识别结果合并并保存为文本文件

## 使用要求

- Python 3.x
- 以下Python库：
  - speech_recognition
  - moviepy

## 安装依赖

```bash
pip install SpeechRecognition moviepy
```

## 使用方法

1. 确保你的视频文件放在同一目录下
2. 修改脚本中的视频文件名
3. 确保有`chunks`和`converted`两个子目录用于存储临时文件
4. 运行脚本：

```bash
python 视频转音频.py
```

5. 识别结果将保存在`recognized.txt`文件中

## 注意事项

- 识别准确率取决于Google Speech Recognition的支持语言及音频质量
- 对于较长的视频文件，识别过程可能需要较长时间