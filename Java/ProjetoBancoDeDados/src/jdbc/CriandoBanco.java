package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class CriandoBanco {

	public static void main(String[] args) throws SQLException {

		final String url = "jdbc:mysql://localhost:3306/";
		final String usuario = "root";
		final String senha = "Lu$33010108";

		Connection conexao = DriverManager.getConnection(url, usuario, senha);
		Statement stmt = conexao.createStatement();

		stmt.execute("CREATE DATABASE IF NOT EXISTS Projetobancodedados");

		System.out.println("Banco de dados criado com sucesso!!!");

		Connection conexaoBanco = DriverManager.getConnection("jdbc:mysql://localhost:3306/Projetobancodedados",
				usuario, senha);

		Statement stmtBanco = conexaoBanco.createStatement();

		String sqlTabela = "CREATE TABLE IF NOT EXISTS Pessoa (" + "id INT AUTO_INCREMENT PRIMARY KEY, "
				+ "nome VARCHAR(100), " + "cpf VARCHAR(11) UNIQUE, " + "dataDeNascimento DATE" + ")";

		stmtBanco.execute(sqlTabela);

		System.out.println("Tabela criada com sucesso!!");

		stmtBanco.close();
		conexaoBanco.close();
		stmt.close();
		conexao.close();
	}
}
