[Discord](https://discord.gg/TMCM2PfHzQ) / Q群 902124277

# 语音识别转文字工具

这是一个离线运行的本地语音识别转文字工具，基于 openai-whipser 开源模型，可将视频/音频中的人类声音识别并转为文字，可输出json格式、srt字幕带时间戳格式、纯文字格式。可用于自行部署后替代 openai 的语音识别接口或百度语音识别等，准确率基本等同openai官方api接口。

> 
> 部署或下载后，双击 start.exe 自动调用本地浏览器打开本地网页。
>
> 拖拽或点击选择要识别的音频视频文件，然后选择发声语言、输出文字格式、所用模型(已内置base模型),点击开始识别，识别完成后以所选格式输出在当前网页。
>
> 全过程无需联网，完全本地运行，可部署于内网
>
> openai-whisper 开源模型有 base/small/medium/large/large-v3, 内置base模型，base->large-v3识别效果越来越好，但所需计算机资源也更多，根据需要可自行下载后放到 models 目录下即可。
>
> [全部模型下载地址](https://github.com/jianchang512/stt/releases/tag/0.0)
>


# 视频演示


https://github.com/jianchang512/stt/assets/3378335/d716acb6-c20c-4174-9620-f574a7ff095d




![image](https://github.com/jianchang512/stt/assets/3378335/0f724ff1-21b3-4960-b6ba-5aa994ea414c)




# 预编译Win版使用方法/Linux和Mac源码部署

1. [点击此处打开Releases页面下载](https://github.com/jianchang512/stt/releases)预编译文件

2. 下载后解压到某处，比如 E:/stt

3. 双击 start.exe ，等待自动打开浏览器窗口即可

4. 点击页面中的上传区域，在弹窗中找到想识别的音频或视频文件，或直接拖拽音频视频文件到上传区域，然后选择发生语言、文本输出格式、所用模型，点击“立即开始识别”，稍等片刻，底部文本框中会以所选格式显示识别结果

5. 如果机器拥有英伟达GPU，并正确配置了CUDA环境，将自动使用CUDA加速


# 源码部署(Linux/Mac/Window)

0. 要求 python 3.9->3.11

1. 创建空目录，比如 E:/stt, 在这个目录下打开 cmd 窗口，方法是地址栏中输入 `cmd`, 然后回车。

	使用git拉取源码到当前目录 ` git clone git@github.com:jianchang512/stt.git . `

2. 创建虚拟环境 `python -m venv venv`

3. 激活环境，win下命令 `%cd%/venv/scripts/activate`，linux和Mac下命令 `source ./venv/bin/activate`

4. 安装依赖: `pip install -r requirements.txt`,如果报版本冲突错误，请执行 `pip install -r requirements.txt --no-deps`

5. win下解压 ffmpeg.7z，将其中的`ffmpeg.exe`和`ffprobe.exe`放在项目目录下, linux和mac 到 [ffmpeg官网](https://ffmpeg.org/download.html)下载对应版本ffmpeg，解压其中的`ffmpeg`和`ffprobe`二进制程序放到项目根目录下

6. [下载模型压缩包](https://github.com/jianchang512/stt/releases/tag/0.0)，根据需要下载模型，下载后将压缩包里的 xx.pt 文件放到项目根目录的 models 文件夹内

7. 执行  `python  start.py `，等待自动打开本地浏览器窗口。



# CUDA 加速支持

**安装CUDA工具**

如果你的电脑拥有 Nvidia 显卡，先升级显卡驱动到最新，然后去安装对应的 
   [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-downloads)  和  [cudnn for CUDA11.X](https://developer.nvidia.com/rdp/cudnn-archive)。
   
   安装完成成，按`Win + R`,输入 `cmd`然后回车，在弹出的窗口中输入`nvcc --version`,确认有版本信息显示，类似该图
   ![image](https://github.com/jianchang512/pyvideotrans/assets/3378335/e68de07f-4bb1-4fc9-bccd-8f841825915a)

   然后继续输入`nvidia-smi`,确认有输出信息，并且能看到cuda版本号，类似该图
   ![image](https://github.com/jianchang512/pyvideotrans/assets/3378335/71f1d7d3-07f9-4579-b310-39284734006b)

    然后执行 `python testcuda.py`，如果提示成功，说明安装正确，否则请仔细检查重新安装

# 注意事项

0. 如果没有英伟达显卡或未配置好CUDA环境，不要使用 large/large-v3 模型，可能导致内存耗尽死机
1. 中文在某些情况下会输出繁体字

# 致谢

本项目主要依赖的其他项目

1. https://github.com/openai/whipser
2. https://github.com/pallets/flask
3. https://ffmpeg.org/
4. https://layui.dev

