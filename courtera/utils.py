from transformers import BertTokenizer
import tensorflow as tf
from transformers import TFBertModel

from transformers import BertTokenizer
from tensorflow import keras
from huggingface_hub import hf_hub_download
# Load tokenizer directly from repo
tokenizer = BertTokenizer.from_pretrained("EyadAmgad/bert_h5_tokenizer")

# Load model
model = keras.models.load_model(
    hf_hub_download("EyadAmgad/bert_h5_tokenizer", "bert_model.h5"),
    custom_objects={"TFBertModel": TFBertModel}
)
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="tf", padding='max_length', truncation=True, max_length=128)
    outputs = model([inputs["input_ids"], inputs["attention_mask"]])
    prediction = tf.argmax(outputs, axis=1).numpy()[0]
    return int(prediction) + 1
