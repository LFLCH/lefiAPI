import json
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# run in command line with uvicorn main:app --reload
# export with deta (https://www.deta.sh/)
# to update changes : deta deploy  | deta watch 
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "https://lflch.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "welcome":"happy to welcome you on lefi's API",
        "bienvenue":"ravi que vous soyez arrivés jusqu'ici !",
        "auteur":"léo filoche"
    }

@app.get("/about")
def read_about():
    return{
        "status":"student",
        "institution":"Esir - Université de Rennes 1, France"
        }
@app.get("/resume")
def read_resume():
    with open('cv.json', encoding='utf-8') as f:
        data = json.load(f)
    return data

class FilePDFResponse(Response):
    media_type = "application/json"

@app.get("/resume/pdf",responses={200:{
    "description":"The resume, on PDF format",
    "content":{"application/pdf":{"example":"No example to show"}}
    }})
async def read_resume_pdf():
    return FileResponse("cv.pdf",media_type="application/pdf",filename="cv.pdf")

@app.get("/projects")
def read_projects():
    return  [
        {
           "name":"School Projects",
           "link":"https://github.com/LFLCH/school-projects",
           "description":"An overview of my most noteworthy school projects."
        },
        {
            "name":"Brain tumor",
            "link":"https://github.com/FenrirWolf4566/brain-tumor",
            "description":"[IN PROGRESS] A web viewer for brain tumors where predictions can be done thanks to AI"
        },
        {
            "name":"HeroesQuest",
            "languages":["Java"],
            "link":"https://github.com/LFLCH/HeroesQuest",
            "description":"[NOT PUBLIC YET] A small 2D adventure game",
            "members":[
                {
                "name":"Jérémy Bindel",
                "link": "https://github.com/J-Bindel"
                }
            ]
        },
        # {
        #     "name":"While Compiler",
        #     "languages":["Java","Antlr","C++","bash"],
        #     "link":"https://github.com/LFLCH/school-projects/tree/main/whilecompiler",
        #     "members":[
        #         {
        #         "name":"Bastien Faisant",
        #         "link": "https://github.com/Unstery"
        #         },
        #         {
        #          "name":"Kilian Cornec",
        #          "link":"https://github.com/Kali-ki"   
        #         }
        #     ]
        # },
        # {
        #     "name":"Administration",
        #     "languages":["Angular","NestJS","Quarkus","Docker"],
        #     "link":"https://github.com/LFLCH/school-projects/tree/main/administration",
        #     "members":[
        #         {
        #         "name":"Bastien Faisant",
        #         "link": "https://github.com/Unstery"
        #         }
        #     ]
        # }
    ]