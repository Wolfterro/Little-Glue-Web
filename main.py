from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.routers import router
from core.little_glue import LittleGlue


app = FastAPI()
app.include_router(router=router)
try:
    app.mount("/generated_glues", StaticFiles(directory="generated_glues"), name="generated_glues")
except RuntimeError:
    LittleGlue.get_or_create_generated_glues_folder()
    app.mount("/generated_glues", StaticFiles(directory="generated_glues"), name="generated_glues")
