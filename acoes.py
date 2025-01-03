import menu
import funcoes
from colorama import Fore, Back, Style, init

def menu_acao(escolha, user: funcoes.Usuario):
    while True:
        if escolha == 1:
            print(Fore.CYAN + "\n════════════════════════════════════════════════\n")
            print(Fore.CYAN +"Este é o feed do Pytter, suas postagens aqui são públicas, então você pode compartilhar o que pensa com todos os usuários!\n")
            funcoes.posts_page()
            print(Fore.CYAN+"\nAperte "+Fore.YELLOW +"Enter "+Fore.CYAN+"para voltar")
            sairOuNao = input("")
            if sairOuNao == '':

                return print(Fore.LIGHTBLACK_EX+"Voltando...")

        elif escolha == 2:
            print(Fore.CYAN + "\n════════════════════════════════════════════════\n")
            print(Fore.CYAN +"Poste algo no feed! Apenas se lembre que o que dizer poderá ser visto por todos os usuários ;)\n")
            conteudo_post = input("Digite:")
            funcoes.publicar_posts(user,conteudo_post)
            print(Fore.CYAN+"\nAperte "+Fore.YELLOW +"Enter "+Fore.CYAN+"para voltar")
            sairOuNao = input("")
            if sairOuNao == '':
                return print(Fore.LIGHTBLACK_EX+"Voltando...")

        elif escolha == 3:
            print(Fore.CYAN + "════════════════════════════════════════════════\n")
            print("Envie e receba mensagens privadas dentro da nossa plataforma\n")
            while True:
                menu.display_opcoes_chat()
                opcao = int(input(Fore.LIGHTBLACK_EX+"Selecione sua ação: "))
                if opcao == 1:
                    print(Fore.YELLOW+"\nEste é seu histórico de mensagens:\n")
                    funcoes.display_mensagens_privadas(user)
                    print(Fore.CYAN+"\nAperte "+Fore.YELLOW +"Enter "+Fore.CYAN+"para voltar")
                    sairOuNao = input("")
                    if sairOuNao != '':
                        break
                elif opcao == 2:
                    users = funcoes.get_all_users()
                    print(Fore.CYAN+"\nTodos os usuários cadastrados:\n")
                    for i, user in enumerate(users, 1):
                        print(Fore.MAGENTA+f"{i}"+Fore.WHITE+f". {user.name}")
                    escolha_de_usuario = int(input("\nEscreva o número da pessoa que você deseja mandar mensagem: ")) - 1
                    destinatario = users[escolha_de_usuario]
                    print(Fore.RED+"\nAperte "+Fore.YELLOW +"Enter "+Fore.RED+"para voltar")
                    while True:
                        conteudo_msg = input(Fore.GREEN+"Digite sua mensagem: "+Fore.WHITE)
                        if conteudo_msg == '':
                            print(Fore.RED+"Voltando...\n")
                            break
                        funcoes.enviar_mensagem_privada(user, destinatario, conteudo_msg)
                elif opcao == 0:
                    return print(Fore.LIGHTBLACK_EX+"Voltando...")
                
                elif opcao > 2:
                    print(Fore.RED+"Insira uma opção válida")
                    break
