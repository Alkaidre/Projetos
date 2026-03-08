package jdbc;

class PessoaDAOTest {

	void testeInserir() throws Exception {
		PessoaDAO dao = new PessoaDAO();

		Pessoa p = new Pessoa("Teste", "teste@email.com", "123.456.789-00", java.time.LocalDate.of(2000, 1, 1));

		dao.inserir(p);

		assert (true);
	}
}