# curso-verao-rl-ime-2021

# Instalação

```bash
# instalar criador de ambiente virtual
# https://virtualenv.pypa.io/en/latest/installation.html
virtualenv -p python3.7 .  # criar ambiente virtual
source bin/activate        # ativar ambiente virtual

# atualizar pip
pip install -U pip setuptools

# instalar OpenAI gym do branch master ===> IMPORTANTE!
pip install -e git+https://github.com/openai/gym.git@master#egg=gym

# Bokeh vizualization (maiores detalhes em github.com/bokeh/jupyter_bokeh)
pip install bokeh jupyter_bokeh

# jupyter lab (IPython notebooks)
pip install jupyterlab

# opcional
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install @bokeh/jupyter_bokeh
```