import locale
import os
import sys
import torch
import re
ROOT_DIR = os.getcwd()

def parse_ini(file=os.path.join(ROOT_DIR,'set.ini')):
    sets={
        "web_address":"127.0.0.1:9977", 
        "lang":"en" if locale.getdefaultlocale()[0].split('_')[0].lower() != 'zh' else "zh", 
        "devtype":"cpu", 
        "cuda_com_type":"int8",
        "beam_size":1,
        "best_of":1,
        "vad":True,
        "temperature":0,
        "condition_on_previous_text":False,
        "initial_prompt_zh":"转录为中文简体。"

    }
    if not os.path.exists(file):
        return sets
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip() or line.strip().startswith(";") :
                continue
            line=[ x.strip() for x in line.strip().split('=', maxsplit=1)]
            if len(line)!=2:
                continue
            if line[1]=='false':
                sets[line[0]] = False
            elif line[1]=='true':
                sets[line[0]] = True
            elif re.match(r'^\d+$', line[1]):
                sets[line[0]]=int(line[1])
            elif line[1]:
                sets[line[0]]=str(line[1]).lower()
    return sets

sets=parse_ini()
print(sets)
web_address=sets.get('web_address')
LANG=sets.get('lang')
devtype=sets.get('devtype')
cuda_com_type=sets.get('cuda_com_type')



MODEL_DIR = os.path.join(ROOT_DIR, 'models')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
TMP_DIR = os.path.join(STATIC_DIR, 'tmp')

progressbar={}
progressresult={}


if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR, 0o777, exist_ok=True)
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR, 0o777, exist_ok=True)
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, 0o777, exist_ok=True)

if sys.platform == 'win32':
    os.environ['PATH'] = f'{ROOT_DIR};{ROOT_DIR}\\ffmpeg;' + os.environ['PATH']
else:
    os.environ['PATH'] = f'{ROOT_DIR}:{ROOT_DIR}/ffmpeg:' + os.environ['PATH']
language_code_list={
    "zh":{
        "中文": ['zh'],
        "英语": ['en'],
        "法语": ['fr'],
        "德语": ['de'],
        "日语": ['ja'],
        "韩语": ['ko'],
        "俄语": ['ru'],
        "西班牙语": ['es'],
        "泰国语": ['th'],
        "意大利语": ['it'],
        "葡萄牙语": ['pt'],
        "越南语": ['vi'],
        "阿拉伯语": ['ar'],
        "土耳其语": ['tr'],
        "匈牙利": ['hu'],
    },
    "en":{
        "Chinese": ['zh'],
        "English": ['en'],
        "French": ['fr'],
        "German": ['de'],
        "Japanese": ['ja'],
        "Korean": ['ko'],
        "Russian": ['ru'],
        "Spanish": ['es'],
        "Thai": ['th'],
        "Italian": ['it'],
        "Portuguese": ['pt'],
        "Vietnamese": ['vi'],
        "Arabic": ['ar'],
        "Turkish": ['tr'],
        "Hungarian": ['hu'],
    }
}

langlist = {
    "zh": {
        "lang1": "上传成功",
        "lang2": "上传失败",
        "lang3": "上传失败：不允许上传该格式",
        "lang4": "模型文件不存在,请下载后放到 models 目录下",
        "lang5": "文件不存在",
        "lang6": "识别成功",
        "lang7": "识别失败",
        "lang8": "浏览器已打开，若未能自动打开，请手动打开网址 ", 
        "lang9":"已转为wav格式"
    },
    "en": {
        "lang1": "Upload successful",
        "lang2": "Upload failed",
        "lang3": "Upload failed: Uploading this format is not allowed",
        "lang4": "Model file does not exist,download and save to models folder",
        "lang5": "File does not exist",
        "lang6": "recognition successful",
        "lang7": "recognition failed",
        "lang8": "The browser is open. If it does not open automatically, please open the URL manually", 
        "lang9":"Converted to wav"
    }
}
updatetips = ""
transobj = langlist[LANG]
lang_code=language_code_list[LANG]


