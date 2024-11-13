import style from "./Login.module.css";
import Imput from "../../component/Imput/Imput";
import Branco from "../../assets/img/Branco.svg";
import olhoFechadoIcon from "../../assets/img/eye.png";
import olhoAbertoIcon from "../../assets/img/show.png";
import { useState } from "react";
import Botao from "../../component/Botao/Botao";
import { useNavigate } from "react-router-dom";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    return(
        <div className={style.container}>
            <div className={style.conteiner2}>
                <h1>Login</h1>
                <Imput
                    type="email"
                    placeholder="Email"
                    onChange={(e) => setEmail(e.target.value)}
                    imagen2={Branco}
                />
                <Imput
                    type="password"
                    placeholder="Senha"
                    onChange={(e) => setPassword(e.target.value)}
                    imagen2={olhoFechadoIcon}
                    imagen3={olhoAbertoIcon}
                />
                <a href="#">Forgot password?</a>
                <Botao children={"Login"} onClick={() => navigate("/menu")} color={'brancoButton'} />
                <div className={style.register}>
                    <p>Don't have an account? <a href="#">Register here!</a></p>
                </div>
            </div>
        </div>
    );
}

export default Login;