import tensorflow as tf
from fastapi import FastAPI
from transformers import TFAutoModel
from gd_download import download_file_from_google_drive

app = FastAPI()

# def get_feature_vectors(text, max_len = max_len, padding = "max_length"):
#   tokens = tokenizer(text.numpy().decode(), max_length = max_len, truncation = True, padding = "max_length", add_special_tokens = True, return_tensors = "tf")
#   return (tokens["input_ids"], tokens["attention_mask"])

# def get_feature_map(text, label):
#   input_ids, attention_mask = tf.py_function(get_feature_vectors, inp=[text,], Tout=[tf.int32, tf.int32])
#   input_ids, attention_mask = input_ids[0], attention_mask[0]
#   input_ids.set_shape([max_len])
#   attention_mask.set_shape([max_len])
#   x = {
#       "input_ids": input_ids,
#       "attention_mask": attention_mask
#   }

#   return (x, label)

# def make_dataset(text, labels):
#     dataset = tf.data.Dataset.from_tensor_slices((text, labels))
#     dataset = dataset.map(get_feature_map, num_parallel_calls = tf.data.experimental.AUTOTUNE, deterministic = False)
#     dataset = dataset.batch(batch_size = batch_size, drop_remainder = True, num_parallel_calls = tf.data.AUTOTUNE)
#     dataset = dataset.prefetch(tf.data.AUTOTUNE)
#     return dataset

# Sample Model Class
# class MyModel:
#     def __init__(self, model_path):
#         self.model = tf.keras.models.load_model(model_path)

#     def predict(self, data):
#         input_data = np.array([data])
#         prediction = self.model.predict(input_data)
#         return prediction.tolist()

# class PredictionInput(BaseModel):
#     text: str


download_file_from_google_drive(id = "1WsXgYeELEsMmrIOOZmfEYJWZbCg2wl-l", destination = "Projects/BERTDeployment/")

bert = TFAutoModel.from_pretrained("bert-base-uncased")
model_path = "Projects/BERTDeployment/bert_model.h5"
my_model = tf.keras.models.load_model(model_path, custom_objects={'TFBertMainLayer': bert.bert})

@app.get("/")
def read_root():
    return "Hello World"