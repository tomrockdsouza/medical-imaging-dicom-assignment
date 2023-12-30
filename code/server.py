from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
from main_module import calculate_volume_from_dicom

app = FastAPI()


@app.get('/')
async def homepage():
    return FileResponse("index.html")


@app.get('/favicon.ico')
async def favicon():
    return FileResponse("favicon.ico")


@app.post("/upload/")
async def upload_dcm_file(file: UploadFile):
    if not file.filename.endswith(".dcm"):
        return JSONResponse(content={"error": "Invalid file format. Only .dcm files are allowed."}, status_code=400)
    try:
        volume_mm3 = calculate_volume_from_dicom(await file.read())
        print(round(volume_mm3, 4))
        return JSONResponse(content={"volume": round(volume_mm3, 4)})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
