import tensorflow as tf
from transformers import TFAutoModel
import gdown
import streamlit as st

file_id = '1WsXgYeELEsMmrIOOZmfEYJWZbCg2wl-l'

url = f'https://drive.google.com/uc?id={file_id}'

output = "Projects/BERTDeployment/bert_model.h5"

gdown.download(url, output = output, quiet=False)

bert = TFAutoModel.from_pretrained("bert-base-uncased")
# model_path = "Projects/BERTDeployment/bert_model.h5"
# model = tf.keras.models.load_model(model_path, custom_objects={'TFBertMainLayer': bert.bert})
# print(model.summary())

def app():
    st.text("Success")