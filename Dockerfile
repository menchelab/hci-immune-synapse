FROM jupyter/datascience-notebook:abdb27a6dfbb

COPY requirements.txt requirements.R /tmp/

# Install additional fonts
RUN mkdir .fonts
RUN wget -O .fonts/Arial.ttf https://github.com/openscenegraph/OpenSceneGraph-Data/raw/master/fonts/arial.ttf 

# Install required Python Modules
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /tmp/requirements.txt

# Install required R Modules
RUN Rscript /tmp/requirements.R
