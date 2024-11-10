from RealtimeSTT import AudioToTextRecorder
from hf_hub_ctranslate2 import MultiLingualTranslatorCT2fromHfHub
from transformers import AutoTokenizer
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

model = MultiLingualTranslatorCT2fromHfHub(
    model_name_or_path="michaelfeil/ct2fast-m2m100_1.2B", device="cpu", compute_type="int8_float32",
    tokenizer=AutoTokenizer.from_pretrained(f"facebook/m2m100_1.2B")
)

def process_text(text):
    cls()
    print("\n" + text + "\n")
    outputs = model.generate(
        [text],
        src_lang=["en"],
        tgt_lang=["tr"]
    )
    print("\n" + outputs[0] + "\n")

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(post_speech_silence_duration=0.1)

    while True:
        recorder.text(process_text)