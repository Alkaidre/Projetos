package jdbc;

import java.time.LocalDate;

public class Pessoa {

	int id;
	String nome;
	String email;
	String cpf;
	LocalDate dataDeNascimento;

	public Pessoa(String nome, String email, String cpf, LocalDate dataDeNascimento) {
		this.nome = nome;
		this.email = email;
		this.cpf = cpf;
		this.dataDeNascimento = dataDeNascimento;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public LocalDate getDataDeNascimento() {
		return dataDeNascimento;
	}

	public void setDataDeNascimento(LocalDate dataDeNascimento) {
		this.dataDeNascimento = dataDeNascimento;
	}

	public void alterarCpf(String novoCpf, Administrador usuario) {

		if (usuario.podeAlterarCpf()) {
			this.cpf = novoCpf;
			System.out.println("CPF alterado com sucesso.");
		} else {
			System.out.println("Usuário não autorizado a alterar CPF.");
		}

	}

	public String getCpf() {
		return cpf;
	}
}