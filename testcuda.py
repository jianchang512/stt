import torch

if torch.cuda.is_available():
    print('CUDA 可用，如果实际使用仍提示 cuda 相关错误，请尝试升级显卡驱动\n将 set.init 中 devtype=cpu改为devtype=cuda')
else:
    print("当前计算机CUDA不可用")