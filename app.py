import streamlit as st
from PIL import Image,ImageEnhance
from torchvision import transforms
import matplotlib.pyplot as plt
from generation import generate
import numpy as np
import io
import zipfile



st.set_page_config(page_title="CREATIVE AI", layout="wide")
st.title("Celeb Face Generator using GAN")
st.markdown("""
This app uses a Generative Adversarial Network (GAN) to create synthetic images.
""")


num_images = st.slider("Number of Images", 2, 16, 4)


def ndarray_to_image(ndarr):
    ndarr = (ndarr + 1) / 2.0
    ndarr = np.clip(ndarr, 0, 1)
    if ndarr.ndim == 4 and ndarr.shape[0] == 1:
        ndarr = np.squeeze(ndarr, axis=0)
    if ndarr.ndim == 3 and ndarr.shape[0] <= 4: 
        ndarr = ndarr.transpose(1, 2, 0)
    img = Image.fromarray((ndarr * 255).astype(np.uint8))
    return img

if st.button("Generate Images"):
    with st.spinner("Generating images..."):
        gen_images = generate(num_images)
        cols = 4
        rows = (num_images + cols - 1) // cols
        
        fig, axs = plt.subplots(rows, cols, figsize=(12, 3 * rows))
        axs = axs.flatten() if num_images > 1 else [axs]
        for img_idx, img in enumerate(gen_images):
            if img_idx < len(axs):
                img = img.transpose(1, 2, 0) 
                img = (img - img.min()) / (img.max() - img.min())
                pil_image = ndarray_to_image(img)
                enhance_img = pil_image.resize((100,100),Image.BICUBIC)
                enhancer = ImageEnhance.Contrast(enhance_img)
                enhanced_img = enhancer.enhance(2.0)
                axs[img_idx].imshow(enhanced_img)
                axs[img_idx].set_title(f"Image {img_idx+1}")
                axs[img_idx].axis("off")
        
      
        for i in range(num_images, len(axs)):
            axs[i].axis("off")
            
        plt.tight_layout()
        st.pyplot(fig)
        
         # Option to download images
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for img_idx, image_array in enumerate(gen_images):
                pil_image = ndarray_to_image(image_array)
            
                img_bytes = io.BytesIO()
                pil_image.save(img_bytes, format="PNG")
                img_bytes.seek(0)
                zip_file.writestr(f"gan_generated_{img_idx+1}.png", img_bytes.getvalue())

        zip_buffer.seek(0)
        st.subheader("Download All Images")
        st.download_button(
            label="Download All Images as ZIP",
            data=zip_buffer,
            file_name="generated_images.zip",
            mime="application/zip",
            use_container_width=True
        )
