FROM python:3.10-slim

WORKDIR /app

# Requirements install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Path confusion illama iruka ellathayum copy panrom
COPY . .

EXPOSE 6009

# Direct-ah Python app run panrom
CMD ["python", "app.py"]