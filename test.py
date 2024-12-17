import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the trained model
model = load_model('Models/best_model.h5')

# Function to make predictions
def predict_defect(image_path, model):
    # Load and preprocess the image
    test_image = load_img(image_path, target_size=(64, 64), color_mode='grayscale')
    test_image = img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    # Predict using the model
    result = model.predict(test_image)
    if result[0] <= 0.5:
        return 'Defective!'
    else:
        return 'Not Defective!'

# Streamlit App
st.title("Cast Defect Classification of Pump Impeller")
st.write("Upload an image of the casted metal to classify whether it is defective or not.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    
    # Save the uploaded file locally
    with open("uploaded_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Make prediction
    with st.spinner("Classifying..."):
        prediction = predict_defect("uploaded_image.jpg", model)
    st.success(f"Prediction is: {prediction}")
    
st.markdown("""
---
**Developed by Raghunandan M S & Kailas E K**
""")
