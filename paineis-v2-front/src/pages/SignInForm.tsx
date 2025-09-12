import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import '../styles/signInForm.scss';

export function SignInForm() {
  const navigate = useNavigate();
  const [email] = useState('');
  const [password] = useState('');

  function navigateToNewuser() {
    navigate('/signup');
  }

  return (
    <div className='formCenter'>
      <form className='formFields'>
        <div className='formField'>
          <label className='formFieldLabel' htmlFor='email'>
            E-Mail Address
          </label>
          <input
            type='email'
            id='email'
            className='formFieldInput'
            placeholder='Enter your email'
            name='email'
            value={email}
          />
        </div>

        <div className='formField'>
          <label className='formFieldLabel' htmlFor='password'>
            Password
          </label>
          <input
            type='password'
            id='password'
            className='formFieldInput'
            placeholder='Enter your password'
            name='password'
            value={password}
          />
        </div>

        <div className='formField'>
          <button className='formFieldButton'>Entrar</button>{' '}
          <button onClick={navigateToNewuser}>Novo Cadastro</button>
        </div>
      </form>
    </div>
  );
}
