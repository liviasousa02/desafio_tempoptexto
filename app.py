from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

codigo = """```python
def formatDuration(n):
    def maior_divisivel(numero1, divisor):
        valor = (numero1 // divisor)
        resto = numero1 - (valor * divisor)
        return valor>0, valor, resto

    n = 87364681
    divisores = {'year': 31557600,'month': 2629800,'day':86400,'hour': 3600,'minute': 60, 'second': 1}

    textos = []

    for unidade, div in divisores.items():
        flag, val, n = maior_divisivel(n, div)
        if flag:
            if val>1:
                textos.append(f"{val} {unidade}s")
            else:
                textos.append(f"{val} {unidade}")
    frase_final = ""
    for i in range(len(textos)):
        
        if i +1 == len(textos) - 1:
            frase_final = frase_final + textos[i] + " and "
        elif i+1 == len(textos):
            frase_final = frase_final + textos[i]
        else:
            frase_final = frase_final + textos[i] + ", "
            
    return frase_final
```
"""
codigo_ex = """```python
formatDuration(62)   # "1 minute and 2 seconds"
formatDuration(3662) # "1 hour, 1 minute and 2 seconds"
```
"""

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🕰️✏️", className="header-emoji"),
                html.H1(
                    children='Desafio "tempo para texto"', className="header-title"
                ),
                html.P(
                    children=(
                        html.P("Esta página mostra o resultado de um desafio que resolvi.O objetivo do desafio é transformar um tempo dado em segundos para um formato amigável."),
                        html.P("Feito por: Lívia Sousa Alves (sousaalveslivia@gmail.com)")
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Tempo (em segundos)", className="menu-title"),
                        dcc.Input(id="num_input", 
                                  type="number",
                                  className="input",
                                  style={'font-size':20,'padding-left':10, 'padding-right':10},
                                  min = 0)]
                ),
                html.Div(
                    children=[
                        html.Button('Converter', id='button', n_clicks=0, className="botao"),
                    ],
                    style={'align-content': 'center', 'padding-bottom': 24}
                ),
            ],
            className="menu",
        ),
        html.Div(
            html.H2(id="frase", children="",className="result-text")
        ),
        
        html.Div(children=[
            html.Div(children=[
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            [
                                html.H3("Nota"),
                                html.P("A função deve aceitar um inteiro não negativo. Se é zero, ele só retorna a palavra now."),
                                html.P("Caso contrário, o retorno deve ser expresso como uma combinação de anos, meses, dias, horas, minutos e segundos em inglês."),
                                html.P("É importante separar as palavras e números por um espaço, para correta verificação da resposta."),
                                html.P("Caso alguma das unidades tenha valor zero, não deve aparecer no resultado. Ou seja, 1 minute and 0 seconds não é válido, sendo a resposta correta 1 minute."),
                                html.P("Considere que:"),
                                html.Ul(children=[
                                    html.Li("1 dia = 24 horas"),
                                    html.Li("1 mês = 30 dias"),
                                    html.Li("1 ano = 365 dias"),
                                ]),
                                html.H3("Código de exemplo"),
                                dcc.Markdown(codigo_ex, style={"backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),                                
                            ],
                            title="Detalhes do desafio",
                        ),
                    ],
                    start_collapsed=False
                ),],
                className="accordions"
            ),
            html.Div(children=[
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            [
                                dcc.Markdown(codigo, style={"backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
                            ],
                            title="Código (solução)",
                        ),
                    ],
                    start_collapsed=True
                ),],
                className="accordions"
            )
        ], className="details")
        ])



@app.callback(
    Output("frase", "children"),
    Input("button", "n_clicks"),
    State("num_input", "value"),
    prevent_initial_call = True
)
def update_graph(button, n):
    def maior_divisivel(numero1, divisor):
        valor = (numero1 // divisor)
        resto = numero1 - (valor * divisor)
        return valor>0, valor, resto

    divisores = {'year': 31557600,'month': 2629800,'day':86400,'hour': 3600,'minute': 60, 'second': 1}

    textos = []

    for unidade, div in divisores.items():
        flag, val, n = maior_divisivel(n, div)
        if flag:
            if val>1:
                textos.append(f"{val} {unidade}s")
            else:
                textos.append(f"{val} {unidade}")
    frase_final = ""
    for i in range(len(textos)):
        
        if i +1 == len(textos) - 1:
            frase_final = frase_final + textos[i] + " and "
        elif i+1 == len(textos):
            frase_final = frase_final + textos[i]
        else:
            frase_final = frase_final + textos[i] + ", "
            
    return frase_final

# Execução do servidor
if __name__ == "__main__":
    app.run_server(debug=True)