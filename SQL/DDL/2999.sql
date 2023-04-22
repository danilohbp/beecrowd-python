create table "departamento" (
	id int,
	nome varchar(50),
	endereco varchar(50)
);

create table "dependente" (
	matr int,
	nome varchar(50),
	endereco varchar(50)
);


create table "desconto" (
	cod_desc int,
	nome varchar(50),
	tipo varchar(50),
	valor numeric
);

create table "divisao" (
	cod_divisao int,
	nome varchar(50),
	endereco varchar(50),
	cod_dep numeric
);


create table "emp_desc" (
	cod_desc int,
	matr int
);


create table "emp_venc" (
	cod_venc int,
	matr int
);


create table "empregado" (
	matr int,
	nome varchar(50),
	tipo varchar(50),
	data_lotacao timestamp,
	lotacao int,
	gerencia_cod_dep int,
	lotacao_div int,
	gerencia_div int
);


create table "vencimento" (
	cod_venc int,
	nome varchar(50),
	tipo varchar(50),
	valor numeric
);