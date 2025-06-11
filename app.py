{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN+6ZMTScNr3j2RmOrD1RgN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/prathikrish/first_llm_project/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ig2P9yzv757b"
      },
      "outputs": [],
      "source": [
        "with open(\"app.py\",\"w\") as f:\n",
        "  f.write(\"\"\"\n",
        "  import streamlit as st\n",
        "  from transformers import pipeline, set_seed\n",
        "\n",
        "  #Load Model\n",
        "  generator = pipeline(\"text-generation\", model = \"distilgpt2\",pad_token = 50256)\n",
        "  set_seed(42)\n",
        "\n",
        "  #Define response function\n",
        "  def get_response(user_input):\n",
        "    prompt = f\"User:{user_input}\\\\nBot:\"\n",
        "    response = generator(prompt,max_new_tokens=50,do_sample=True, temperature=0.7,top_p=0.95)\n",
        "    full_text = response[0][\"generated_text\"]\n",
        "    if \"Bot:\" in full_text:\n",
        "      return full_text.split(\"Bot:\")[-1].strip()\n",
        "    else:\n",
        "      return full_text.strip()\n",
        "\n",
        "  #Streamlit UI\n",
        "  st.title(\"LLM_trial1 : Chatbot\")\n",
        "  user_input = st.text_input(\"You:\",\"\")\n",
        "\n",
        "  if st.button(\"Send\"):\n",
        "    if user_input:\n",
        "      response = get_response(user_input)\n",
        "      st.text_area(\"Bot:\",value=response,height=100)\n",
        "      \"\"\")"
      ]
    }
  ]
}