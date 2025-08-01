
# Spoken Language Identification using u-vector with CLI

This Python script performs spoken language identification using a u-vector with WSSL model. It takes either a single audio file or a directory containing multiple audio files as input. The script uses a pre-trained model to identify the language of the spoken audio.

## Prerequisites

#### Platform
- Operating System: Ubuntu 22.04
- Python: python >= 3.8 (make sure the default python is python3)

#### Make sure you have the following libraries installed:

- pandas
- torch
- matplotlib
- numexpr
- scipy
- numpy

#### The list of imported libraries

- tkinter
- pygame
- matplotlib
- datetime
- shutil
- random
- os
- scipy
- numpy

#### You can install these libraries using the following command:

```bash
pip install pandas torch matplotlib numexpr numpy scipy
```
Or,

```bash
pip install -r requirements.txt
```

## Usage

### 1. Clone the repository:

```bash
git clone https://github.com/NLTM-LID/LID.git
cd LID/CLI
```

### 2. Run the scripts:

#### For u-vector with WSSL
```bash
python demo_uvector_wssl.py path/to/audio_file_or_directory
```

Replace `path/to/audio_file_or_directory` with the path to the audio file or directory containing audio files with the '.wav' extension.

## Output

- If a directory is provided, the predicted languages for each audio file will be displayed in the console, and a CSV file named `predicted_lang.csv` will be created in the current directory, containing the audio filename and predicted language for each audio file.

- The predicted language will be displayed in the console if a single audio file path is provided. Additionally, a bar chart will be displayed, showing the predicted probabilities for all languages.

## Model Information

The script uses the pre-trained model for Indian spoken language identification. The model is trained for 12 Indian languages (12 classes).

The model file (`ZWSSL_20_50_e21.pth`) is located in the `model` directory:


## References

- H. Muralikrishna, P. Sapra, A. Jain and D. A. Dinesh, "Spoken Language Identification Using Bidirectional LSTM Based LID Sequential Senones," 2019 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU), Singapore, 2019, pp. 320-326, doi: 10.1109/ASRU46091.2019.9003947.(https://ieeexplore.ieee.org/document/9003947)
- M. H, S. Kapoor, D. A. Dinesh and P. Rajan, "Spoken Language Identification in Unseen Target Domain Using Within-Sample Similarity Loss," ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Toronto, ON, Canada, 2021, pp. 7223-7227, doi: 10.1109/ICASSP39728.2021.9414090.(https://ieeexplore.ieee.org/document/9414090)

## License

This project is licensed under the NLTM License - see the [LICENSE](../LICENSE) file for details.
