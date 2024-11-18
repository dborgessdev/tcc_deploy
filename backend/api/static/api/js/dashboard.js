document.addEventListener('DOMContentLoaded', () => {
    // Botões para redirecionar
    document.getElementById('btn-cadastrar-paciente').addEventListener('click', () => {
        window.location.href = "/cadastrar-paciente/";
    });
    document.getElementById('btn-cadastrar-medico').addEventListener('click', () => {
        window.location.href = "/cadastrar-medico/";
    });
    document.getElementById('btn-cadastrar-enfermeiro').addEventListener('click', () => {
        window.location.href = "/cadastrar-enfermeiro/";
    });
    document.getElementById('btn-cadastrar-atendimento').addEventListener('click', () => {
        window.location.href = "/cadastrar-atendimento/";
    });
});
