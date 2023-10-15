# AI Voice Cloning

AI Voice Cloning is a Windows-based tool that allows you to clone voices for various applications. It leverages the power of Bark and Transformers for voice synthesis and processing.

## Bark
- [Bark GitHub](https://github.com/suno-ai/bark): The core library used for voice cloning.
- [Bark Presets](https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c): Explore voice presets and configurations for Bark.

## Quick Start

### Installing Python 3

To get started, you'll need to ensure you have Python 3 version 3.10.9 installed on your system.

### PIP Dependency Resoltion
[documentation](https://pip.pypa.io/en/stable/topics/dependency-resolution/#possible-ways-to-reduce-backtracking)

### Installing Virtual Environment and Setup

Follow these steps to set up a virtual environment for your project. This helps manage dependencies and isolate your environment.

1. Update `pip` to the latest version:
2. Install `virtualenv` to manage your virtual environment:
3. Create a virtual environment in your project directory, for example:
4. Activate the virtual environment. Use the appropriate command for your operating system:
- On Linux & macOS:
  ```
  source .env/bin/activate
  ```
- On Windows:
  ```
  .env/Scripts/activate
  ```
5. To deactivate the virtual environment, simply type:

### Installing Rust Package Manager

Bark might require Rust for some components. You can install Rust using [rustup](https://rustup.rs/).

### Installing Transformers

Transformers is a machine learning library from Hugging Face, used for voice synthesis. Follow these steps to set up Transformers within your virtual environment.

1. Create a virtual environment in your project directory.
2. Activate the virtual environment as previously explained.
3. Install Transformers using pip:

### Start Virtual Environment in VS Code Terminal

If you are using Visual Studio Code, make sure to activate your virtual environment in the VS Code terminal for a seamless development experience.

### Install SciPy

Install SciPy, a library used for scientific and technical computing:


### Compatibility for CUDA

If you are using NVIDIA GPUs, check compatibility with CUDA [here](https://developer.nvidia.com/cuda-gpus#compute).

### Install PyTorch

If your project requires PyTorch, follow the installation instructions provided [here](https://pytorch.org/get-started/locally/).


## Get or create fine, course, and text models
 - [Download Pretrained Models](https://huggingface.co/suno/bark/tree/main): place inside ./bark directory


## Cloning New Voices

### Installing TTS
- [TTS GitHub](https://tts.readthedocs.io/en/dev/installation.html): The core library used for voice cloning.
- [Useful Stackoverflow post](https://stackoverflow.com/questions/66726331/how-can-i-run-mozilla-tts-coqui-tts-training-with-cuda-on-a-windows-system)

To clone new voices, you may need to install additional libraries. Run the following command in your VS Code terminal or any other preferred terminal:


Now you're ready to clone and synthesize voices using this powerful tool.
