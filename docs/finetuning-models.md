# Model Finetuning

Parameters determine the ability of the model to learn, generalize and capture language features. More parameters generally mean the model can learn more complex patterns in the data. Larger models with more parameters tend to perform better on a wide range of language tasks. In our case, our model has a specified task, and can perform well with less parameters. 

Smaller models are able to generate responses more quickly, and require less resources to operate and finetune.



Some proposed models for finetuning are:

* [Microsoft Phi-3-mini](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) - 3.82B params
* [stablelm-2-1_6B](https://huggingface.co/stabilityai/stablelm-2-1_6b) - 1.64B params
* [roberta-base-sqaud2](https://huggingface.co/deepset/roberta-base-squad2) (This one is currently used) - 124M params
* [minilm-uncased-squad2](https://huggingface.co/deepset/minilm-uncased-squad2) 33.4M params

[YorkGPT Huggingface Dataset Repository](https://huggingface.co/datasets/darrylnurse/yorkgpt)

References:

* [SQuAD Question Answering Fine-tuning](https://github.com/huggingface/transformers/tree/v4.37.0/examples/pytorch/question-answering)
* [SQuAD Datasets](https://www.tensorflow.org/datasets/catalog/squad)
* [Creating a Dataset on the Huggingface Dataset Registry](https://huggingface.co/docs/datasets/repository_structure)


Dependencies for finetuning:  

1. pip install git+https://github.com/huggingface/accelerate
2. pip install datasets
3. pip install torch
4. pip install evaluate
5. pip install transformers


Then, run in this in the Terminal (YorkGPT CWD):

python finetuning-scripts/run_qa_no_trainer.py --model_name_or_path deepset/minilm-uncased-squad2 --dataset_name darrylnurse/yorkgpt --train_file <**location of your dataset (json or csv file)**> --max_seq_length 384 --doc_stride 128 --output_dir <**output location of your model**>

You can replace "deepset/roberta-base-squad2" with a model of your choice.
