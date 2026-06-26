# 🚀 4-Week AI & Cloud Portfolio Project Plan

> **Goal:** Build one project per week — 2 AI projects + 2 Cloud projects — to showcase on your resume and GitHub portfolio.

---

## 📅 Overview

| Week | Type  | Project |
|------|-------|---------|
| 1    | 🤖 AI    | RAG-Powered Document Chatbot (LangChain + OpenAI) |
| 2    | ☁️ Cloud | AWS Serverless Resume / Portfolio Website |
| 3    | 🤖 AI    | AI Image Recognition Web App (Python + HuggingFace) |
| 4    | ☁️ Cloud | GCP Real-Time Data Pipeline (BigQuery + Cloud Functions) |

---

## 🤖 WEEK 1 — AI Project #1
### RAG-Powered Document Chatbot (LangChain + OpenAI)

**What You'll Build:**
A chatbot that can answer questions about any PDF or document you feed it. It uses Retrieval-Augmented Generation (RAG) — one of the hottest AI patterns in the industry right now.

**Why It's Great for Your Resume:**
- Demonstrates knowledge of **LLMs, embeddings, and vector databases**
- Shows you can build **production-style GenAI apps**
- Highly relevant to real-world AI engineering roles

**Tech Stack:**
- Python
- LangChain
- OpenAI API (GPT-4o or GPT-3.5-turbo)
- FAISS or ChromaDB (vector store)
- Streamlit (UI)

**Step-by-Step Plan:**

| Day | Task |
|-----|------|
| Day 1 | Set up Python environment, install LangChain, OpenAI, and Streamlit. Get your OpenAI API key. |
| Day 2 | Write the PDF loader and text chunking logic using LangChain's `PyPDFLoader` and `RecursiveCharacterTextSplitter` |
| Day 3 | Create embeddings and store them in a FAISS vector store |
| Day 4 | Build the RAG chain using LangChain's `RetrievalQA` and connect it to OpenAI |
| Day 5 | Build the Streamlit front-end (upload PDF → ask questions) |
| Day 6 | Test, fix bugs, and clean up the code |
| Day 7 | Push to GitHub with a detailed README and deploy to Hugging Face Spaces (free) |

**Key Commands to Get Started:**
```bash
pip install langchain openai faiss-cpu streamlit pypdf tiktoken langchain-openai langchain-community
```

**Resume Bullet Point:**
> *Built a RAG-powered document chatbot using LangChain, OpenAI GPT, and FAISS — enabling natural language Q&A over custom PDF documents, deployed via Streamlit on Hugging Face Spaces.*

---

## ☁️ WEEK 2 — Cloud Project #1
### AWS Serverless Portfolio / Resume Website (The Cloud Resume Challenge)

**What You'll Build:**
A fully serverless personal portfolio/resume website hosted on AWS using S3, CloudFront, Lambda, API Gateway, and DynamoDB — complete with a live visitor counter. This is based on the famous **AWS Cloud Resume Challenge**.

**Why It's Great for Your Resume:**
- Demonstrates **5+ AWS services** in one project
- Shows understanding of **serverless architecture, IaC, and CI/CD**
- Recognized by cloud hiring managers — it's an industry-known challenge

**Tech Stack:**
- AWS S3 (static hosting)
- AWS CloudFront (CDN + HTTPS)
- AWS Route 53 (custom domain - optional)
- AWS Lambda (Python — visitor counter function)
- AWS API Gateway (REST API)
- AWS DynamoDB (visitor count storage)
- GitHub Actions (CI/CD pipeline)

**Step-by-Step Plan:**

| Day | Task |
|-----|------|
| Day 1 | Build your HTML/CSS resume page (keep it simple and clean) |
| Day 2 | Deploy the site to an S3 bucket and configure it for static website hosting |
| Day 3 | Set up CloudFront distribution in front of S3 for HTTPS and CDN caching |
| Day 4 | Create a DynamoDB table and a Python Lambda function for the visitor counter |
| Day 5 | Create an API Gateway endpoint to trigger your Lambda function |
| Day 6 | Add JavaScript to your site to call the API and display the visitor count live |
| Day 7 | Set up a GitHub Actions CI/CD pipeline to auto-deploy on push. Push to GitHub. |

**Resume Bullet Point:**
> *Deployed a fully serverless resume website on AWS using S3, CloudFront, Lambda, API Gateway, and DynamoDB, with a CI/CD pipeline via GitHub Actions — implementing Infrastructure as Code principles.*

---

## 🤖 WEEK 3 — AI Project #2
### AI Image Recognition Web App (HuggingFace + Gradio)

**What You'll Build:**
A web application where users upload an image and the AI identifies what's in it — built using a pre-trained Vision Transformer (ViT) model from Hugging Face. You can extend it to a niche use case (e.g., plant disease detector, food classifier, skin condition screener) to make it stand out even more.

**Why It's Great for Your Resume:**
- Shows understanding of **computer vision and transformer models**
- Demonstrates ability to use **pre-trained models (transfer learning)**
- Live shareable demo link (Hugging Face Spaces — free)

**Tech Stack:**
- Python
- Hugging Face Transformers (`google/vit-base-patch16-224`)
- Gradio (instant web UI)
- PyTorch
- Hugging Face Spaces (free deployment)

**Step-by-Step Plan:**

| Day | Task |
|-----|------|
| Day 1 | Set up environment, install `transformers`, `gradio`, and `torch`. Explore Hugging Face model hub. |
| Day 2 | Load the pre-trained ViT model and run basic image classification in a Jupyter notebook |
| Day 3 | **Optional upgrade:** Fine-tune the model on a custom dataset (e.g., 5-class food dataset from Kaggle) using Hugging Face `Trainer` |
| Day 4 | Build the Gradio interface — image upload → AI label + confidence scores |
| Day 5 | Add multiple model options (let user pick between models) or a confidence threshold slider |
| Day 6 | Write tests, clean up code, add comments |
| Day 7 | Deploy to Hugging Face Spaces. Push all code to GitHub with a thorough README including screenshots. |

**Key Commands to Get Started:**
```bash
pip install transformers gradio torch torchvision
```

**Resume Bullet Point:**
> *Developed an AI image recognition web app using Hugging Face Vision Transformers (ViT) and Gradio, capable of classifying images with confidence scores — deployed live on Hugging Face Spaces.*

---

## ☁️ WEEK 4 — Cloud Project #2
### GCP Real-Time Data Pipeline (Cloud Functions + BigQuery + Looker Studio)

**What You'll Build:**
An automated cloud data pipeline on Google Cloud Platform (GCP) that ingests data from a public API (e.g., weather data, stock prices, or Reddit posts), transforms it with a Cloud Function, stores it in BigQuery, and visualizes it with a live Looker Studio dashboard.

**Why It's Great for Your Resume:**
- Demonstrates **cloud data engineering** skills — extremely in-demand
- Shows end-to-end pipeline: **ingest → transform → store → visualize**
- Uses **GCP's free tier** — no cost to build it
- Produces a **live dashboard link** you can share with recruiters

**Tech Stack:**
- Google Cloud Functions (Python — data ingestion + transformation)
- Google Cloud Scheduler (cron trigger — runs every hour)
- Google Cloud Storage (GCS) (raw data landing zone)
- Google BigQuery (data warehouse)
- Looker Studio (free real-time dashboard)

**Step-by-Step Plan:**

| Day | Task |
|-----|------|
| Day 1 | Create a GCP free-tier account. Set up a project, enable APIs (Cloud Functions, BigQuery, Scheduler). |
| Day 2 | Write a Python Cloud Function that calls a public API (e.g., Open-Meteo weather API — free, no key needed) and saves raw JSON to a GCS bucket |
| Day 3 | Write a second Cloud Function triggered by GCS uploads that transforms the data and loads it into a BigQuery table |
| Day 4 | Set up Cloud Scheduler to run your ingestion function every hour (fully automated pipeline) |
| Day 5 | Connect BigQuery to Looker Studio and build a live dashboard (charts, time-series, KPIs) |
| Day 6 | Test the full pipeline end-to-end. Add error handling and logging. |
| Day 7 | Document the architecture with a diagram (use draw.io or Excalidraw). Push code to GitHub with architecture diagram in the README. Share the live Looker Studio dashboard link. |

**Resume Bullet Point:**
> *Engineered an automated real-time data pipeline on GCP using Cloud Functions, Cloud Scheduler, GCS, and BigQuery — processing hourly API data with a live Looker Studio visualization dashboard.*

---

## 🗂️ Portfolio & Resume Tips (Apply to All 4 Projects)

### GitHub Best Practices
- ✅ Each project gets its **own GitHub repository**
- ✅ Every repo has a **README.md** with: description, tech stack, architecture diagram, setup instructions, and screenshots
- ✅ Include a **live demo link** wherever possible (Hugging Face Spaces, AWS CloudFront URL, Looker Studio)
- ✅ Use `.env` files and `.gitignore` to **never commit API keys**
- ✅ Write clean, commented code with logical folder structure

### Resume Format for Each Project
```
[Project Name] | [Tech Stack keywords] | GitHub Link | Live Demo Link
• What it does (1 line)
• How you built it (tools/services used)
• Quantified result if possible (e.g., "processes 500+ records/hour", "deployed to 3 AWS services")
```

### Skills You'll Have After 4 Weeks
| Skill | Where You Used It |
|-------|-------------------|
| Python | All 4 projects |
| LLMs / Generative AI | Week 1 |
| LangChain | Week 1 |
| RAG Architecture | Week 1 |
| AWS (S3, Lambda, CloudFront, DynamoDB, API Gateway) | Week 2 |
| Serverless Architecture | Week 2 |
| CI/CD (GitHub Actions) | Week 2 |
| Computer Vision / Transformers | Week 3 |
| Hugging Face | Week 3 |
| GCP (Cloud Functions, BigQuery, Scheduler, GCS) | Week 4 |
| Data Engineering / ETL Pipelines | Week 4 |
| Data Visualization (Looker Studio) | Week 4 |

---

## 💰 Estimated Cost

| Project | Cost |
|---------|------|
| Week 1 — RAG Chatbot | ~$1–5 (OpenAI API calls) — use GPT-3.5-turbo to minimize |
| Week 2 — AWS Serverless Site | Free tier eligible — ~$0 |
| Week 3 — Image Recognition App | **$0** — Hugging Face is free |
| Week 4 — GCP Data Pipeline | Free tier eligible — ~$0 |

> 💡 **Pro Tip:** Sign up for the **AWS Free Tier** and **GCP Free Tier** ($300 free credit for new accounts) to cover all cloud costs.

---

*Plan generated for portfolio building — 4 weeks, 4 projects, 2 AI + 2 Cloud.*
