from supabase import create_client, Client
from colorama import Fore, Back, Style, init
import datetime
import re
import sys


url = 'https://vtmnioufopvxthauqbid.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ0bW5pb3Vmb3B2eHRoYXVxYmlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjQ4NjM4MTksImV4cCI6MjA0MDQzOTgxOX0.uWOlYu-E3BtFzVUUL5KRP7Sork7ycMVhI8qrVWPnRro'
supabase: Client = create_client(url, key)


class Usuario:
  def __init__(usuario,  id, name, email):
    usuario.id = id
    usuario.name = name
    usuario.email = email


# ----------------- User interaction --------------

def validacao_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(email_regex, email))

def create_user(nomeCadastro,emailCadastro,senhaCadastro):
      if not validacao_email(emailCadastro):
        print(Fore.RED + "\nFormato de email incorreto.")
        print(Fore.BLUE+"\n1) "+Fore.WHITE+ "Retornar ao ínicio\n"+Fore.RED+"2) Fechar programa")
        try:
            opc_fechar = int(input())
            if opc_fechar == 1:
                return None
            else:
                fechar_programa()
        except:
            print(Fore.RED+"Opção inválida")
            fechar_programa()
      if len(senhaCadastro) < 6:
        print(Fore.RED + "\nA senha tem que ter no minímo 6 caracteres.")
        print(Fore.BLUE+"\n1) "+Fore.WHITE+ "Retornar ao ínicio\n"+Fore.RED+"2) Fechar programa")
        try:
            opc_fechar = int(input())
            if opc_fechar == 1:
                return None
            else:
                fechar_programa()
        except:
            print(Fore.RED+"Opção inválida")
            fechar_programa()

      cadastrar = supabase.auth.sign_up({
          "email": emailCadastro,
          "password": senhaCadastro
      })
      user_id = cadastrar.user.id
      profile_response = supabase.table("profiles").insert({
            'id': user_id,
            'name': nomeCadastro,
            'email': emailCadastro
      }).execute()

      perfil = supabase.table("profiles").select("name").execute()

      if len(profile_response.data) == 0:
          raise Exception("Erro ao criar seu usuário")
      print(f"Conta criada com sucesso: {nomeCadastro} ({emailCadastro})")

      return Usuario(id=user_id, email=emailCadastro, name=perfil.data)


def login_user(emailLogin,senhaLogin):
    if not validacao_email(emailLogin):
        print(Fore.RED + "\nFormato de email incorreto.")
        print(Fore.BLUE+"\n1) "+Fore.WHITE+ "Retornar ao ínicio\n"+Fore.RED+"2) Fechar programa")
        try:
            opc_fechar = int(input())
            if opc_fechar == 1:
                return None
            else:
                fechar_programa()
        except:
            print(Fore.RED+"Opção inválida")
            fechar_programa()
    if len(senhaLogin) < 6:
        print(Fore.RED + "\nA senha tem que ter no minímo 6 caracteres.")
        print(Fore.BLUE+"\n1) "+Fore.WHITE+ "Retornar ao ínicio\n"+Fore.RED+"2) Fechar programa")
        try:
            opc_fechar = int(input())
            if opc_fechar == 1:
                return None
            else:
                fechar_programa()
        except:
            print(Fore.RED+"Opção inválida")
            fechar_programa()
    try:
      login = supabase.auth.sign_in_with_password({
          "email": emailLogin,
          "password": senhaLogin
      })
      user_id = login.user.id
      perfil = supabase.table("profiles").select("name").eq('id',user_id).execute()

      return Usuario(id=user_id, email=emailLogin, name=perfil.data)

    except:
        print(Fore.RED+"Email/Senha inválidos")
        print(Fore.MAGENTA+"\n1) "+Fore.WHITE+ "Retornar ao ínicio\n"+Fore.RED+"2) Fechar programa")
        try:
            opc_fechar = int(input())
            if opc_fechar == 1:
                return None
            else:
                fechar_programa()
        except:
            print(Fore.RED+"Opção inválida")
            fechar_programa()

# ---------------------------------------------

def fechar_programa():
    print(Fore.RED+"Fechando...")
    sys.exit()

# ---------------- Table interactions   ---------------------------

def publicar_posts(emissor: Usuario, conteudo_post):
    timestamp = datetime.datetime.now().isoformat()
    postar = supabase.table('posts_publicos').insert({
        'conteudo_post': conteudo_post,
        'emissor_id': emissor.id,
        'timestamp_post': timestamp
    }).execute()
    print(Fore.GREEN+"Post enviado com sucesso!")

def formatar_posts(id_post):
    info = carregar_posts(id_post)
    for coisas in info:
      emissor_name = get_user_name(coisas['emissor_id'])
      for nome in emissor_name:
        final_post = (
            Fore.CYAN+
            f"{nome['name']}\n" + Fore.WHITE+
            f"{coisas['conteudo_post']}\n" + Fore.LIGHTBLACK_EX+
            f"{coisas['timestamp_post']}\n"
        ) 
    print(final_post)

def carregar_posts(id_post):
    get_posts = supabase.table('posts_publicos').select('id,conteudo_post,emissor_id,timestamp_post').eq('id',id_post).execute()
    return get_posts.data

def get_user_name(user_id):
    user_name = supabase.table('profiles').select('name').eq('id', user_id).execute()
    return user_name.data

def get_all_users():
    response = supabase.table("profiles").select("id, email, name").execute()
    return [Usuario(id=user['id'], email=user['email'], name=user['name']) for user in response.data]



# ------------------------------- mensagens ---------------------------------

def enviar_mensagem_privada(remetente: Usuario, destinatario: Usuario, conteudo_msg):
    timestamp = datetime.datetime.now().isoformat()
    data = supabase.table("private_messages").insert({
        "remetente_id": remetente.id,
        "destinatario_id": destinatario.id,
        "conteudo": conteudo_msg,
        "timestamp": timestamp
    }).execute()
    print(Fore.CYAN + f"Mensagem enviada para "+Fore.YELLOW+f"{destinatario.name}"+Fore.WHITE+f": {conteudo_msg}")


def receber_mensagem_privada(user: Usuario):
    receber = supabase.table('private_messages').select('*').or_(f'destinatario_id.eq.{user.id},remetente_id.eq.{user.id}')
    menssages = receber.execute()
    return menssages.data

def display_mensagens_privadas(user: Usuario):
    messages = receber_mensagem_privada(user)

    for message in messages:
        nome_remetente = get_user_name(message['remetente_id'])
        nome_destinatario = get_user_name(message['destinatario_id'])
        for nomeR in nome_remetente:
          for nomeD in nome_destinatario:
            if message['remetente_id'] == user.id:
                print(Fore.LIGHTBLACK_EX + f"[{message['timestamp']}]"+Fore.CYAN +" You"+Fore.YELLOW +" -> "+ Fore.GREEN+ f"{nomeD['name']}"+Fore.WHITE+f": {message['conteudo']}")
            else:
                print(Fore.LIGHTBLACK_EX + f"[{message['timestamp']}]" + Fore.GREEN + f"{nomeR['name']} "+Fore.YELLOW+"->" + Fore.CYAN+ " You" + Fore.WHITE+f": {message['conteudo']}")



# --------------------------------------------------------------------------

def posts_page():
  i = 1
  while True:
    try:
      formatar_posts(i)
      i += 1
    except:
      print("Esses foram todos os posts até em tão!")
      break