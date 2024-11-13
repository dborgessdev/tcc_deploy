import style from './Cadastro.module.css';

function Cadastro() {
    



    return(
        <div>
            <h1>Cadastro</h1>
            <p>Cadastre-se para poder utilizar o sistema</p>
            <form>
                <input type="text" placeholder="Nome" />
                <input type="text" placeholder="Email" />
                <input type="password" placeholder="Senha" />
                <input type="password" placeholder="Confirme sua senha" />
                <input type="submit" value="Cadastrar" />
            </form>
        </div>
    );
}

export default Cadastro;