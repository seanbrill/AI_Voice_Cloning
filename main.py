#Authors
#Sean Brill 
#James Campbell
#source: https://github.com/suno-ai/bark

from transformers import AutoProcessor, BarkModel
import scipy 

#must use cpu if you do not have a CUDA enabled NVIDIA GPU
#must also set up CUDA
output_dir = './audio_outputs'
proccessor = None
model = None
device = 'cpu' #default to cpu

def useGPU():
    global device
    device = 'cuda:0'

def useCPU():
    global device
    device = 'cpu'


#possible devices
#cpu
#cuda:0
#cuda:1
#cuda:n where n is the gpu index


def generate_audio(text, preset, file_name):
    inputs = proccessor(text, voice_preset=preset)
    for k, v in inputs.items():
        inputs[k] = v.to(device)
    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()
    sample_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(output_dir + '/' + file_name, rate=sample_rate, data=audio_array)

def initialize():
    global proccessor
    global model
    proccessor = AutoProcessor.from_pretrained("suno/bark")
    model = BarkModel.from_pretrained("suno/bark")
    model.to(device)


useGPU()
initialize()

generate_audio(
    text="Hello, what you are hearing is completly AI generated audio.. pretty cool huh!? Lets get coding mother fuckers!",
    preset="v2/en_speaker_0",
    file_name="output2.wav"
)



