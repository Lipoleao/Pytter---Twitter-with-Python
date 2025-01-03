from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)


def display_logo():
    logo = ("""
        _____    _____      _____  _________________  _________________      ______        _____
    ___|\    \  |\    \    /    /|/                 \/                 \ ___|\     \   ___|\    \.
    |    |\    \ | \    \  /    / |\______     ______/\______     ______/|     \     \ |    |\    \.
    |    | |    ||  \____\/    /  /   \( /    /  )/      \( /    /  )/   |     ,_____/||    | |    |
    |    |/____/| \ |    /    /  /     ' |   |   '        ' |   |   '    |     \--'\_|/|    |/____/
    |    ||    ||  \|___/    /  /        |   |              |   |        |     /___/|  |    |\    \.
    |    ||____|/      /    /  /        /   //             /   //        |     \____|\ |    | |    |
    |____|            /____/  /        /___//             /___//         |____ '     /||____| |____|
    |    |           |`    | /        |`   |             |`   |          |    /_____/ ||    | |    |
    |____|           |_____|/         |____|             |____|          |____|     | /|____| |____|
    \(                )/              \(                 \(              \( |_____|/   \(     )/
    '                '                '                  '               '    )/       '     '
                                                                                '
            """)

    print(Fore.CYAN + logo)

def colorful_menu():
    cl_menu = (
        Fore.CYAN + "   Bem-vindo ao Pytter! sua alternativa agora que o Twit... perdâo, o X foi bloqueado em nosso país.\n" +
        Fore.WHITE + "   Primeiro, deixe-nos conhecer você.\n"
    )

    print(cl_menu)

def display_cadastro():
    cadastro_page = (
        Fore.CYAN + "\n════════════════════════════════════════════════\n" +
        Fore.WHITE + "\nPara tirar proveito do Pytter pedimos que você crie uma conta, ou caso ja a possua, basta fazer o login.\n" +
        Fore.MAGENTA + "\n1) " + Fore.WHITE + "Fazer Login\n" +
        Fore.GREEN + "2) " + Fore.WHITE + "Criar Conta\n"+
        Fore.RED + "0) Fechar Programa\n"
    )
    print(cadastro_page)

def display_escolha_acao():
    escolha_acao = (
            Fore.CYAN+"\n╔═════════════════════════════════════════╗\n"+
            "║      Escolha uma das opções abaixo      ║\n"+
            "║                                         ║\n"+
            "║    "+ Fore.RED + "0 - Voltar"+Fore.CYAN+"                           ║\n"+
            "║    "+Fore.MAGENTA+"1"+ Fore.WHITE+" - Ver o feed"+Fore.CYAN+"                       ║\n"+
            "║    "+Fore.GREEN+"2"+ Fore.WHITE+" - Fazer um post"+ Fore.CYAN+"                    ║\n"+
            "║    "+ Fore.BLUE+"3"+ Fore.WHITE+" - Mensagens privadas"+ Fore.CYAN+"               ║\n"+
            "║                                         ║\n"+
            "╚═════════════════════════════════════════╝\n"
    )
    print(escolha_acao)

def display_opcoes_chat():
    menu_chat = (
        Fore.CYAN+
          "╔═══════════════════════════════════════╗\n"+
          "║                                       ║\n"+
          "║   "+Fore.GREEN+"1"+Fore.WHITE+" - Vizualizar Mensagens recebidas"+Fore.CYAN+"  ║\n"+
          "║   "+Fore.BLUE+"2"+Fore.WHITE+" - Enviar mensagens"+Fore.CYAN+"                ║\n"+
          "║   "+Fore.RED+"0 - Voltar"+Fore.CYAN+"                          ║\n"+
          "╚═══════════════════════════════════════╝\n"
    )
    print(menu_chat)
