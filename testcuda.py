import torch
from torch.backends import cudnn

if torch.cuda.is_available():
    
    if cudnn.is_available() and cudnn.is_acceptable(torch.tensor(1.).cuda()):
        print('cuda和cudnn 可用')
        print('如果实际使用仍提示 cuda 相关错误，请尝试升级显卡驱动\n将 set.init 中 devtype=cpu改为devtype=cuda')
    else:
        print('cuda可用但cudnn不可用，cuda11.x请安装cudnn8,cuda12.x请安装cudnn9')
        
else:
    print("当前计算机CUDA不可用")
   
input("\n回车关闭")