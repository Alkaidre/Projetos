package jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class PessoaDAO {

	Scanner entrada = new Scanner(System.in);
	private Connection conexao;

	public PessoaDAO() throws SQLException {
		this.conexao = FabricarConexao.getConnection();
	}

	String sqlInserir = "INSERT INTO Pessoa ( nome, email, CPF, dataDeNascimento) VALUES (?, ?, ?, ?)";
	String sqlUptadeNome = "UPDATE Pessoa SET nome = ? WHERE id = ? ";
	String sqlUptadeEmail = "UPDATE Pessoa SET email = ? WHERE id = ? ";
	String sqlUptadeNascimento = "UPDATE Pessoa SET dataDeNascimento = ? WHERE id = ? ";
	String sqlConsulta = "SELECT id , nome From Pessoa WHERE nome LIKE ? LIMIT 30";
	String sqlConsultaId = "SELECT id , nome From Pessoa WHERE id = ? LIMIT 30";
	String sqlDeletar = "DELETE FROM Pessoa WHERE id = ?";
	String sqlListarPorNome = "SELECT * FROM Pessoa ORDER BY  nome  Limit 30";
	String sqlListarPorId = "SELECT * FROM Pessoa ORDER BY id Limit 30";

	public void inserir(Pessoa pessoa) throws SQLException {

		PreparedStatement stmt = conexao.prepareStatement(sqlInserir);
		stmt.setString(1, pessoa.getNome());
		stmt.setString(2, pessoa.getEmail());
		stmt.setString(3, pessoa.getCpf());
		stmt.setDate(4, java.sql.Date.valueOf(pessoa.getDataDeNascimento()));
		stmt.executeUpdate();
		stmt.close();

		System.out.println("Pessoa inserida com sucesso!");
	}

	public void Update() throws SQLException {

		System.out.println("Qual codigo deseja alterar: ");
		int pesquisa = entrada.nextInt();
		entrada.nextLine();

		PreparedStatement stmt = conexao.prepareStatement(sqlConsultaId);
		stmt.setInt(1, pesquisa);
		ResultSet rs = stmt.executeQuery();

		if (rs.next()) {
			int id = rs.getInt("id");
			String nome = rs.getString("nome");

			System.out.println("O id selecionado é " + id + " com nome " + nome);

			System.out.println("Qual informação deseja alterar:");
			String resposta = entrada.nextLine();

			if (resposta.equalsIgnoreCase("nome")) {

				System.out.println("Digite o novo nome: ");
				String novoNome = entrada.nextLine();

				PreparedStatement stmtUpdate = conexao.prepareStatement(sqlUptadeNome);
				stmtUpdate.setString(1, novoNome);
				stmtUpdate.setInt(2, pesquisa);

				int linhasAfetadas = stmtUpdate.executeUpdate();
				if (linhasAfetadas > 0) {
					System.out.println("alteração do nome foi realizada com sucesso!!");

				}
				stmtUpdate.close();
			} else if (resposta.equalsIgnoreCase("email")) {

				System.out.println("Digite o novo email: ");
				String novoEmail = entrada.nextLine();

				PreparedStatement stmtUpdate = conexao.prepareStatement(sqlUptadeEmail);
				stmtUpdate.setString(1, novoEmail);
				stmtUpdate.setInt(2, pesquisa);

				int linhasAfetadas = stmtUpdate.executeUpdate();
				if (linhasAfetadas > 0) {
					System.out.println("alteração do Email foi realizada com sucesso!!");
				}
				stmtUpdate.close();

			} else if (resposta.equalsIgnoreCase("datadenascimento") || resposta.equalsIgnoreCase("date")) {

				System.out.println("Digite a nova data de nascimento: ");
				String novoDataDeNascimento = entrada.nextLine();

				PreparedStatement stmtUpdate = conexao.prepareStatement(sqlUptadeNascimento);
				stmtUpdate.setDate(1, java.sql.Date.valueOf(novoDataDeNascimento));
				stmtUpdate.setInt(2, pesquisa);

				int linhasAfetadas = stmtUpdate.executeUpdate();
				if (linhasAfetadas > 0) {
					System.out.println("alteração da data de nascimento foi realizada com sucesso!!");

				}
				stmtUpdate.close();
				rs.close();
				stmt.close();
			}

		}
	}

	public void Consulta() throws SQLException {

		System.out.println("Digite o nome para ser consultado: ");
		String consulta = entrada.nextLine();

		PreparedStatement stmt = conexao.prepareStatement(sqlConsulta);
		stmt.setString(1, "%" + consulta + "%");
		ResultSet resultado = stmt.executeQuery();

		boolean encontrou = false;

		while (resultado.next()) {

			encontrou = true;

			int id = resultado.getInt("id");
			String nome = resultado.getString("nome");

			System.out.println(nome + " , " + id);
		}

		if (!encontrou) {
			System.out.println("Registro nao encontrado!!");
		}
		resultado.close();
		stmt.close();

	}

	public void ConsultaPorId() throws SQLException {

		System.out.println("Digite o id para ser consultado: ");
		int consulta = entrada.nextInt();

		PreparedStatement stmt = conexao.prepareStatement(sqlConsultaId);
		stmt.setInt(1, consulta);
		ResultSet resultado = stmt.executeQuery();

		if (resultado.next()) {
			int id = resultado.getInt("id");
			String nome = resultado.getString("nome");

			System.out.println(nome + " , " + id);

		} else {
			System.out.println("Registro nao encontrado!!");
		}
		resultado.close();
		stmt.close();

	}

	public void Deletar() throws SQLException {
		System.out.println("Qual codigo deseja alterar: ");
		int pesquisa = entrada.nextInt();
		entrada.nextLine();

		PreparedStatement stmt = conexao.prepareStatement(sqlConsultaId);
		stmt.setInt(1, pesquisa);
		ResultSet rs = stmt.executeQuery();

		if (rs.next()) {

			int id = rs.getInt("id");
			String nome = rs.getString("nome");

			System.out.println("O id selecionado e " + id + " o nome e " + nome + ".");

			System.out.println("Deseja deletar esse registro:(S/N) ");
			String resposta = entrada.nextLine();

			if (resposta.equalsIgnoreCase("S")) {

				stmt = conexao.prepareStatement(sqlDeletar);
				stmt.setInt(1, id);

				int linhasAfetadas = stmt.executeUpdate();

				if (linhasAfetadas > 0) {
					System.out.println("Registro apagado com sucesso!!");
				}

			} else {
				System.out.println("Operação cancelada!!");
			}
		} else {
			System.out.println("Codigo nao encontrado!!");
		}
		rs.close();
		stmt.close();
	}

	public void listarPorId() throws SQLException {
		System.out.println("Deseja listar por ID:(S/N) ");
		String resposta = entrada.nextLine();

		if (resposta.equalsIgnoreCase("S")) {

			PreparedStatement stmt = conexao.prepareStatement(sqlListarPorId);
			ResultSet resultado = stmt.executeQuery();

			while (resultado.next()) {
				int id = resultado.getInt("id");
				String nomePessoa = resultado.getString("nome");
				String email = resultado.getString("email");
				String nascimento = resultado.getString("DataDeNascimento");

				System.out.println("ID: " + id + "\nNome: " + nomePessoa + "\nEmail: " + email
						+ "\nData de Nascimento: " + nascimento + ".");

			}
			resultado.close();
			stmt.close();
		} else {

			System.out.println("Programa encerrado!!");

		}

	}

	public void listarPorNome() throws SQLException {
		System.out.println("Deseja listar por nome:(S/N) ");
		String resposta = entrada.nextLine();

		if (resposta.equalsIgnoreCase("S")) {

			PreparedStatement stmt = conexao.prepareStatement(sqlListarPorNome);
			ResultSet resultado = stmt.executeQuery();

			while (resultado.next()) {
				int id = resultado.getInt("id");
				String nomePessoa = resultado.getString("nome");
				String email = resultado.getString("email");
				String nascimento = resultado.getString("DataDeNascimento");

				System.out.println("ID: " + id + "\nNome: " + nomePessoa + "\nEmail: " + email
						+ "\nData de Nascimento: " + nascimento + ".");

			}
			resultado.close();
			stmt.close();
		} else {

			System.out.println("Programa encerrado!!");

		}

	}

}
