
```sql
select * from tb_fat_cad_individual;
select * from tb_fat_cad_domiciliar;
select * from tb_fat_familia_territorio;
select * from tb_fat_cidadao_territorio;
select * from tb_fat_cidadao_pec;
select * from tb_fat_atendimento_individual;
select * from tb_dim_municipio;
select * from tb_dim_unidade_saude;
select * from tb_fat_atendimento_odonto;
select * from tb_dim_cbo;
```

# Lista de Chaves estrangeiras
```
tb_fat_cad_individual
    co_dim_profissional -> tb_dim_profissional
    co_dim_tipo_ficha -> tb_dim_tipo_ficha
    co_dim_municipio -> tb_dim_municipio
    co_dim_unidade_saude -> tb_dim_unidade_saude
    co_dim_equipe -> tb_dim_equipe
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
    co_dim_cbo -> tb_dim_cbo
	co_dim_cbo_cidadao -> tb_dim_cbo
	co_dim_equipe -> tb_dim_equipe
	co_dim_etnia -> tb_dim_etnia
	co_dim_faixa_etaria -> tb_dim_faixa_etaria
	co_dim_frequencia_alimentacao -> tb_dim_frequencia_alimentacao
	co_dim_municipio_cidadao -> tb_dim_municipio
	co_dim_municipio -> tb_dim_municipio
	co_dim_nacionalidade -> tb_dim_nacionalidade
	co_dim_pais_nascimento -> tb_dim_pais
	co_dim_profissional -> tb_dim_profissional
	co_dim_raca_cor -> tb_dim_raca_cor
	co_dim_sexo -> tb_dim_sexo
	co_dim_situacao_trabalho -> tb_dim_situacao_trabalho
	co_dim_tempo -> tb_dim_tempo
	co_dim_tempo_validade_recusa -> tb_dim_tempo
	co_dim_tempo_validade -> tb_dim_tempo
	co_dim_tempo_morador_rua -> tb_dim_tempo_morador_rua
	co_dim_tipo_condicao_peso -> tb_dim_tipo_condicao_peso
	co_dim_tipo_escolaridade -> tb_dim_tipo_escolaridade
	co_dim_tipo_ficha -> tb_dim_tipo_ficha
	co_dim_tipo_orientacao_sexual -> tb_dim_tipo_orientacao_sexual
	co_dim_tipo_parentesco -> tb_dim_tipo_parentesco
	co_dim_tipo_saida_cadastro -> tb_dim_tipo_saida_cadastro
	co_dim_cds_tipo_origem -> tb_dim_tipo_origem
	co_dim_unidade_saude -> tb_dim_unidade_saude
	co_dim_identidade_genero -> tb_dim_identidade_genero
	co_dim_tipo_origem_dado_transp -> tb_dim_tipo_origem_dado_transp
	co_fat_cidadao_pec -> tb_fat_cidadao_pec
	co_fat_cidadao_pec_responsvl -> tb_fat_cidadao_pec

tb_fat_cad_domiciliar
    co_dim_cbo -> tb_dim_cbo
    co_dim_equipe -> tb_dim_equipe
    co_dim_municipio_cidadao -> tb_dim_municipio
    co_dim_municipio -> tb_dim_municipio
    co_dim_profissional -> tb_dim_profissional
    co_dim_tempo -> tb_dim_tempo
    co_dim_tempo_validade -> tb_dim_tempo
    co_dim_tempo_validade_recusa -> tb_dim_tempo
    co_dim_tipo_abastecimento_agua -> tb_dim_tipo_abastecimento_agua
    co_dim_tipo_acesso_domicilio -> tb_dim_tipo_acesso_domicilio
    co_dim_tipo_destino_lixo -> tb_dim_tipo_destino_lixo
    co_dim_tipo_domicilio -> tb_dim_tipo_domicilio
    co_dim_tipo_escoamento_sanitar -> tb_dim_tipo_escoamento_sanitar
    co_dim_tipo_ficha -> tb_dim_tipo_ficha
    co_dim_tipo_imovel -> tb_dim_tipo_imovel
    co_dim_tipo_localizacao -> tb_dim_tipo_localizacao
    co_dim_tipo_logradouro -> tb_dim_tipo_logradouro
    co_dim_tipo_material_parede -> tb_dim_tipo_material_parede
    co_dim_tipo_posse_terra -> tb_dim_tipo_posse_terra
    co_dim_tipo_situacao_moradia -> tb_dim_tipo_situacao_moradia
    co_dim_tipo_tratamento_agua -> tb_dim_tipo_tratamento_agua
    co_dim_cds_tipo_origem -> tb_dim_tipo_origem
    co_dim_unidade_saude -> tb_dim_unidade_saude
    co_dim_tipo_origem_dado_transp -> tb_dim_tipo_origem_dado_transp

tb_fat_familia_territorio
    co_dim_equipe -> tb_dim_equipe
    co_dim_municipio -> tb_dim_municipio
    co_dim_tempo_fcd -> tb_dim_tempo
    co_dim_unidade_saude -> tb_dim_unidade_saude
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
    co_fat_cidadao_territorio -> tb_fat_cidadao_territorio


tb_fat_cidadao_territorio
    co_dim_municipio -> tb_dim_municipio
    co_dim_unidade_saude -> tb_dim_unidade_saude
    co_dim_equipe -> tb_dim_equipe
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
```

## Lista de Chaves estrangeiras em fatos
```

tb_fat_cad_individual
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
    co_fat_cidadao_pec_responsavel -> tb_fat_cidadao_pec


tb_fat_cad_domiciliar


tb_fat_familia_territorio
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
    co_fat_cidadao_territorio -> tb_fat_cidadao_territorio
    co_fat_cad_domiciliar -> tb_fat_cad_domiciliar


tb_fat_cidadao_territorio
    co_fat_cidadao_pec -> tb_fat_cidadao_pec
```