#!/bin/bash
MODEL_URL="https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF/resolve/main/llama-3-8b-instruct.Q4_K_M.gguf"
MODEL_DIR="../models"
mkdir -p $MODEL_DIR
wget -O $MODEL_DIR/llama-3-8b-instruct.Q4_K_M.gguf $MODEL_URL