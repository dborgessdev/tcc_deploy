import { WebSocket } from "ws";
import { BASE_URL } from "./axiosInstance";

class WebSocketService {
    constructor(BASE_URL) {
        this.socket = new WebSocket(BASE_URL);
    }

    connect(onMessageCallback) {
        this.socket.onopen = () => {
            console.log("Conectado ao servidor WebSocket");
        };

        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            onMessageCallback(data);
        };

        this.socket.onerror = (error) => {
            console.error("Erro no WebSocket:", error);
        };

        this.socket.onclose = () => {
            console.log("Desconectado do servidor WebSocket");
        };
    }

    disconnect() {
        if (this.socket) {
            this.socket.close();
        }
    }
}

export default WebSocketService;
