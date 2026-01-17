def generate_response(email_text: str, categoria: str) -> str:
    """
    Gera uma resposta automática segura e corporativa
    baseada na categoria do email.
    """

    if categoria == "Produtivo":
        return (
            "Olá, recebemos sua solicitação e ela está em análise. "
            "Em breve retornaremos com mais informações."
        )

    return "Agradecemos sua mensagem e desejamos um excelente dia."
