FROM python

WORKDIR /booktracker

RUN pip install --no-cache-dir poetry

COPY . .

RUN poetry install

EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

