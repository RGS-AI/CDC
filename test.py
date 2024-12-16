import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the trained model
model = load_model('../CDCApp/Models/cdcmodel.keras')

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

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
        return 'Defective'
    else:
        return 'Not Defective'

# Streamlit App
st.title("Casting Defect Classification")
st.write("Upload an image of the casted metal to classify whether it is defective or not.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    st.write("Classifying...")
    # Save the uploaded file locally
    with open("uploaded_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Make prediction
    prediction = predict_defect("uploaded_image.jpg", model)
    st.write(f"Prediction is: {prediction}")
    
    
st.write("Authored by: Raghunandan M S & Kailas E K")