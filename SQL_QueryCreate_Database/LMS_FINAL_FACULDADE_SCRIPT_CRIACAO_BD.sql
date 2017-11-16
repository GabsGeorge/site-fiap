CREATE DATABASE Faculdade
GO
USE Faculdade
GO
CREATE TABLE Disciplina(
	Nome varchar(240) NOT NULL,
	CargaHoraria tinyint NOT NULL,
	Teoria decimal(3) NOT NULL,
	Pratica decimal(3) NOT NULL,
	Ementa text NOT NULL,
	Competencias text NOT NULL,
	Habilidades text NOT NULL,
	Conteudo text NOT NULL,
	Bibliografia_Basica text NOT NULL,
	Biblioteca_complementar	text NOT NULL,
CONSTRAINT [UQ_DisciplinaNome]	UNIQUE (Nome)
)
GO
CREATE TABLE Curso(
	Sigla varchar(5) NOT NULL,
	Nome varchar(50) NOT NULL,
CONSTRAINT [UQ_CursoSigla]	UNIQUE (Sigla),
CONSTRAINT [UQ_CursoNome]	UNIQUE (Nome)
)
GO
CREATE TABLE Aluno(
	RA_Aluno int NOT NULL,
	Nome varchar(120) NOT NULL,
	Email varchar(80) NOT NULL,
	Celular char(11) NOT NULL,
	Sigla_Curso varchar(5) NOT NULL,
CONSTRAINT [UQ_AlunoRA]			UNIQUE (RA_Aluno),
CONSTRAINT [FK_AlunoCurso]		FOREIGN KEY (Sigla_Curso) REFERENCES Curso(Sigla)
)
GO
CREATE TABLE GradeCurricular(
	Sigla_Curso varchar(5) NOT NULL,
	Ano smallint NOT NULL,
	Semestre char(1) NOT NULL,
CONSTRAINT [UQ_GradeCurricularAno]			UNIQUE (Ano),
CONSTRAINT [UQ_GradeCurricularSemestre]		UNIQUE (Semestre),
CONSTRAINT [FK_CursoGradeCurricular]		FOREIGN KEY (Sigla_Curso) REFERENCES Curso(Sigla)
)
GO
CREATE TABLE Periodo(
	Sigla_Curso varchar(5) NOT NULL,
	Ano_Grade smallint NOT NULL,
	Semestre_Grade char(1) NOT NULL,
	NumeroPeriodo tinyint NOT NULL,
CONSTRAINT [UQ_PeriodoNumero]							UNIQUE (NumeroPeriodo),
CONSTRAINT [FK_CursoPeriodo]							FOREIGN KEY (Sigla_Curso)		REFERENCES Curso(Sigla),
CONSTRAINT [FK_SemestreGradeCurricularAnoPeriodo]		FOREIGN KEY (Ano_Grade)			REFERENCES GradeCurricular(Ano),
CONSTRAINT [FK_SemestreGradeCurricularSemestrePeriodo]	FOREIGN KEY (Semestre_Grade)	REFERENCES GradeCurricular(Semestre)

)
GO
CREATE TABLE PeriodoDisciplina(
	Sigla_Curso varchar(5) NOT NULL,
	Ano_Grade smallint NOT NULL,
	Semestre_Grade char(1) NOT NULL,
	Numero_Periodo tinyint NOT NULL,
	Nome_Disciplina varchar(240) NOT NULL,
CONSTRAINT [FK_CursoPeriodoDisciplina]					FOREIGN KEY (Sigla_Curso)		REFERENCES Curso(Sigla),
CONSTRAINT [FK_SemestreGradeCurricularPerDisciplina]	FOREIGN KEY (Semestre_Grade)	REFERENCES GradeCurricular(Semestre),
CONSTRAINT [FK_AnoGradeCurricularPerDisciplina]			FOREIGN KEY (Ano_Grade)			REFERENCES GradeCurricular(Ano),
CONSTRAINT [FK_PeriodoDisciplinaPeriodo]				FOREIGN KEY (Numero_Periodo)	REFERENCES Periodo(NumeroPeriodo),
CONSTRAINT [FK_DisciplinaPeriodoDisciplina]				FOREIGN KEY (Nome_Disciplina)	REFERENCES Disciplina(Nome)
)
GO
CREATE TABLE DisciplinaOfertada(
	Nome_Disciplina varchar(240) NOT NULL,
	AnoOfertado smallint NOT NULL,
	SemestreOfertado char(1) NOT NULL,
CONSTRAINT [UQ_DisciplinaOfertadaAno]				UNIQUE (AnoOfertado),
CONSTRAINT [UQ_DisciplinaOfertadaSemestre]			UNIQUE (SemestreOfertado),
CONSTRAINT [FK_DisciplinaDisciplinaOfertada]		FOREIGN KEY (Nome_Disciplina) REFERENCES Disciplina(Nome),
)
GO
CREATE TABLE Professor(
	RA_Professor int NOT NULL,
	Apelido varchar(30) NOT NULL,
	Nome varchar(30) NOT NULL,
	Email varchar(120) NOT NULL,
	Celular char(11) NOT NULL,
CONSTRAINT [UQ_ProfessorRA]			UNIQUE(RA_Professor),
CONSTRAINT [UQ_ProfessorApelido]	UNIQUE(Apelido)
)
GO
CREATE TABLE Turma(
	Nome_Disciplina varchar(240) NOT NULL,
	Ano_Ofertado smallint NOT NULL,
	Semestre_Ofertado char(1) NOT NULL,
	Id_Turma char(1) NOT NULL,
	RA_Professor int NOT NULL,
	Turno varchar(15) NOT NULL,
CONSTRAINT [UQ_Id_Turma] UNIQUE (Id_Turma),
CONSTRAINT [FK_DisciplinaTurma]					FOREIGN KEY (Nome_Disciplina)			REFERENCES Disciplina(Nome),
CONSTRAINT [FK_DisciplinaOfertadaAnoTurma]		FOREIGN KEY (Ano_Ofertado)				REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_DisciplinaOfertadaSemestreTurma]	FOREIGN KEY (Semestre_Ofertado)			REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_ProfessorTurma]					FOREIGN KEY (RA_Professor)				REFERENCES Professor(RA_Professor)
)
GO
CREATE TABLE CursoTurma(
	Sigla_Curso varchar(5)	NOT NULL,
	Nome_Disciplina varchar(240) NOT NULL,
	Ano_Ofertado smallint NOT NULL,
	Semestre_Ofertado char(1) NOT NULL,
	Id_Turma char(1) NOT NULL,
CONSTRAINT [FK_CursoCursoTurma]							FOREIGN KEY (Sigla_Curso)						REFERENCES Curso(Sigla),
CONSTRAINT [FK_DisciplinaCursoTurma]					FOREIGN KEY (Nome_Disciplina)					REFERENCES Disciplina(Nome),
CONSTRAINT [FK_DisciplinaOfertadaAnoCursoTurma]			FOREIGN KEY (Ano_Ofertado)						REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_DisciplinaOfertadaSemestreCursoTurma]	FOREIGN KEY (Semestre_Ofertado)					REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_TurmaCursoTurma]							FOREIGN KEY (Id_Turma)							REFERENCES Turma(Id_Turma)
)
GO
CREATE TABLE Questao(
	Nome_Discplina varchar(240) NOT NULL,
	Ano_Ofertado smallint NOT NULL,
	Semestre_Ofertado char(1) NOT NULL,
	Id_Turma char(1) NOT NULL,
	NumeroQuestao int NOT NULL,
	DataLimiteEntrega date NOT NULL,
	Descricao text NOT NULL,
	Data date NOT NULL,
CONSTRAINT [UQ_NumQuestao]						UNIQUE (NumeroQuestao),
CONSTRAINT [FK_DisciplinaQuestao]				FOREIGN KEY (Nome_Discplina)	REFERENCES Disciplina(Nome),
CONSTRAINT [FK_OfertadaQuestaoAno]				FOREIGN KEY (Ano_Ofertado)		REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_OfertadaQuestaoSemestre]			FOREIGN KEY (Semestre_Ofertado) REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_IdTurma] FOREIGN KEY (Id_Turma)	REFERENCES Turma(Id_Turma)
)
GO
CREATE TABLE ArquivosQuestao(
	Nome_Disciplina varchar(240) NOT NULL,
	Ano_Ofertado smallint NOT NULL,
	Semestre_Ofertado char(1) NOT NULL,
	Id_Turma char(1) NOT NULL,
	Numero_Questao int NOT NULL,
	ArquivoQuestao varchar(500) 
CONSTRAINT [UQ_QuestaoArquivo]								UNIQUE (ArquivoQuestao),
CONSTRAINT [FK_QuestaoArquivosQuestao]						FOREIGN KEY (Numero_Questao)	REFERENCES Questao(NumeroQuestao),
CONSTRAINT [FK_DisciplinaArquivosQuestao]					FOREIGN KEY (Nome_Disciplina)	REFERENCES Disciplina(Nome),
CONSTRAINT [FK_DisciplinaOfertadaAnoArquivosQuestao]		FOREIGN KEY(Ano_Ofertado)		REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_DisciplinaOfertadaSemestreArquivosQuestao]	FOREIGN KEY(Semestre_Ofertado)	REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_TurmaArquivoQuestao]							FOREIGN KEY (Id_Turma)			REFERENCES Turma(Id_Turma)
)
GO
CREATE TABLE Resposta(
	Nome_Disciplina varchar(240) NOT NULL,
	Ano_Ofertado smallint NOT NULL,
	Id_Turma char (1) NOT NULL,
	Numero_Questao int NOT NULL,
	Semestre_Ofertado char(1) NOT NULL,
	RA_Aluno int NOT NULL,
	DataAvaliacao date NOT NULL,
	Nota decimal(4,2) NOT NULL,
	Avaliacao text NOT NULL,
	Descricao text NOT NULL,
	DataDeEnvio date NOT NULL,
CONSTRAINT [UQ_Aluno_RA]								UNIQUE (RA_Aluno),
CONSTRAINT [FK_DisciplinaResposta]						FOREIGN KEY (Nome_Disciplina)	REFERENCES Disciplina(Nome),
CONSTRAINT [FK_DisciplinaOfertadaAnoResposta]			FOREIGN KEY(Ano_Ofertado)		REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_DisciplinaOfertadaSemestreResposta]		FOREIGN KEY(Semestre_Ofertado)	REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_TurmaResposta]							FOREIGN KEY (Id_Turma)			REFERENCES Turma(Id_Turma),
CONSTRAINT [FK_QuestaoResposta]							FOREIGN KEY (Numero_Questao)	REFERENCES Questao(NumeroQuestao)
)
GO
CREATE TABLE ArquivosRespostas(
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	Id_Turma CHAR(1) NOT NULL,
	Numero_Questao INT NOT NULL,
	RA_Aluno INT NOT NULL,
	ArquivoResposta VARCHAR(500) NOT NULL,
CONSTRAINT [UQ_ArquivoResposta]										UNIQUE(ArquivoResposta),
CONSTRAINT [FK_DisciplinaArquivosRespostas]							FOREIGN KEY (Nome_Disciplina)	REFERENCES Disciplina(Nome),
CONSTRAINT [FK_DisciplinaOfertadaArquivosAnoRespostas]				FOREIGN KEY(Ano_Ofertado)		REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_DisciplinaOfertadaArquivosSemestreRespostas]			FOREIGN KEY(Semestre_Ofertado)	REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_TurmaArquivosRespostas]								FOREIGN KEY (Id_Turma)			REFERENCES Turma(Id_Turma),
CONSTRAINT [FK_QuestaoArquivosRespostas]							FOREIGN KEY (Numero_Questao)	REFERENCES Questao(NumeroQuestao),
CONSTRAINT [FK_AlunoArquivosRespostas]								FOREIGN KEY (RA_Aluno)			REFERENCES Aluno(RA_Aluno)
)	
GO
CREATE TABLE Matricula(
	RA_Aluno INT NOT NULL,
	Nome_Disciplina VARCHAR(240) NOT NULL,
	Ano_Ofertado SMALLINT NOT NULL,
	Semestre_Ofertado CHAR(1) NOT NULL,
	Id_Turma CHAR (1) NOT NULL,
CONSTRAINT [FK_AlunoMatricula]									FOREIGN KEY (RA_Aluno)				REFERENCES Aluno(RA_Aluno),
CONSTRAINT [FK_DisciplinaMatricula]								FOREIGN KEY (Nome_Disciplina)		REFERENCES Disciplina(Nome),
CONSTRAINT [FK_DisciplinaOfertadaAnoAMatricula]					FOREIGN KEY(Ano_Ofertado)			REFERENCES DisciplinaOfertada(AnoOfertado),
CONSTRAINT [FK_DisciplinaOfertadaSemestreAMatricula]			FOREIGN KEY(Semestre_Ofertado)		REFERENCES DisciplinaOfertada(SemestreOfertado),
CONSTRAINT [FK_TurmaMatricula] FOREIGN KEY (Id_Turma)			REFERENCES Turma(Id_Turma)
)