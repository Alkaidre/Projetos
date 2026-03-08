package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class FabricarConexao {

	private static final String url = "jdbc:mysql://localhost:3306/Projetobancodedados";
	private static final String usuario = "root";
	private static final String senha = "Lu$33010108";

	public static Connection getConnection() throws SQLException {
		return DriverManager.getConnection(url, usuario, senha);
	}

}