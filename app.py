from fastapi.responses import JSONResponse
from src.retriver import DataEmbedding
import uvicorn
from src.flow import ModelGraph
from fastapi import FastAPI, File, HTTPException, UploadFile
import os

app = FastAPI()


UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

retriver=DataEmbedding()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")
    
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    

    retriver.get_retriever(path=file_path, model="sentence-transformers/all-MiniLM-L6-v2")
    return JSONResponse(content={"message": "File uploaded and indexed successfully"}, status_code=200)



@app.post('/ask')    
def load_graph(question:str):
    """Initialize the model graph."""
   
   
    retriver_tool=retriver.get_tool()
    model=ModelGraph(retriver_tool)
    graph=model.graph_run()

    print("Graph initialized successfully")
    mystate=graph.invoke({"query":question})
    print(mystate)
    return JSONResponse(content={"message": mystate['generated_out']}, status_code=200)

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)    
