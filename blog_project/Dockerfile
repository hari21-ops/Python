ARG python_version=3.8

FROM python:${python_version} as builder 
WORKDIR /app
COPY blog_project/requirements.txt requirements.txt
RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:${python_version}-alpine
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY blog_project/ .

# Set the entry point to run the app
CMD [ "python", "blog/manage.py", runserver ] 
#CMD ["gunicorn", "blog_project.wsgi:application", "--bind", "0.0.0.0:8000"]
