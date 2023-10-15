from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
import scipy 

output_dir = 'audio_outputs'
device = None
model = None
config = None

def useGPU():
    global device
    device = 'cuda:0'

def useCPU():
    global device
    device = 'cpu'

def init():
    global model
    global device
    global config
    config = BarkConfig()
    model = Bark.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)
    model.to(device)
    print('initialized')

def clone(speech_as_text,file_name):
    # cloning a speaker.
    # It assumes that you have a speaker file in `bark_voices/speaker_n/speaker.wav` or `bark_voices/speaker_n/speaker.npz`
    output_dict = model.synthesize(
        speech_as_text,
        config,
        speaker_id="joe_biden",
        voice_dirs="audio_inputs/",
        temperature=0.5
        )
    scipy.io.wavfile.write(output_dir + '/' + file_name, 24000, output_dict['wav'])
    print('clone complete')

useGPU()
init()
clone(
    "Hi I am Joe Biden President of Mexico I mean United States [laughs]",
    'biden1.wav'
    )

clone(
    'Im Invoking the build better backs program, I mean uh anyway..',
    'biden2.wav'
    )