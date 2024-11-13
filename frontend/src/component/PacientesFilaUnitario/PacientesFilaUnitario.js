import React, { useState } from 'react';
import Botao from '../Botao/Botao';
import EscolhaDeFila from '../EscolhaDeFila/EscolhaDeFila';
import style from './PacientesFilaUnitario.module.css';
import ExluirPacienteFila from '../ExluirPacineteFila/ExluirPacienteFila';
import ExluirPaciente from '../ExluirPacinete/ExluirPaciente';

const MODAL_COMPONENTS = {
    1: EscolhaDeFila,
    2: ExluirPacienteFila,
    3: ExluirPaciente,
    // Adicione novos modais aqui conforme necessário
};

function PacientesFilaUnitario({ cpf, nome, dataNasc, pacientekey, botao, modeal }) {
    const [isModalOpen, setModalOpen] = useState(false);
    const [ModalComponent, setModalComponent] = useState(null);

    const handleOpenModal = () => {
        const Component = MODAL_COMPONENTS[modeal];
        if (Component) {
            setModalComponent(() => Component);
            setModalOpen(true);
        }
    };

    const handleCloseModal = () => {
        setModalOpen(false);
        setModalComponent(null);
    };

    return (
        <>
            <div className={style.conteiner}>
                <h5>{cpf}</h5>
                <h5>{nome}</h5>
                <h5>{dataNasc}</h5>
                <div className={style.botoes}>
                    <Botao children={botao} onClick={handleOpenModal} color={'brancoButton'} />
                </div>
            </div>
            {isModalOpen && ModalComponent && (
                <ModalComponent
                    isOpen={isModalOpen}
                    onClose={handleCloseModal}
                    paciente={{ cpf, nome, dataNasc, pacientekey }}
                />
            )}
        </>
    );
}

export default PacientesFilaUnitario;
