import sqlite3

def conectar(cnn:str):
    """_summary_

    Args:
        cnn (str): caminho para conexão

    Returns:
        cnn: retorna uma conexão
    """
    conn = sqlite3.connect(cnn)
    return conn

def criar_tabela(cnn:sqlite3.Connection):
    """Cria a tabela se não existir

    Args:
        conn (sqlite3.Connection): conexão inde sera criada a tabela
    """    
    sql = """
    CREATE TABLE IF NOT EXISTS produtos (
        nr INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        marca TEXT NOT NULL,
        codigo INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    );
    """
    cnn.execute(sql)
    cnn.commit()

def inserir(conn:sqlite3.Connection,
                        nome:str,
                        marca:str,
                        codigo:int,
                        quantidade:int,
                        preco:float):
 
    
    sql = """
    INSERT INTO produtos (nome, marca, codigo, quantidade, preco)
    VALUES (?, ?, ?, ?,?);
    """
    conn.execute(sql, (nome, marca, codigo, quantidade, preco))
    conn.commit()

def consultar_produto(conn:sqlite3.Connection, codigo:int = None, nome: str = None):
    """Consulta as advertencias do usuario

    Args:
        conn (sqlite3.Connection): Conexão com banco
        user_id (int): id do usuario

    Returns:
        list: retorna uma lista com o numero da advertencia, id do user, e motivo da advertencia
    """
    if codigo:
        sql = "SELECT * FROM produtos WHERE codigo = ?;"
        cursor = conn.execute(sql, (codigo,))
        return cursor.fetchall()
    if nome:
        sql = "SELECT * FROM produtos WHERE nome = ?;"
        cursor = conn.execute(sql, (nome,))
        return cursor.fetchall()