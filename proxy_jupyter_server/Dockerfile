FROM pytorch/pytorch:latest

WORKDIR /src

COPY . .

RUN pip install jupyterlab

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

