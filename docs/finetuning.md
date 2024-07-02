# Model Finetuning

Some proposed models for training are:
* [Microsoft Phi-3-mini](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
* [Microsoft Phi-2](https://ollama.com/library/phi)
* [stablelm2 1.6B](https://ollama.com/library/stablelm2:1.6b)
* [stablelm2 1.6B on HuggingFace](https://huggingface.co/stabilityai/stablelm-2-1_6b)
* [roberta-base-sqaud2](https://huggingface.co/deepset/roberta-base-squad2) (This one is currently used)

References:

* [SQuAD Question Answering Fine-tuning](https://github.com/huggingface/transformers/tree/v4.37.0/examples/pytorch/question-answering)
* [SQuAD Datasets](https://www.tensorflow.org/datasets/catalog/squad)



To train the model:  

1. pip install git+https://github.com/huggingface/accelerate
2. pip install datasets
3. pip install torch
4. pip install evaluate
5. pip install transformers
6. download utils_qa.py and run_qa_no_trainer.py from the [Transformers Github Question Answering Directory.](https://github.com/huggingface/transformers/tree/v4.37.0/examples/pytorch/question-answering)


Then, run in this in the Terminal:

python run_qa_no_trainer.py --model_name_or_path deepset/roberta-base-squad2 --dataset_name squad_v2 --train_file <**location of your dataset (json or csv file)**> --max_seq_length 384 --doc_stride 128 --output_dir <**output location of your model**>
