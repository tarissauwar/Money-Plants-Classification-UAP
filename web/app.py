import streamlit as st
from klasifikasi_citra import load_models, predict, class_labels
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the models
vgg16_model, vgg19_model = load_models()

def main():
    st.set_page_config(page_title="Money Plant Disease Prediction", layout="wide")

    # Header with a background image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d2");
            background-size: cover;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Sidebar menu
    with st.sidebar:
        st.image("https://i.pinimg.com/originals/ff/d9/b4/ffd9b46366e14141790a80d4922485bf.gif", width=150)  # Your logo
        st.title("Select Options")
        selected_model = st.radio("Choose a Model:", ('VGG16', 'VGG19'))
        model = vgg16_model if selected_model == 'VGG16' else vgg19_model
        st.info("Tip: VGG16 is lighter; VGG19 may take longer.")

    # Main Title
    st.title("🌿 Money Plant Disease Prediction AI")
    st.write("Upload images of money plants to identify their condition and get predictions.")

    # Multi-upload images
    uploaded_files = st.file_uploader(
        "Upload Images (JPG, JPEG, PNG)", 
        accept_multiple_files=True, 
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_files:
        st.write("### Uploaded Images and Predictions:")
        all_predictions = []  # For collecting data for the table and graph
        
        for idx, uploaded_file in enumerate(uploaded_files):
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

            # Perform predictions
            # Perform predictions
            with st.spinner("Analyzing..."):
                predictions = predict(image, model)  # Modify predict to return probabilities directly
                if len(predictions) == 0:
                    st.error("Error occurred during prediction.")
                    continue

                predicted_class = class_labels[np.argmax(predictions)]
                confidence = float(np.max(predictions))  # Ensure confidence is numeric
                all_predictions.append({"Image": uploaded_file.name, "Class": predicted_class, "Confidence": confidence})
                
                # Display prediction results for each image
                st.success(f"**Predicted Class:** {predicted_class}")
                st.info(f"**Confidence:** {confidence:.2f}")
        
        # Show prediction results in a table
        st.write("### Summary Table:")
        df_predictions = pd.DataFrame(all_predictions)
        st.dataframe(df_predictions)

        # Visualize confidence for each class in a bar chart
        st.write("### Confidence Distribution:")
        class_wise_scores = {label: 0 for label in class_labels}  # Initialize all scores to zero
        for predictions in all_predictions:
            class_wise_scores[predictions["Class"]] += predictions["Confidence"]

        # Plot bar chart
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(class_wise_scores.keys(), class_wise_scores.values(), color="lightgreen")
        ax.set_title("Confidence Scores by Class", fontsize=16)
        ax.set_xlabel("Classes", fontsize=12)
        ax.set_ylabel("Confidence", fontsize=12)
        st.pyplot(fig)

    # Footer section
    st.markdown("---")
    st.markdown(
        """  
        Powered by Streamlit and TensorFlow.
        """
    )

if __name__ == "__main__":
    main()