package jdbc;

import java.sql.SQLException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) throws SQLException {

		Scanner entrada = new Scanner(System.in);
		PessoaDAO dao = new PessoaDAO();

		int opcao = -1;

		while (opcao != 0) {

			System.out.println("\n===== MENU =====");
			System.out.println("1 - Inserir pessoa");
			System.out.println("2 - Atualizar pessoa");
			System.out.println("3 - Buscar pessoa por nome");
			System.out.println("4 - Buscar pessoa por id");
			System.out.println("5 - Deletar pessoa");
			System.out.println("6 - Listar pessoas por nome");
			System.out.println("7 - Listar pessoas por id");
			System.out.println("0 - Sair");
			System.out.print("Escolha uma opção: ");

			opcao = entrada.nextInt();
			entrada.nextLine();

			switch (opcao) {
			case 1:
				System.out.println("Digite o nome:");
				String nome = entrada.nextLine();

				System.out.println("Digite o email:");
				String email = entrada.nextLine();

				System.out.println("Digite o CPF:");
				String cpf = entrada.nextLine();

				System.out.println("Digite a data de nascimento (AAAA-MM-DD):");
				String data = entrada.nextLine().trim();

				DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
				LocalDate nascimento = LocalDate.parse(data, formatter);

				Pessoa pessoa = new Pessoa(nome, email, cpf, nascimento);

				dao.inserir(pessoa);
				break;
			case 2:
				dao.Update();
				break;
			case 3:
				dao.Consulta();
				break;
			case 4:
				dao.ConsultaPorId();
				break;
			case 5:
				dao.Deletar();
				break;
			case 6:
				dao.listarPorNome();
				break;
			case 7:
				dao.listarPorId();
				break;
			case 0:
				System.out.println("Programa encerrado!");
				break;
			default:
				System.out.println("Opção inválida!");
				break;
			}
		}
		entrada.close();
	}

}
