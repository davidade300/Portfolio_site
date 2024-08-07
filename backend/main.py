from fastapi import FastAPI
from routers import auth, landing_page, projects

"""
Arquivo principal, contendo as configurações da API em sí
"""


app = FastAPI(debug=True)


app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(landing_page.router)


# intead of using the lines below it's better to use
# "uvicorn run" command on terminal or simply use "fastapi dev main.py"
# also on console

# if __name__ == "__main__":
# import uvicorn
#
# uvicorn.run(app, host="127.0.01.", port=8000)
