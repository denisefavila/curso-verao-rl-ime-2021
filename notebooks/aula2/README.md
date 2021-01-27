# Instalação
Tendo instalado o `python>=3.7` e o `jupyterlab`, o resto das dependências está definido no notebook `AULA2.ipynb`.

Entretanto, se preferir instalar pela linha de comando antes de rodar o notebook, execute as linhas abaixo.

```shell
# atualizar pip
pip install -U pip setuptools
# instalar OpenAI gym do branch master ===> IMPORTANTE!
pip install -e git+https://github.com/openai/gym.git@master#egg=gym
pip install pyglet==1.5.11
pip install matplotlib tensorflow tensorflow-probability tensorboard dm-sonnet ipywidgets tqdm
```
