def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print("Bem vindo, Administrador")
    else:
        print("Bem vindo, usuario")
loginUsuario("admin")
loginUsuario("Admin")
loginUsuario("user")
loginUsuario("ADMIM")

