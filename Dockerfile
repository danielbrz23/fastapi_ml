FROM python:3.12

WORKDIR /app

RUN apt-get  update && apt-get install -y \
	python3-dev \
	apt-utils \
	build-essential \
	&& rm -fr /var/lib/apt/lists/*

RUN pip install --upgrade setuptools
RUN pip install \
	cython==0.29.35 \
	numpy==2.3.2 \
	pandas==2.0.1 \
	pystan==3.10.0

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
