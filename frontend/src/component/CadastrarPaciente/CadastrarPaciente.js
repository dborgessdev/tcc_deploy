import React, { useState } from 'react';
import style from './CadastrarPaciente.module.css';
import Imput from '../Imput/Imput';
import Botao from '../Botao/Botao';
import { handleCPFChange } from '../../service/FuncoesGerais';
import { cadastrarPaciente } from '../../service/API_function';

function CadastrarPaciente({ isOpen, onClose }) {
    const [cpf, setCpf] = useState('');
    const [nome, setNome] = useState('');
    const [data, setData] = useState('');

    const handleInputChange = (e) => {
        const cpfFormatado = handleCPFChange(e);
        setCpf(cpfFormatado);
    };

    const handleNomeChange = (e) => {
        setNome(e.target.value); 
    };

    const handleDataChange = (e) => {
        setData(e.target.value);
    };

    const HandleCadastroPaciente = () => {
        const paciente = {
            nome: nome,
            dataNasc: data,
            cpf: cpf
        };
        try {
            cadastrarPaciente(paciente);
            console.log(paciente);
            onClose();
        } catch (error) {
            console.error(error);
        }
    }

    return(
        <>
            {isOpen && (
                <div className={style.modalOverlay}>
                    <div className={style.conteiner}>
                        <div className={style.conteiner2}>
                            <div className={style.cima}>
                                <h3>Cadastro de Paciente</h3>
                            </div>
                            <div className={style.meio}>
                                <div className={style.meioImfo}>
                                    <p>Nome</p>
                                    <Imput type={'text'} placeholder={'Nome'} color={'CadaastroInput'} onChange={handleNomeChange} />
                                    <p>Data de Nascimento</p>
                                    <Imput type={'date'} placeholder={'Data de Nascimento'} color={'CadaastroInput'} onChange={handleDataChange } />
                                    <p>CPF</p>
                                    <Imput 
                                        type={'text'} 
                                        placeholder={'000.000.000-00'} 
                                        color={'CadaastroInput'} 
                                        value={cpf}
                                        onChange={handleInputChange} 
                                    />
                                </div>
                            </div>
                            <div className={style.baixo}>
                                <div className={style.conteiner3}>
                                    <Botao children={'Cancelar'} onClick={() => onClose()} color={'brancoButton'} />
                                    <Botao children={'Cadastrar'} onClick={() => HandleCadastroPaciente()} color={'brancoButton'} />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}

export default CadastrarPaciente;
