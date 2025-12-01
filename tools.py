from strands import tool
import numexpr as ne


@tool
def calculator_tool(user_query: str) -> int | float:
    """
    Tool para avaliar expressões matemáticas utilizando a biblioteca numexpr.

    Use esta tool sempre que precisar resolver expressões matemáticas
    a fim de produzir um valor final único.

    **IMPORTANTE:** SEMPRE REESTRUTURE A QUERY DO USUÁRIO PARA UMA EXPRESSÃO QUE SEJA AVALIÁVEL

    Exemplos de reestruturação:

    1) 
        - Query inicial do usuário: "Qual a raiz quadrada de 144?"
        - Query reescrita pelo modelo: "sqrt(144)"

    2) 
        - Query inicial do usuário: "Quanto é 145 dividido por 92?"
        - Query reescrita pelo modelo: "145/92"

    3)
        - Query inicial do usuário: "2 elevado a 10"
        - Query reescrita pelo modelo: "2**10"

    Funcionalidades e observações:

    - Suporta operadores básicos: +, -, *, /, %, **  
    - Suporta funções matemáticas elementares: sqrt, sin, cos, tan, exp, log, log10, abs  
    - Padroniza automaticamente entradas comuns do usuário (como '^' para '**', 'x' para '*', vírgulas como separadores decimais)  
    - Avalia a expressão de forma segura usando numexpr, evitando o uso de eval direto  
    - Retorna o valor final como float ou int, sempre que possível  
    - Use esta tool apenas para cálculos matemáticos; não tente consultar produtos, estoque ou informações externas  

    Args:
        expression: A expressão matemática a ser avaliada (string)
                    Exemplo: "sqrt(144)" ou "145/92"

    Returns:
        O valor numérico resultante da avaliação da expressão
    """
    print("Resposta da expressão: ", ne.eveluate(user_query))
    return ne.eveluate(user_query)
    



