import { useState } from 'react';
import style from './Imput.module.css';

function Imput({ type, placeholder, value, onChange, imagen2, imagen3, color }) {
    const [inputType, setInputType] = useState(type);
    const [currentImage, setCurrentImage] = useState(imagen2);
    const inputClass = style[color] || style.defaultInput;

    const togglePasswordVisibility = () => {
        if (inputType === 'password') {
            setInputType('text');
            setCurrentImage(imagen3);
        } else {
            setInputType('password');
            setCurrentImage(imagen2);
        }
    };

    return (
        <div className={inputClass}>
            <input
                className={style.input}
                type={inputType}
                placeholder={placeholder}
                value={value}
                onChange={onChange}
            />
            {type === 'password' && (
                <img
                    src={currentImage}
                    className={style.icon2}
                    onClick={togglePasswordVisibility}
                    alt="toggle visibility"
                />
            )}
        </div>
    );
}

export default Imput;
