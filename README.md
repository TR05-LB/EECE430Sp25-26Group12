# Player List Django App



# **PART 3 — Run Docker image from GitHub**


```bash
git clone https://github.com/TR05-LB/EECE430Sp25-26Group12.git
cd EECE430Sp25-26GroupXX

docker build -t playerlist-django .

docker run -p 8000:8000 playerlist-django
```

