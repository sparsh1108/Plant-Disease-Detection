import streamlit as st
import requests


st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱"
)


st.title("🌱 Plant Disease Detection")
st.write("Upload a plant leaf image to detect its disease.")


uploaded_file = st.file_uploader(
    "Choose a plant leaf image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Predict Disease"):

        with st.spinner("Analyzing image..."):

            response = requests.post(
                "https://plant-disease-detection-3-uvki.onrender.com/predict",
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed!")

            st.subheader("Prediction")

            st.write(
                f"🌿 **{result['disease']}**"
            )

            confidence = result["confidence"]

            st.write(
                f"**Confidence:** {confidence * 100:.2f}%"
            )

            st.progress(confidence)

        else:

            st.error(
                f"Prediction failed: {response.text}"
            )




