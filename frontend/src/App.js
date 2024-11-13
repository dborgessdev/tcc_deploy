import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/Login/Login';
import MenuPrincipal from './pages/MenuPrincipal/MenuPrincipal';
import Cadastro from './pages/Cadastro/Cadastro'; //Lembre-se de importar a pagina de cadastro

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/menu" element={<MenuPrincipal />} />
        <Route path="/cadastro" element={<Cadastro />} /> {/*Lembre-se de importar a pagina de cadastro*/}
        {/*<Route path="*" element={<NotFound />} />*/} {/* Rota para página 404 */} {/*Lembra de fazer a pagina de erro 404 n esquecer de forma nehuma */}
      </Routes>
    </Router>
  );
}

export default App;