import subprocess
import sys
import webbrowser
from datetime import timedelta

import requests
import stslib
from stslib import cfg

def runffmpeg(arg):
    cmd = ["ffmpeg","-hide_banner","-y"]
    # if cfg.devtype =='cuda':
    #     cmd.extend(["-hwaccel", "cuda","-hwaccel_output_format","cuda"])
    cmd = cmd + arg
    p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=0 if sys.platform != 'win32' else subprocess.CREATE_NO_WINDOW)
    while True:
        try:
            #等待0.1未结束则异常
            outs, errs = p.communicate(timeout=0.5)
            errs=str(errs)
            if errs:
                errs = errs.replace('\\\\','\\').replace('\r',' ').replace('\n',' ')
                errs=errs[errs.find("Error"):]
            # 成功
            if p.returncode==0:
                return "ok"
            # 失败
            # if cfg.devtype=='cuda':
            #     errs+="[error] Please try upgrading the graphics card driver and reconfigure CUDA"
            return errs
        except subprocess.TimeoutExpired as e:
            # 如果前台要求停止
            pass
        except Exception as e:
            #出错异常
            errs=f"[error]ffmpeg:error {cmd=},\n{str(e)}"
            return errs
def checkupdate():
    try:
        res=requests.get("https://raw.githubusercontent.com/jianchang512/sts/main/version.json")
        if res.status_code==200:
            d=res.json()
            if d['version_num']>stslib.VERSION:
                cfg.updatetips=f'New version {d["version"]}'
    except Exception as e:
        pass

def openweb(web_address):
    try:
        webbrowser.open("http://"+web_address)
        print(f"\n{cfg.transobj['lang8']} http://{web_address}")
    except Exception:
        pass

def ms_to_time_string(*, ms=0, seconds=None):
    # 计算小时、分钟、秒和毫秒
    if seconds is None:
        td = timedelta(milliseconds=ms)
    else:
        td = timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 1000

    # 格式化为字符串
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    return time_string