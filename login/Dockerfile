# Set python env 
ARG python_version=3.8

# Install dependencies & create venv
FROM python:${python_version} as builder 
WORKDIR /app
COPY login/requirements.txt requirements.txt
RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

#Copy bulder image with dependencies required to run app & copy source code
FROM python:${python_version}-alpine
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY login/ .


# Command to execute 
CMD["python", "login/manage.py", "runserver", "0.0.0.0:8000"]
