CREATE DATABASE Faculdade
GO
USE Faculdade
GO
CREATE TABLE Disciplina(
	IdDisciplina INT NOT NULL,
	Nome varchar(240) NOT NULL,
	CargaHoraria tinyint NOT NULL,
	Teoria decimal(3) NOT NULL,
	Pratica decimal(3) NOT NULL,
	Ementa text NOT NULL,
	Competencias text NOT NULL,
	Habilidades text NOT NULL,
	Conteudo text NOT NULL,
	Bibliografia_Basica text NOT NULL,
	Biblioteca_complementar text NOT NULL,
CONSTRAINT [UQ_DisciplinaNome] UNIQUE (IdDisciplina, Nome),
CONSTRAINT [PK_Disciplina] PRIMARY KEY
(
	IdDisciplina ASC	
))
GO
CREATE TABLE Curso(
	IdCurso INT NOT NULL,
	Sigla varchar(5) NOT NULL,
	Nome varchar(50) NOT NULL,
CONSTRAINT [UQ_CursoSiglaNome]	UNIQUE (IdCurso, Sigla, Nome),
CONSTRAINT [PK_Curso] PRIMARY KEY CLUSTERED
(
	IdCurso ASC
))
GO
CREATE TABLE Aluno(
	IdAluno INT NOT NULL,
	IdCurso INT NOT NULL,
	RA_Aluno int NOT NULL,
	Nome varchar(120) NOT NULL,
	Email varchar(80) NOT NULL,
	Celular char(11) NOT NULL,
CONSTRAINT [UQ_AlunoRA] UNIQUE (IdAluno, RA_Aluno),
CONSTRAINT [FK_AlunoCurso]FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
CONSTRAINT [PK_Aluno] PRIMARY KEY
(
		IdAluno ASC
))
GO
CREATE TABLE GradeCurricular(
	IdGradeCurricular INT NOT NULL,
	IdCurso INT NOT NULL,
	Ano int NOT NULL,
	Semestre char(1) NOT NULL,
CONSTRAINT [UQ_GradeCurricularAnoSemestre] UNIQUE (IdGradeCurricular, Ano, Semestre),
CONSTRAINT [FK_CursoGradeCurricular]FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
CONSTRAINT [PK_GradeCurricular] PRIMARY KEY CLUSTERED
(
	IdGradeCurricular ASC
))
GO
CREATE TABLE Periodo(
	IdPeriodo INT NOT NULL,
	IdCurso INT NOT NULL,
	IdGradeCurricular INT NOT NULL,
	NumeroPeriodo tinyint NOT NULL,
CONSTRAINT [UQ_PeriodoNumero] UNIQUE (IdPeriodo, NumeroPeriodo),
CONSTRAINT [FK_CursoPeriodo] FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
CONSTRAINT [FK_GradeCurricularPeriodo] FOREIGN KEY (IdGradeCurricular) REFERENCES GradeCurricular(IdGradeCurricular),
CONSTRAINT [PK_Periodo] PRIMARY KEY CLUSTERED
(
	IdPeriodo ASC
))
GO
CREATE TABLE PeriodoDisciplina(
	IdPeriodoDisciplina INT NOT NULL,
	IdCurso INT NOT NULL,
	IdGradeCurricular INT NOT NULL,
	IdPeriodo INT NOT NULL,
	IdDisciplina INT NOT NULL,
CONSTRAINT [FK_CursoPeriodoDisciplina] FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
CONSTRAINT [FK_PeriodoGradeCurricular] FOREIGN KEY (IdGradeCurricular) REFERENCES GradeCurricular(IdGradeCurricular),
CONSTRAINT [FK_PeriodoDisciplinaPeriodo] FOREIGN KEY (IdPeriodo) REFERENCES Periodo(IdPeriodo),
CONSTRAINT [FK_DisciplinaPeriodoDisciplina] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [PK_PeriodoDisciplina] PRIMARY KEY CLUSTERED
(
	IdPeriodoDisciplina
))
GO
CREATE TABLE DisciplinaOfertada(
	IdDisciplinaOfertada INT NOT NULL,
	IdDisciplina INT NOT NULL,
	AnoOfertado SMALLINT NOT NULL,
	SemestreOfertado CHAR(1) NOT NULL,
CONSTRAINT [UQ_DisciplinaOfertadaData] UNIQUE (IdDisciplinaOfertada, AnoOfertado, SemestreOfertado),
CONSTRAINT [FK_DisciplinaDisciplinaOfertada] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [PK_DisciplinaOfertada] PRIMARY KEY CLUSTERED
(
	IdDisciplinaOfertada ASC
))
GO
CREATE TABLE Professor(
	IdProfessor INT NOT NULL,
	RA_Professor INT NOT NULL,
	Apelido varchar(30) NOT NULL,
	Nome varchar(30) NOT NULL,
	Email varchar(120) NOT NULL,
	Celular char(11) NOT NULL,
CONSTRAINT [UQ_Professor] UNIQUE(IdProfessor, RA_Professor, Apelido),
CONSTRAINT [PK_Professor] PRIMARY KEY CLUSTERED
(
	IdProfessor ASC
))
GO
CREATE TABLE Turma(
	IdTurma INT NOT NULL,
	IdDisciplina INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdProfessor INT NOT NULL,
	Turno varchar(15) NOT NULL,
CONSTRAINT [FK_DisciplinaTurma] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [FK_DisciplinaOfertadaTurma] FOREIGN KEY (IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_ProfessorTurma] FOREIGN KEY (IdProfessor) REFERENCES Professor(IdProfessor),
CONSTRAINT [PK_Turma] PRIMARY KEY CLUSTERED
(
	IdTurma
))
GO
CREATE TABLE CursoTurma(
	IdCursoTurma INT NOT NULL,
	IdCurso INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdTurma INT NOT NULL,
CONSTRAINT [FK_CursoCursoTurma] FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
CONSTRAINT [FK_OfertadaCursoTurma] FOREIGN KEY (IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_TurmaCursoTurma] FOREIGN KEY (IdTurma) REFERENCES Turma(IdTurma),
CONSTRAINT [PK_CursoTurma] PRIMARY KEY CLUSTERED
(
	IdCursoTurma ASC
))
GO
CREATE TABLE Questao(
	IdQuestao INT NOT NULL,
	IdDisciplina INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdTurma INT NOT NULL,
	NumeroQuestao INT NOT NULL,
	DataLimiteEntrega DATE NOT NULL,
	Descricao TEXT NOT NULL,
	Data DATE NOT NULL,
CONSTRAINT [UQ_NumQuestao] UNIQUE (IdQuestao, NumeroQuestao),
CONSTRAINT [FK_DisciplinaQuestao] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [FK_OfertadaQuestao] FOREIGN KEY (IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_IdTurma] FOREIGN KEY (IdTurma) REFERENCES Turma(IdTurma),
CONSTRAINT [PK_Questao] PRIMARY KEY CLUSTERED
(
	IdQuestao ASC
))
GO
CREATE TABLE ArquivosQuestao(
	IdArquivosQuestao INT NOT NULL,
	IdQuestao INT NOT NULL,
	IdDisciplina INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdTurma INT NOT NULL,
	ArquivoQuestao varchar(500) 
CONSTRAINT [UQ_ArquivoQuestao] UNIQUE (IdArquivosQuestao, ArquivoQuestao),
CONSTRAINT [FK_QuestaoArquivosQuestao] FOREIGN KEY (IdQuestao) REFERENCES Questao(IdQuestao),
CONSTRAINT [FK_DisciplinaArquivosQuestao] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [FK_DisciplinaOfertadaArquivosQuestao] FOREIGN KEY(IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_TurmaArquivoQuestao] FOREIGN KEY (IdTurma) REFERENCES Turma(IdTurma),
CONSTRAINT [PK_ArquivosQuestao] PRIMARY KEY CLUSTERED
(
	IdArquivosQuestao ASC
))
GO
CREATE TABLE Resposta(
	IdResposta INT NOT NULL,
	IdDisciplina INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdTurma INT NOT NULL,
	IdQuestao INT NOT NULL,
	IdAluno INT NOT NULL,
	DataAvaliacao DATE NOT NULL,
	Nota DECIMAL(4,2) NOT NULL,
	Avaliacao TEXT NOT NULL,
	Descricao TEXT NOT NULL,
	DataDeEnvio DATE NOT NULL,
CONSTRAINT [FK_DisciplinaResposta] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [FK_DisciplinaOfertadaResposta] FOREIGN KEY(IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_TurmaResposta] FOREIGN KEY (IdTurma) REFERENCES Turma(IdTurma),
CONSTRAINT [FK_QuestaoResposta] FOREIGN KEY (IdQuestao) REFERENCES Questao(IdQuestao),
CONSTRAINT [FK_AlunoResposta] FOREIGN KEY (IdAluno) REFERENCES Aluno(IdAluno),
CONSTRAINT [PK_Resposta] PRIMARY KEY CLUSTERED
(
	IdResposta ASC
))
GO
CREATE TABLE ArquivosRespostas(
	IdArquivoResposta INT NOT NULL,
	IdDisciplina INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdTurma INT NOT NULL,
	IdQuestao INT NOT NULL,
	IdAluno INT NOT NULL,
	IdResposta INT NOT NULL,
	ArquivoResposta VARCHAR(500) NOT NULL,
CONSTRAINT [UQ_ArquivoResposta] UNIQUE(IdArquivoResposta, ArquivoResposta),
CONSTRAINT [FK_DisciplinaArquivosRespostas] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [FK_DisciplinaOfertadaArquivosRespostas] FOREIGN KEY(IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_TurmaArquivosRespostas] FOREIGN KEY (IdTurma) REFERENCES Turma(IdTurma),
CONSTRAINT [FK_QuestaoArquivosRespostas] FOREIGN KEY (IdQuestao) REFERENCES Questao(IdQuestao),
CONSTRAINT [FK_AlunoArquivosRespostas] FOREIGN KEY (IdAluno) REFERENCES Aluno(IdAluno),
CONSTRAINT [FK_RespostaArquivosRespostas] FOREIGN KEY (IdResposta) REFERENCES Resposta(IdResposta),
CONSTRAINT [PK_ArquivosRespostas] PRIMARY KEY CLUSTERED
(
	IdArquivoResposta ASC
))
GO
CREATE TABLE Matricula(
	IdMatricula INT NOT NULL,
	IdAluno INT NOT NULL,
	IdDisciplina INT NOT NULL,
	IdDisciplinaOfertada INT NOT NULL,
	IdTurma INT NOT NULL,
CONSTRAINT [FK_AlunoMatricula] FOREIGN KEY (IdAluno) REFERENCES Aluno(IdAluno),
CONSTRAINT [FK_DisciplinaMatricula] FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(IdDisciplina),
CONSTRAINT [FK_DisciplinaOfertadaAMatricula] FOREIGN KEY(IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(IdDisciplinaOfertada),
CONSTRAINT [FK_TurmaMatricula] FOREIGN KEY (IdTurma) REFERENCES Turma(IdTurma),
CONSTRAINT [PK_Matricula] PRIMARY KEY CLUSTERED
(
	IdMatricula ASC
))