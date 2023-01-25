from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    message_number = 1
    try:
        while True:
            data = await websocket.receive_json()
            data['number'] = message_number
            await websocket.send_json(data)
            message_number += 1
            
    except WebSocketDisconnect:
        message_number = 0
        pass
