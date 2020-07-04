FROM python:3.7

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /streamlit-docker

# copy over requirements
COPY requirements.txt ./requirements.txt

# installing required packages
RUN pip3 install -r requirements.txt

# copying all app files to image
COPY . .

# cmd to launch app when container is run
CMD streamlit run main.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
baseUrlPath = \"coviddash\"\n\
" > /root/.streamlit/config.toml'