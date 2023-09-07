-- Crear la tabla para almacenar metadatos de entregas
CREATE TABLE CGA_META_ENTREGAS (
    ID_ENTREGAS NUMBER GENERATED ALWAYS AS IDENTITY,
    TX_FICHERO VARCHAR2(100),
    TX_FECHA TIMESTAMP,
    LG_TRATADO CHAR(1) CHECK (LG_TRATADO IN ('S', 'N')),
	NU_VERSION VARCHAR2(50),
    CONSTRAINT PK_CGA_META_ENTREGAS PRIMARY KEY (ID_ENTREGAS)
);

-- Agregar comentarios a las columnas
COMMENT ON COLUMN CGA_META_ENTREGAS.ID_ENTREGAS IS 'Identificador único de las entregas';
COMMENT ON COLUMN CGA_META_ENTREGAS.TX_FICHERO IS 'Nombre del fichero entregado';
COMMENT ON COLUMN CGA_META_ENTREGAS.TX_FECHA IS 'Fecha y hora de la entrega';
COMMENT ON COLUMN CGA_META_ENTREGAS.LG_TRATADO IS 'Indica si el fichero fue tratado';
COMMENT ON COLUMN CGA_META_ENTREGAS.NU_VERSION IS 'Versión de la entrega';

COMMENT ON TABLE CGA_META_ENTREGAS IS 'Tabla para almacenar información sobre las entregas SGA';

-- Crear la tabla para almacenar información de tablas y grupos SGA
CREATE TABLE CGA_META_TABLAS_SGA (
    ID_TABLAS_SGA NUMBER GENERATED ALWAYS AS IDENTITY,
    TX_NOMBRE VARCHAR2(100),
    TX_GRUPO_SGA VARCHAR2(50),
    CONSTRAINT PK_CGA_META_TABLAS PRIMARY KEY (ID_TABLAS_SGA)
);

-- Agregar comentarios a las columnas
COMMENT ON COLUMN CGA_META_TABLAS_SGA.ID_TABLAS_SGA IS 'Identificador único de las tablas';
COMMENT ON COLUMN CGA_META_TABLAS_SGA.TX_NOMBRE IS 'Nombre de la tabla';
COMMENT ON COLUMN CGA_META_TABLAS_SGA.TX_GRUPO_SGA IS 'Grupo de SGA al que pertenece la tabla';


COMMENT ON TABLE CGA_META_TABLAS_SGA IS 'Tabla para almacenar información sobre las tablas y grupos SGA'