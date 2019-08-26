FROM jupyter/datascience-notebook:abdb27a6dfbb

COPY requirements.txt requirements.R /tmp/

# Install additional fonts (ArialMT)
RUN mkdir /tmp/.fonts
RUN wget -O /tmp/.fonts/Arial.ttf https://github.com/matomo-org/travis-scripts/raw/master/fonts/Arial.ttf 
# Rebuild the font cache.
RUN fc-cache -fv /tmp/.fonts

# Install required Python Modules
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /tmp/requirements.txt

# Install required R Modules
RUN Rscript /tmp/requirements.R
