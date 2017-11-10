--Fillipe Borges 1700135
--Gabriel George S. 1700824
--Alisson Ferrari 1700784
--Lucca Marques 1700726
CREATE DATABASE LMS_Final_Faculdade
GO
USE LMS_Final_Faculdade
GO
CREATE TABLE Curso(
	Sigla VARCHAR(5) NOT NULL,
	Nome VARCHAR(50) NOT NULL,
	CONSTRAINT [UQ_Sigla] UNIQUE(Sigla),
	CONSTRAINT [UQ_Nome] UNIQUE(Nome)
)
GO
CREATE TABLE GradeCurricular(
	Sigla_Curso VARCHAR (5) NOT NULL,
	Ano  SMALLINT NOT NULL,
	Semestre Char(1) NOT NULL,
	CONSTRAINT [UQ_Semestre] UNIQUE(Semestre),
	CONSTRAINT [FK_Sigla_Curso] FOREIGN KEY (Sigla_Curso) REFERENCES Curso(Sigla)
)
GO
CREATE TABLE Periodo(
	Sigla_Curso VARCHAR(5) NOT NULL,
	Ano_Grade SMALLINT NOT NULL,
	Semestre_Grade CHAR(1) NOT NULL,
	Numero TINYINT NOT NULL,
	CONSTRAINT [UQ_Numero] UNIQUE (Numero),
	CONSTRAINT [FK_Semestre_Grade] FOREIGN KEY (Semestre_Grade) REFERENCES GradeCurricular(Semestre)
)
GO
CREATE TABLE Disciplina(
	Nome VARCHAR (240) NOT NULL,
	Carga_Horario TINYINT NOT NULL,
	Teoria DECIMAL(3) NOT NULL,
	Pratica DECIMAL(3) NOT NULL,
	Ementa TEXT NOT NULL,
	Competencias TEXT NOT NULL,
	Habilidades TEXT NOT NULL,
	Conteudo TEXT NOT NULL,
	Bibliografia_Basica TEXT NOT NULL,
	Bibliografia_Complementar TEXT NOT NULL,
	CONSTRAINT [UQ_NomeDisciplina] UNIQUE (Nome)
)
GO

CREATE TABLE PeriodoDisciplina(
	Sigla_Curso VARCHAR(5) NOT NULL,
	Ano_Grade SMALLINT NOT NULL,
	Semestre_Grade CHAR(1) NOT NULL,
	Numero_Periodo TINYINT NOT NULL,
	Nome_Disciplina VARCHAR(240) NOT NULL,
	CONSTRAINT [UQ_Numero_Disciplina] UNIQUE (Numero_Periodo),
	CONSTRAINT [FK_Nome_Disciplina] FOREIGN KEY (Nome_Disciplina) REFERENCES Disciplina(Nome)
	)
	GO
CREATE TABLE Aluno(
	RA INT NOT NULL,
	Nome VARCHAR(120) NOT NULL,
	Email VARCHAR(80),
	Celular CHAR(11) NOT NULL,
	Sigla_Curso CHAR(2) NOT NULL,
	CONSTRAINT [UQ_RA] UNIQUE (RA)
)
GO
CREATE TABLE Professor(
	RA INT NOT NULL,
	Apelido VARCHAR(30) NOT NULL,
	Nome VARCHAR(120) NOT NULL,
	Email VARCHAR(80) NOT NULL,
	Celular CHAR(11) NOT NULL,
	CONSTRAINT [UQ_RA_Professor] UNIQUE (RA),
	CONSTRAINT [UQ_Apelido] UNIQUE (Apelido)
)
GO
CREATE TABLE Turma(
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	id CHAR(1) NOT NULL,
	Turno VARCHAR(15) NOT NULL,
	RA_Professor INT NOT NULL,
	CONSTRAINT [UQ_Id_Turma] UNIQUE (id),
	CONSTRAINT [FK_RA_Professor] FOREIGN KEY (RA_Professor) REFERENCES Professor(RA)
)
GO

CREATE TABLE CursoTurma(
	Sigla_Curso VARCHAR(5)	NOT NULL,
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	id_Turma CHAR(1) NOT NULL,
	CONSTRAINT [UQ_Id_TurmaCurso] UNIQUE (id_Turma),
	CONSTRAINT [FK_Id_Turma] FOREIGN KEY (id_Turma) REFERENCES Turma(id)
)
GO
CREATE TABLE Questoes(
	Nome_Discplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	id_Turma CHAR(1) NOT NULL,
	Numero INT NOT NULL,
	Data_Limite_Entrega DATE NOT NULL,
	Descricao TEXT,
	Dia_Publicacao DATE NOT NULL,
	CONSTRAINT [FK_Id_TurmaQuestoes] FOREIGN KEY (id_Turma) REFERENCES Turma(id),
	CONSTRAINT [UQ_QuestaoNumero] UNIQUE (Numero),
	CONSTRAINT [UQ_Id_QuestoesTurma] UNIQUE (id_Turma)
)
GO
CREATE TABLE ArquivoQuestoes(
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	id_Turma CHAR(1) NOT NULL,
	Numero_Questao INT NOT NULL,
	Arquivo VARCHAR(500) NOT NULL,
	CONSTRAINT [FK_QuestoesNumero] FOREIGN KEY (Numero_Questao) REFERENCES Questoes(Numero),
	CONSTRAINT [UQ_QuestoesArquivo] UNIQUE (Arquivo),
)
GO
CREATE TABLE Respostas(
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	id_Turma CHAR (1) NOT NULL,
	Numero_Questao INT NOT NULL,
	RA_Aluno INT NOT NULL,
	Data_Avaliacao DATE NOT NULL,
	Nota DECIMAL(4,2) NOT NULL,
	Avaliacao TEXT,
	Descricao TEXT,
	Data_de_Envio DATE NOT NULL,
	CONSTRAINT [UQ_RA_Aluno] UNIQUE (RA_Aluno),
	CONSTRAINT [FK_Id_TurmaRespostas] FOREIGN KEY (id_Turma) REFERENCES Questoes(id_Turma),
	CONSTRAINT [UQ_NumeroQuestao] UNIQUE (Numero_Questao)
)
GO
CREATE TABLE ArquivoRespostas(
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	id_Turma CHAR(1) NOT NULL,
	Numero_Questao INT NOT NULL,
	RA_Aluno INT NOT NULL,
	Arquivo VARCHAR(500) NOT NULL,
	CONSTRAINT [UQ_ArquivoRespostas] UNIQUE (Arquivo),
	CONSTRAINT [FK_QuestaoRespostas] FOREIGN KEY (Numero_Questao) REFERENCES Respostas(Numero_Questao)
)
GO
CREATE TABLE Matricula(
	RA_Aluno INT NOT NULL,
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	id_Turma CHAR (1) NOT NULL,
	CONSTRAINT [UQ_Id_TurmaMatricula] UNIQUE (id_Turma),
	CONSTRAINT [FK_Aluno_RA] FOREIGN KEY (RA_Aluno) REFERENCES Aluno(RA)
)
GO
