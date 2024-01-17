import { FormEvent, useState } from 'react';
import { useNavigate } from "react-router-dom";

import { Spinner } from 'reactstrap';

import '../styles/login.scss';

import logoImg from '../assets/images/logo.svg';
import iconUser from '../assets/images/user.svg';
import iconPassword from '../assets/images/password.svg';

import { AiOutlineEye, AiOutlineEyeInvisible } from "react-icons/ai";

import { useAuth } from '../context/AuthProvider/useAuth';
import { Footer } from '../components/Footer';
import { Snackbar } from '../components/Snackbar';

import { useQuery } from 'react-query';
import { Api } from "../services/api";
import { useInfo } from '../context/infoProvider/useInfo';
import { STALE_TIME } from '../config/stale-time';


interface CityResponse {
    cep: string;
    codIgbe: string;
    estado: string;
    municipio: string
    uf: string;
}

type CityInformationResponse = CityResponse
export function Login() {
    const auth = useAuth();
    let navigate = useNavigate();

    const [username, setUsername] = useState("admin");

    //const [password, setPassword] = useState("painelfiocruz22");
    const [password, setPassword] = useState("FCadmin");
    // const [username, setUsername] = useState("");
    // const [password, setPassword] = useState("");
    const [city, setCity] = useState("");
    const infoContext = useInfo();

    const [passwordShown, setPasswordShown] = useState(false);

    const [loading, setLoading] = useState(false);
    const [someStateOpen, setSomeStateOpen] = useState(false);

    const { data: diabeticosList, isLoading, error } = useQuery('city-informations', async () => {
        const response = await Api.get<CityInformationResponse>('city-informations');
        const data: CityResponse = response.data;
        setCity(`${data.municipio} - ${data.uf}`)
        infoContext.setCityInformation(data);
        return data;
    }
        , {
            staleTime: STALE_TIME
        });

    function validateForm() {
        return username.length > 0 && password.length > 0;
    }

    async function handleSubmit(event: FormEvent) {
        event.preventDefault();

        setLoading(true);

        if (validateForm()) {
            try {
                await auth.authenticate(username, password);
                navigate("/selecionarubs");
            } catch (error) {
                setSomeStateOpen(true);
                setLoading(false);
                setPassword('');
            }
        } else {
            setSomeStateOpen(true);
            setLoading(false);
            setPassword('');
        }
    }

    const togglePassword = () => {
        setPasswordShown(!passwordShown);
    };

    return (
        <div id="page-login">

            <div id="main">
                <aside>
                    <div className="header-content mb-5">
                        <div className="logo-content">
                            <img src={logoImg} alt="Painel e-SUS APS" title="Painel e-SUS APS" />
                            <div>
                                <h1>Painel Saúde Fiocruz</h1>
                                <h2 className='text-end'>{city}</h2>
                            </div>
                        </div>
                    </div>

                    <div className="container px-0">
                        <div className="row gx-5">
                            <div className="col-12 col-md-8 order-2 order-md-1">
                                <div className="separator mt-4"></div>

                                <div>
                                    <div className="subtitle my-4">O QUE É:</div>
                                    <p>O Painel Saúde Fiocruz é um software nativo para o Windows criado para ajudar gestores e profissionais da saúde na tomada de decisão e gestão do cuidado em saúde.</p>
                                </div>

                                <div className="separator mt-4"></div>

                                <div>
                                    <div className="subtitle my-4">PARA QUÊ:</div>
                                    <p>O Painel Saúde Fiocruz conecta o e-SUS APS e a base local de dados. Com isso, você tem acesso à informação de forma estruturada e a relatórios pré-configurados. Os relatórios são validados por especialistas em saúde pública e são atribuições das equipes de APS.</p>
                                </div>

                                <div className='mt-5'>
                                    <p>* Esta é uma ferramenta gratuita e essencial para a tomada de decisão em Atenção e Vigilância à Saúde.</p>
                                </div>
                            </div>

                            <div className="col-12 col-md-4 order-1 order-md-2">
                                <div className="formCenter" style={loading ? { opacity: 0.2 } : { opacity: 1 }}>
                                    <form className="formFields" onSubmit={handleSubmit}>

                                        <div className="formField">
                                            <label className="formFieldLabel" htmlFor="username">
                                                <img src={iconUser} alt="Usuário" /> Usuário
                                            </label>
                                            <div className='container-field'>
                                                <input
                                                    type="text"
                                                    id="username"
                                                    className="formFieldInput"
                                                    placeholder="Digite seu usuário"
                                                    name="username"
                                                    value={username}
                                                    autoComplete='off'
                                                    onChange={e => setUsername(e.target.value)}
                                                />
                                            </div>
                                        </div>

                                        <div className="formField">
                                            <label className="formFieldLabel" htmlFor="password">
                                                <img src={iconPassword} alt="Senha" /> Senha
                                            </label>

                                            <div className='container-field'>
                                                <input
                                                    type={passwordShown ? "text" : "password"}
                                                    id="password"
                                                    className="formFieldInput"
                                                    placeholder="Digite sua senha"
                                                    name="password"
                                                    value={password}
                                                    onChange={e => setPassword(e.target.value)}
                                                />

                                                {passwordShown
                                                    ? <AiOutlineEye size={'1.5rem'} onClick={togglePassword} className='password-toggle' />
                                                    : <AiOutlineEyeInvisible size={'1.5rem'} onClick={togglePassword} className='password-toggle' />
                                                }

                                            </div>
                                        </div>

                                        <div className="formField mt-5">
                                            <button className="btn btn-light formFieldButton" disabled={loading}>
                                                {loading ? (<Spinner size="sm">Carregando...</Spinner>) : 'ENTRAR'}
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </aside>

                <Snackbar
                    type="error"
                    open={someStateOpen}
                    onClose={() => setSomeStateOpen(false)}
                >
                    Usuário ou Senha inválidos!
                </Snackbar>
            </div>

            <Footer />
        </div>
    )
}
