


class Cbo:
 
        
    def __init__(
        self,
        co_seq_dim_cbo: int,
        nu_cbo: str,
        no_cbo: str,
        st_registro_valido: int,
        ds_filtro: str
) -> None:
        self.co_seq_dim_cbo = co_seq_dim_cbo
        self.nu_cbo = nu_cbo
        self.no_cbo = no_cbo
        self.st_registro_valido = st_registro_valido
        self.ds_filtro = ds_filtro
        self.label = self.parse_class(nu_cbo)
        
    def parse_class(self, nu_cbo: str):
        if nu_cbo.startswith("225"):
            return'MÉDICOS' 
        elif nu_cbo.startswith("2232"):
            return 'CIRURGIÕES-DENTISTAS'
        elif nu_cbo.startswith("2234"):
            return 'FARMACÊUTICOS'
        elif nu_cbo.startswith("2236"):
            return 'FISIOTERAPEUTAS'
        elif nu_cbo.startswith("2237"):
            return 'NUTRICIONISTAS'
        elif nu_cbo.startswith("2238"):
            return 'FONOAUDIÓLOGOS'
        elif nu_cbo.startswith("2239"):
            return 'TERAPEUTAS OCUPACIONAIS'
        elif nu_cbo.startswith("2241"):
            return 'EDUCAÇÃO FÍSICA'
        elif nu_cbo.startswith("2263"):
            return 'INTEGRATIVA E COMPLEMENTAR'
        elif nu_cbo.startswith("2515"):
            return 'PSCICÓLOGO'
        elif nu_cbo.startswith("2516"):
            return 'ASSITENTE SOCIAL'
        elif nu_cbo.startswith("2235"):
            return 'ENFERMEIROS'
        else:
            return 'OUTRO'
        
    def __str__(self) -> str:
        return f'\
            \n\t"co_seq_dim_cbo": {self.co_seq_dim_cbo}, \
            \n\t"nu_cbo": {self.nu_cbo}, \
            \n\t"no_cbo": {self.no_cbo}, \
            \n\t"st_registro_valido": {self.st_registro_valido}, \
            \n\t"ds_filtro": {self.ds_filtro}, \
            \n\t"label": {self.label}, \
        '
       
    def to_dict(self):
        return {
            "co_seq_dim_cbo": {self.co_seq_dim_cbo}, 
            "nu_cbo": {self.nu_cbo}, 
            "no_cbo": {self.no_cbo}, 
            "st_registro_valido": {self.st_registro_valido}, 
            "ds_filtro": {self.ds_filtro}, 
            "label": {self.label}, 
        }
  
class CboMeta(type):
    
    _instances = {}
    

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            header = True
            with open('../../../files/tb_dim_cbo.csv', 'r') as f:
                while 1:
                    row = f.readline()
                    if not row:
                        break
                    if not header:
                        row = row.split(",")
                        cbo = Cbo(
                            co_seq_dim_cbo=row[0],
                            nu_cbo=row[1],
                            no_cbo=row[2],
                            st_registro_valido=row[3],
                            ds_filtro=row[4]
                        )
                        cls._instances[cls].cbo_list.append(cbo)
                    else:
                        header = False
                
        return cls._instances[cls]        
       
class CboCollection(metaclass=CboMeta):
    cbo_list = []
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return [ str(cbo) for cbo in self.cbo_list]