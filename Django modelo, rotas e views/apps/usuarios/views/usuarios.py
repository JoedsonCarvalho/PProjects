from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):      
    """Cadastra uma pessoa na BD"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, "O nome não pode estar em branco" )
            print("O nome não pode estar em branco")
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, "O email não pode estar em branco")

            print("O email não pode estar em branco")
            return redirect('cadastro')

        if senha_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            print("As senhas 1 e 2 devem ser iguais")
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuário já cadastrado")

            print("Usuário já cadastrado")
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Nome já cadastrado")

            print("Usuário já cadastrado")
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha, )
        user.save()
        print("usuário cadastrado com sucesso")
        print(f"{nome}, {email}, {senha} e {senha2}")
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """Efetua o login de uma pessoa cadastrada"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, "os campos email ou senha não podem ficar vazios")
            print("os campos email ou senha não podem ficar vazios")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                print(user.username)
                messages.success(request, "login realizado com sucesso!!")
                auth.login(request, user)
                print("login realizado com sucesso!!")
                return redirect('dashboard')

        print(email, senha)

    return render(request, 'usuarios/login.html')

def dashboard(request):
    """Renderiza a página principal de um usuário logado"""
    id = request.user.id
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
        
def logout(request):
    """Faz logout de um usuário"""
    auth.logout(request)
    return redirect('index')
    
def campo_vazio(campo):
    """Verifica se um campo está vazio"""
    return not campo.strip();

def senha_nao_sao_iguais(senha, senha2):
    """Verifica a igualdade de duas senhas"""
    return senha != senha2
   

