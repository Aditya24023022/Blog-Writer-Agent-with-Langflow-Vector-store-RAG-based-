Blog-Writer-Agent-with-Langflow-Vector-store-RAG-based-

🧠 Blog Writer Agent with Langflow (RAG-Based)
This project is an intelligent AI-powered Blog Writer Agent built using Langflow, integrating Retrieval-Augmented Generation (RAG) architecture. It combines IBM Embedding Models and IBM Granite model to create long, detailed, and human-like blog posts based on reference documents and user queries.

The project includes both:

A Langflow RAG pipeline (backend logic)
A Streamlit interface (frontend UI)
🚀 Project Overview
This Blog Writer Agent automates the process of writing research-based blogs. It retrieves contextual information from a reference document (e.g., a hackathon file) and uses a powerful LLM (IBM Granite model) to generate a detailed, engaging, and natural-sounding blog in plain text.

You can run the project in two main phases:

Building and Testing the RAG pipeline in Langflow Desktop
Creating and Running the Streamlit Interface
🧩 Prerequisites
Before starting, make sure you have:

Langflow Desktop installed
IBM Cloud Account (for embedding model and IBM Granite model) — or a Replicate token if you choose to run IBM Granite via Replicate
Python 3.10
VS Code or any IDE
⚙️ Step 1: Setting Up Langflow RAG Project
	1.	Open Langflow Desktop
Launch Langflow Desktop on your system. Once opened, you’ll be greeted with the template selection window.
	2.	Select the “Vector Store RAG” Template
From the list of available templates, select:

Vector Store RAG

This template gives you a base flow with:

Document Loader
Text Splitter
Embedding Model
Vector Store
Retriever
Language Model (LLM)
Prompt Template
🧠 Step 2: Configure the Embedding Model
	1.	Open the “Vector Store” Component
By default, the Vector Store component uses OpenAI embeddings. We’ll replace this with IBM Embeddings.
	2.	Change the Embedding Model
Click on the Embedding Model inside the Vector Store block.
Select IBM Embedding from the dropdown.
	3.	Connect IBM Cloud
Get your Project ID and API Key from your IBM Cloud account:

Log in to IBM Cloud
Go to your project dashboard
Copy the Project ID and API Key
Paste these credentials into the IBM Embedding Model configuration in Langflow.

✅ Ensure proper connection — test it by running a small embedding check to confirm it’s working.

📁 Step 3: Add the Reference File
Locate the Hackathon reference file included in the project repository.
Upload this file in the File Loader or Document Loader component in Langflow.
This file will act as your context data for the RAG model — meaning the AI will retrieve information from it when writing blogs.

🧾 Step 4: Update the Prompt
Open the Prompt component in Langflow.
Replace the default text with the custom prompt for your Blog Writer Agent. (You’ll find this prompt inside the project repository.)
This prompt instructs the AI to:

“Write a very long, detailed, and human-like blog in plain text using the reference data and context.”

🤖 Step 5: Replace the Language Model
	1.	Remove the Default LLM
By default, the RAG template uses an OpenAI or similar model. Delete that Language Model component.
	2.	Add the IBM Granite LLM Component
Add the IBM Granite LLM component — you can configure it either with your IBM Cloud Project ID and API Key, or (optionally) by using a Replicate token if you prefer to run Granite via Replicate. Fill in the required credentials (IBM Project ID & API Key, or Replicate token) in the component configuration.

🧩 Step 6: Test Your Agent in Playground
Now, go to the Playground section in Langflow and test your setup.

Try a query like this:

Write a very long, detailed, human-like blog in plain text about:
get the whole information from the parser as team name and everything timing
and then write a blog.
✅ You should get a beautiful, long, natural, and structured blog as output.

🌐 Step 7: Get API Access
Once your flow is working perfectly:

Click API Access on the top-right corner of Langflow.

Copy:

The Flow URL
The Langflow API Key
These two will be used for the Streamlit interface.

💻 Step 8: Building the Interface (Streamlit)
Now, we’ll build a web interface to interact with the agent.
	1.	Open app.py in VS Code
Locate the app.py file from your repository and open it in VS Code.

Inside this file, find the placeholders for:

API URL
Langflow API Key
Replace them with:

The Flow URL (from Langflow)
The API Key (from Langflow)
Save the file.

🐍 Step 9: Run the Streamlit Interface
Now, open your Command Prompt or VS Code Terminal, and run these commands step by step:

Step 1: Create a virtual environment

python -m venv myenv python==3.10

Step 2: Activate the environment

myenv\Scripts\activate

Step 3: Install dependencies

pip install streamlit requests

Step 4: Run the Streamlit app

streamlit run app.py
🌍 Step 10: Test Your Project
Once the above command runs successfully, your Blog Writer Agent Interface will open automatically in your browser at:

http://localhost:8501
You can now test your blog writer by entering any query such as:

“Write a very long, detailed, human-like blog in plain text about the hackathon event including team names, timings, and outcomes.”

The system will use:

The reference document (Hackathon file)
The RAG pipeline
The IBM Granite model (configured via IBM Cloud credentials or Replicate token)
…to generate an in-depth, human-like blog post in plain text!

🧰 Technologies Used
Component	Technology
Framework	Langflow Desktop
AI Architecture	RAG (Retrieval-Augmented Generation)
Embedding Model	IBM Embedding Model
Language Model	IBM Granite model (via IBM Cloud or Replicate)
Frontend	Streamlit
Backend API	Langflow Flow API
Programming Language	Python 3.10
