# 🎭 Celebrity Face Generator  

A deep learning-based application that generates celebrity faces using  Generative Adversarial Network. The project is built using *Streamlit* and deployed on *Streamlit Cloud*.

## 📌 Table of Contents  
- [Overview](#-overview)
- [Dataset Information](#-dataset-information) 
- [Setup & Installation](#-setup--installation)  
- [Usage Instructions](#-usage-instructions)  
- [Deployment Process](#-deployment-process)  
- [Project Submission Requirements](#-project-submission-requirements)  
- [Contributors](#-contributors)
- [Contact Details](#-contact) 

---

## 🔍 Overview  
The *Celebrity Face Generator* is an AI-powered application that creates synthetic celebrity-like faces. It utilizes a trained deep learning model to generate high-quality images.  

---

## 📂 Dataset Information  
- The model is trained on **[CelebA]** (https://www.kaggle.com/datasets/jessicali9530/celeba-dataset).
- Download dataset from above link.
- It will be downloaded in ZIP format,Extract it.
- Move the folder img_align_celeba to project directory.


---
## ⚙ Setup & Installation  

### ➡ Clone the Repository  
```bash
git clone https://github.com/srikanth-maganti/Celebrity-Face-Generator.git
cd celebrity-face-generator
```

### ✅ Create a Virtual Environment (Optional but Recommended)  
```bash
conda create -n <env_name> python=3.12
conda activate <env_name>
```

### 💾 Install Dependencies  
```bash
pip install -r requirements.txt
```

### 🌐 Run the Application  
```bash
streamlit run app.py
```

---

## 🚀 Usage Instructions  
1. Open the deployed Streamlit app in your browser.
2. Select No of Images you want to generate
3. Click on the **Generate Face** button to create a synthetic celebrity face.
4. Download or save the generated image.

---

## 🌍 Deployment Process  

### Step 1: Train and Save the Model  
- Train the model on the dataset.
- Save it as a `.pth`  file in the project directory.

### Step 2: Create a Streamlit App  
- The main application logic is in `app.py`.
- Ensure the script correctly loads the trained model and generates outputs.

### Step 3: Push the Project to GitHub  
Ensure your project includes:
- ✅ `app.py` (Main application script)
- ✅ `requirements.txt` (Dependencies)
- ✅ `README.md` (Documentation)
- ✅ Trained model file

Push your project to GitHub using:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### Step 4: Deploy on Streamlit Cloud  
1. Go to **Streamlit Cloud**.
2. Create a new app and connect your GitHub repository.
3. Select `app.py` as the entry point.
4. Click **Deploy** and wait for it to go live!

📌 **Make sure the deployed app is publicly accessible.**

---





## 👨‍💻 Contributors 
### Team ReLU
- **Srikanth Maganti** - [GitHub Profil](https://github.com/srikanth-maganti)
- **Veneeth Batchu**   -[GitHub Profile](https://github.com/IAMVENEETH)
- **Chaitanya Kallepalli** -[GitHub Profile]()

---


---

## 📢 Additional Notes  
- This project follows the hackathon guidelines for proper conduct, project submission, and deployment documentation.
- Judges can interact with the model through the publicly accessible Streamlit app.

---



