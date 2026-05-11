# Fine-Tuning Qwen2.5 on 78k SQL Records

This repository contains a Jupyter Notebook for fine-tuning the **Qwen2.5** language model on a massive dataset of 78,000 SQL-related examples. The project leverages **Unsloth** for highly efficient training, significantly reducing memory usage and training time.

## 🚀 Key Features

- **Efficient Fine-Tuning**: Uses [Unsloth](https://github.com/unslothai/unsloth) to achieve up to 2x faster training speeds.
- **Model**: Qwen2.5 (optimized for instruction following and code generation).
- **Dataset**: 78,000 high-quality SQL create/context examples.
- **Methodology**: LoRA (Low-Rank Adaptation) with `r=16` and `alpha=32`, targeting all linear modules for maximum performance.
- **Platform**: Optimized for Google Colab (Tesla T4 GPU support).

## 📂 Project Structure

- `fine_tune_qwen2.5_78k_sql_data.ipynb`: The main notebook containing the full training pipeline (loading, adapter application, SFT training, and evaluation).
- `auto_click.py`: A helper script using `pyautogui` to prevent Google Colab from disconnecting during long training sessions (4+ hours).
- `assets/`: Contains images and diagrams related to the Qwen model architecture.

## 🛠️ Requirements

To run this notebook, you will need:
- A GPU (NVIDIA Tesla T4 or better).
- Python 3.10+
- Key Libraries:
  - `unsloth`
  - `transformers`
  - `trl`
  - `torch`
  - `xformers`

## 📈 Training Results

The model was trained for **1 epoch** (9,331 steps) with a global batch size of 8.
- **Hardware**: Tesla T4 GPU.
- **Duration**: ~4 hours 45 minutes.
- **Training Loss**: ~0.57 (converged significantly from 0.71).

## 💡 Usage

1. Open `fine_tune_qwen2.5_78k_sql_data.ipynb` in Google Colab.
2. Ensure the runtime type is set to **GPU (T4)**.
3. (Optional) Run `python auto_click.py` locally to keep your browser session active while training runs in the background.
4. Follow the cells sequentially to install dependencies and begin training.

## 📄 License

This project is for educational purposes. Please refer to the [Unsloth License](https://github.com/unslothai/unsloth) and [Qwen Model License](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) for usage restrictions.
