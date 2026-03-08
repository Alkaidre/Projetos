package jdbc;

public class Administrador {

	@SuppressWarnings("unused")
	private String nome;
	private boolean podeAlterarCpf;

	public Administrador(String nome, boolean podeAlterarCpf) {
		this.nome = nome;
		this.podeAlterarCpf = podeAlterarCpf;
	}

	public boolean podeAlterarCpf() {
		return podeAlterarCpf;
	}
}
