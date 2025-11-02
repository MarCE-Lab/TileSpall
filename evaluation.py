import numpy as np 
import os, glob, torch, cv2, json
import torch.nn as nn
import segmentation_models_pytorch_3branch as smp_3b
import albumentations as A
from dataset import SpallingDataset
from albumentations.pytorch import ToTensorV2
from utils import surfd, compute_metrics
from sklearn.model_selection import train_test_split


class Eval:
    def __init__(self, img_path, label_path, save_path, ckpt, device = 'cuda'):
        self.img_path = img_path
        self.label_path = label_path
        self.save_path = save_path
        self.ckpt = ckpt
        self.device = device
    
    def predict(self, image):
        image = image.unsqueeze(0)
        h, w = image.shape[-2:]
        image=image.to(self.device)
        with torch.no_grad():
            output = self.model(image)[1]
            output = torch.argmax(output, dim=1)
            output = output.cpu().squeeze(0).numpy()
        return output
    
    def eval(self):
        hd95_array = []
        pred_array = []
        label_array = []
        test_set = self.get_ds()
        self.model = smp_3b.create_model(arch='MAnet',encoder_name='efficientnet-b6', encoder_weights='imagenet'
                                , classes=2, activation=None, encoder_depth=5, decoder_channels=[256, 128, 64, 32, 16]).to(self.device)
        self.model.load_state_dict(torch.load(self.ckpt))
        self.model.eval()
        for i,test in enumerate(test_set):
            image, label = test
            pred = self.predict(image)
            hd95_array.append(np.percentile(surfd(pred, label.numpy(), 1, 1), 95))
            pred_array+=list(pred.reshape(-1))
            label_array+=list(label.numpy().reshape(-1))
        hd95 = np.array(hd95_array).mean()
        pred_array = np.array(pred_array).reshape(-1)
        label_array = np.array(label_array).reshape(-1)
        metrics_dict = compute_metrics(pred_array, label_array, background=False)
        metrics_dict['hd95'] = hd95
        json.dump(metrics_dict, open(self.save_path, 'w'))
        
    def get_ds(self):
        t_test = A.Compose([A.Resize(864, 864), A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
                ToTensorV2()])
        X = os.listdir(self.img_path)
        _X_train, X_temp = train_test_split(X, test_size=0.2, random_state=0)
        _X_val, X_test = train_test_split(X_temp, test_size=0.5, random_state=0)
        test_set = SpallingDataset(X_test, t_test)
        
        return test_set
        
def main():
    eval = Eval(
            img_path = './spalling_data/image/',
            label_path = './spalling_data/label/',
            save_path = f'./output/performance.json',
            ckpt = './ckpt/best.pt',
        )
    eval.eval()
   
if __name__ == '__main__':
    main()