import torch
import torch.nn as nn
import matplotlib.pyplot as plt

#parameters
num_channels = 3
latent_vector = 100
num_gen_features = 64
ngpu = 1

#generator class
class Generator(nn.Module):
    def __init__(self, ngpu):
        super(Generator, self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            
            nn.ConvTranspose2d( latent_vector, num_gen_features * 8, kernel_size=4, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(num_gen_features * 8),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(num_gen_features * 8, num_gen_features * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(num_gen_features * 4),
            nn.ReLU(True),
           
            nn.ConvTranspose2d( num_gen_features * 4, num_gen_features * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(num_gen_features * 2),
            nn.ReLU(True),
            
            nn.ConvTranspose2d( num_gen_features * 2, num_gen_features, 4, 2, 1, bias=False),
            nn.BatchNorm2d(num_gen_features),
            nn.ReLU(True),
           
            nn.ConvTranspose2d( num_gen_features, num_channels, 4, 2, 1, bias=False),
            nn.Tanh()
            
        )

    def forward(self, input):
        return self.main(input)


#generation
def generate(num_img):
    #loading  model
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    netG = Generator(latent_vector).to(device)
    checkpoint = torch.load("gan_trained.pth", map_location=device)
    netG.load_state_dict(checkpoint['generator_state_dict'])
    # print("Trained Generator loaded successfully!")


    netG.eval()  
    noise = torch.randn(num_img, latent_vector, 1, 1, device=device)


    with torch.no_grad():
        gen_images = netG(noise).cpu().detach().numpy()

    return gen_images

    
