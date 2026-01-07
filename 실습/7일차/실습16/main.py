from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws/{nicname}")
async def websocket_endpoint(websocket: WebSocket, nicname: str):
    await websocket.accept()
    await websocket.send_text(f"{nicname}님 환영합니다!")

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"{nicname}닝의 메시지: {data}")

    except WebSocketDisconnect:
        print("웹소켓 연결 해제")
