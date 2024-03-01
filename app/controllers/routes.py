from app import app, db
from flask import render_template, url_for, jsonify

from app.models.forms import ProdutoForm
from app.models.tables import Produto


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = ProdutoForm()
    success = False

    if form.validate_on_submit():
        produto = Produto(nome=str(form.nome.data).strip(),
                          preco=str(form.preco.data).strip(),
                          descricao=str(form.descricao.data).strip())
        db.session.add(produto)
        db.session.commit()
        form = ProdutoForm(formdata=None)
        success = True
    else:
        print(form.errors)

    context = {
        'form': form,
        'success': success,
        'tipo': 'Cadastrar',
        'action': url_for('cadastrar'),
        'finalizado': 'cadastrado'
    }

    return render_template('cadastro.html', **context)


@app.route('/', methods=['GET'])
@app.route('/listar', methods=['GET'])
def listar():
    produtos_db = Produto.query.all()
    produtos = [{'id': x.id, 'nome': x.nome, 'preco': x.preco, 'descricao': x.descricao} for x in produtos_db]

    return render_template('listar.html', produtos=produtos)


@app.route('/editar/<id_produto>', methods=['GET', 'POST'])
def editar(id_produto):
    form = ProdutoForm()
    produto = Produto.query.get_or_404(id_produto)
    success = False

    print(form.data)
    if form.validate_on_submit():
        form.populate_obj(produto)
        db.session.commit()
        form = ProdutoForm(formdata=None)
        success = True
    else:
        print(form.errors)

    form.nome.data = produto.nome
    form.preco.data = produto.preco
    form.descricao.data = produto.descricao

    context = {
        'form': form,
        'produto': produto,
        'tipo': 'Editar',
        'action': url_for('editar', id_produto=produto.id),
        'finalizado': 'editado',
        'success': success
    }

    return render_template('cadastro.html', **context)


@app.route('/deletar/<id_produto>', methods=['DELETE'])
def deletar(id_produto):
    produto = Produto.query.get_or_404(id_produto)
    db.session.delete(produto)
    db.session.commit()

    return jsonify({'message': f'produto {id_produto} deletado com sucesso'}), 200
