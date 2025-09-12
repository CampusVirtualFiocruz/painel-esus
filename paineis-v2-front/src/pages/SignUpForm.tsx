import { Link } from 'react-router-dom';

export function SignUpForm() {
  return (
    <>
      <h1>Novo usuário</h1>

      <div>Formulário para cadastro de usuário</div>

      <Link to='/'>authenticate</Link>
    </>
  );
}
