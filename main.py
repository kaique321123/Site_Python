from flask import Flask, render_template

meu_site = Flask(__name__)

# criar a 1ª pagina do site
# route ->   meuprimeirosite.com/
# função -> o que você quer exibir naquela página
#template
@meu_site.route("/")
def homepage():   #o que vc quer que apareça na página coloca dentro de return
    return render_template("apresentacao.html")

@meu_site.route("/contatos")
def contatos():
    return render_template("contatos.html")


@meu_site.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#para fazer o nome mudar tem que colocar nome_usuario=nome_usuario para que no html o nome_usuario vire uma variável
#e para o html reconhecer colocar dentro de duas chave {{variavel}} ex: {{nome_usuario}}


    #servidor do heroku


# colocar o site no ar
if __name__ == "__main__":
    meu_site.run(debug=True)
#se colocar (debug=True) não precisa ficar atualizando o site toda hora autompático
