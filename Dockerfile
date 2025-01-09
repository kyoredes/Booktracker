FROM python

WORKDIR /booktracker

RUN pip install uv

COPY . .

RUN uv sync

EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

