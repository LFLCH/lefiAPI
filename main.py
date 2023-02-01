from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# run in command line with uvicorn main:app
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
        "bienvenue":"ravi que vous soyez arrivés jusqu'ici !"
    }

@app.get("/about")
def read_about():
    return{
        "status":"student",
        "institution":"Esir - Université de Rennes 1, France"
        }
@app.get("/resume")
def read_resume():
    return {
        "header":"I am currently looking for a summer internship",
        "categories":[
         {
            "name":"Education",
            "articles":[
                {
                    "title":"Engineering degree in computer science",
                    "dates":"2021->2024",
                    "content":"Courses in Computer Science at Université de Rennes 1"
                }
            ]
         }   
        ]
    }

@app.get("/projects")
def read_projects():
    return  [
        {
            "name":"HeroesQuest",
            "languages":["Java"],
            "link":"https://github.com/LFLCH/HeroesQuest",
            "members":[
                {
                "name":"Jérémy Bindel",
                "link": "https://github.com/J-Bindel"
                }
            ]
        },
        {
            "name":"While Compiler",
            "languages":["Java","Antlr","C++","bash"],
            "link":"https://github.com/LFLCH/school-projects/tree/main/whilecompiler",
            "members":[
                {
                "name":"Bastien Faisant",
                "link": "https://github.com/Unstery"
                },
                {
                 "name":"Kilian Cornec",
                 "link":"https://github.com/Kali-ki"   
                }
            ]
        },
        {
            "name":"Administration",
            "languages":["Angular","NestJS","Quarkus","Docker"],
            "link":"https://github.com/LFLCH/school-projects/tree/main/administration",
            "members":[
                {
                "name":"Bastien Faisant",
                "link": "https://github.com/Unstery"
                }
            ]
        }
    ]