create database RDR_PDI

-- Tabla de estudiantes
CREATE TABLE Estudiante (
    id INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    apellido NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    foto_url NVARCHAR(255),
    reconocimiento_facial_id NVARCHAR(100) 
);
GO

-- Tabla de docentes
CREATE TABLE Docente (
    id INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    apellido NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    foto_url NVARCHAR(255),
    reconocimiento_facial_id NVARCHAR(100) 
);
GO

-- Tabla de carreras
CREATE TABLE Carrera (
    id INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL
);
GO

-- Tabla de materias
CREATE TABLE Materia (
    id INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    carrera_id INT,
    FOREIGN KEY (carrera_id) REFERENCES Carrera(id)
);
GO

CREATE TABLE Aula (
    id INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    ubicacion NVARCHAR(255) NOT NULL
);
GO

-- Tabla de clases
CREATE TABLE Clase (
    id INT PRIMARY KEY,
    materia_id INT,
    docente_id INT,
    aula_id INT,
    horario NVARCHAR(100),
    FOREIGN KEY (materia_id) REFERENCES Materia(id),
    FOREIGN KEY (docente_id) REFERENCES Docente(id),
    FOREIGN KEY (aula_id) REFERENCES Aula(id)
);
GO

-- Tabla de asistencias
CREATE TABLE Asistencia (
    id INT PRIMARY KEY,
    clase_id INT,
    estudiante_id INT,
    fecha DATE,
    presente BIT,
    FOREIGN KEY (clase_id) REFERENCES Clase(id),
    FOREIGN KEY (estudiante_id) REFERENCES Estudiante(id)
);
GO
