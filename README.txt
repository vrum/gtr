1. Create a google cloud project and enable the translation API
    Open 
        https://console.cloud.google.com/projectselector2/home/dashboard 
    and create a new project or select an existing one.
    
    In the left hand menu, select APIs & services - Library, search for 
    translation, select the Cloud Translation API and enable it. In case you 
    don't have a billing account, you will be prompted to create one. 

2. Open https://console.cloud.google.com/iam-admin/serviceaccounts
    and create a service account for your project. Then create a key for 
    the service account. Select json format and save the downloaded file to 
    project folder.

3. Run the server
    Using docker-compose to create a container for the server
        Under the project folder, run:
            docker-compose up
    !!! Note: Server runs on port 8000. Update docker config if something else
    is already using port 8000.

or 

    Install Python 3, pip and virtualenv. Then inside the project folder, run:
        python3 -m venv env
        source env/bin/activate
        pip install -r requirements.txt
        GOOGLE_APPLICATION_CREDENTIALS=<path to service account key json file> uvicorn gtd:app

4. Run the client
    python gtranslate -f input.txt -l en


You should have the following structure for the project folder. 

!!!  Note the location of translate-key.json file.

syneto-dist
├── app
│   ├── common.py
│   ├── gtd.py
│   ├── gtranslate.py
│   ├── __init__.py
│   └── translate-key.json
├── definition.txt
├── docker-compose.yml
├── Dockerfile
├── input.txt
├── notes.txt
├── README.txt
└── requirements.txt
