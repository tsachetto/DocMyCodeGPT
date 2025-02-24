"""
DocMyCodeGPT - Gerador de Documentação Técnica em PDF
Versão 3.1 - PDF Completo
"""

import argparseQ
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Tuple, List

from openai import OpenAI, APITimeoutError
from dotenv import load_dotenv
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    ListFlowable,
    ListItem,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors

# Configuração de ambiente
load_dotenv()
console = Console()
version = '1.0b' #Sempre atualizar a versão em casos de grandes modificações

# ====================== Configuração de Estilos ======================
def configure_styles():
    """Configura estilos customizados para o PDF"""
    styles = getSampleStyleSheet()

    custom_styles = [
        {
            "name": "TitleStyle",
            "fontSize": 16,
            "leading": 20,
            "alignment": TA_CENTER,
            "textColor": colors.HexColor("#2B3A55"),
            "fontName": "Helvetica-Bold",
        },
        {
            "name": "HeaderStyle",
            "fontSize": 10,
            "textColor": colors.HexColor("#666666"),
            "alignment": TA_LEFT,
        },
        {
            "name": "SectionTitle",
            "fontSize": 12,
            "leading": 14,
            "textColor": colors.HexColor("#2B3A55"),
            "spaceAfter": 6,
            "fontName": "Helvetica-Bold",
        },
        {
            "name": "CustomBullet",
            "fontSize": 10,
            "leading": 12,
            "leftIndent": 20,
            "spaceAfter": 4,
            "bulletFontName": "Helvetica-Bold",
            "bulletFontSize": 10,
        },
    ]

    for style in custom_styles:
        if not hasattr(styles, style["name"]):
            styles.add(ParagraphStyle(**style))

    return styles

# ====================== Processamento de Argumentos ======================
def process_args() -> Tuple[Path, Path]:
    """Processa e valida argumentos da linha de comando"""
    parser = argparse.ArgumentParser(
        prog="DocMyCodeGPT",
        description="Gera documentação técnica em PDF para arquivos de código fonte",
        epilog="Exemplo: python docmycodegpt.py meu_codigo.py -o ./docs",
    )

    parser.add_argument(
        "codefile",
        type=str,
        help="Caminho para o arquivo de código a ser analisado",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Diretório de saída para o documento PDF",
    )

    args = parser.parse_args()

    # Validação do arquivo de entrada
    code_path = Path(args.codefile).resolve()
    if not code_path.exists():
        console.print(f"[bold red]Erro: Arquivo não encontrado: {code_path}[/]")
        sys.exit(1)

    # Cria diretório de saída se necessário
    output_dir = Path(args.output).resolve() if args.output else code_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    return code_path, output_dir

# ====================== Análise com OpenAI ======================
def analyze_code(code_content: str, api_key: str) -> str:
    """Obtém análise do código usando OpenAI API"""
    client = OpenAI(api_key=api_key)

    system_prompt = """Você é um engenheiro de software sênior especializado em análise de código e documentação técnica. 
    Sua análise deve ser estruturada, técnica e completa."""

    user_prompt = f"""Analise o seguinte código e gere um relatório técnico detalhado (pt-br) em markdown seguindo esta exata estrutura:

    ## 1. Visão Geral

    - Objetivo principal:
    
    - Contexto de uso e aplicações:
    
    - Arquitetura geral:

    ## 2. Funcionamento Técnico

    - Fluxo de execução: (narre um passo a passo do funcionamento em até 300 palavras)

    - Estruturas de dados: (explique a estruturação do código)

    - Principais Componentes e Subcomponentes:

    ## 3. Ambiente e Dependências
    
    - Linguagem e versão:
    
    - Bibliotecas essenciais e requisitos: (descreve brevemente cada uma e sua aplicação)

    ## 4. Análise Crítica
    
    ### Destaques
    
    - Lista de aspectos positivos:
    
    ### Vulnerabilidades
    
    - Possíveis riscos e vulnerabilidades:
    
    ### Recomendações
    
    - Sugestões de melhorias: (informe dicas e truques para aperfeiçoamento e melhoria do código)

    ## 5. Conclusão
    
    - Avaliação geral: (report técnico abrangente e bem explicado contendo entre 150 e 300 palavras)
    
    - Considerações finais:

    
    Formato requerido:
    - Títulos com ##/### 
    - Listas com marcadores
    - Sem formatação extra
    
    Código a analisar:
    ```{code_content}```"""

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task("Analisando código...", total=1)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.3,
                max_tokens=2000,
                top_p=0.95,
                timeout=30,
            )

            progress.update(task, advance=1)
            return response.choices[0].message.content

    except Exception as e:
        console.print(f"[bold red]Erro na análise:[/] {str(e)}")
        sys.exit(1)

# ====================== Geração do PDF ======================
def create_pdf_document(analysis: str, output_path: Path, code_filename: str):
    """Gera documento PDF profissional com a análise"""
    styles = configure_styles()
    
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
    )

    elements = []

    # Cabeçalho
    elements.append(Paragraph(f"DocMyCodeGPT - Relatório Técnico - Versão {version}", styles["TitleStyle"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Arquivo analisado: {code_filename}", styles["HeaderStyle"]))
    elements.append(Paragraph(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", styles["HeaderStyle"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(" "))
    elements.append(Paragraph(" "))
    elements.append(Paragraph(" "))
    #elements.append(PageBreak())

    # Processamento do conteúdo
    current_list = []
    for line in analysis.split("\n"):
        line = line.strip()

        if line.startswith("## "):
            if current_list:
                elements.append(ListFlowable(current_list, bulletType="bullet"))
                current_list = []
                elements.append(Spacer(1, 12))
            
            title = line[3:].strip()
            elements.append(Paragraph(title, styles["SectionTitle"]))
            elements.append(Spacer(1, 8))

        elif line.startswith("### "):
            if current_list:
                elements.append(ListFlowable(current_list, bulletType="bullet"))
                current_list = []
            
            subtitle = line[4:].strip()
            elements.append(Paragraph(subtitle, styles["Heading3"]))
            elements.append(Spacer(1, 6))

        elif line.startswith("- "):
            current_list.append(ListItem(Paragraph(line[2:].strip(), styles["CustomBullet"])))

        elif line:
            if current_list:
                elements.append(ListFlowable(current_list, bulletType="bullet"))
                current_list = []
            elements.append(Paragraph(line, styles["Normal"]))
            elements.append(Spacer(1, 4))

    if current_list:
        elements.append(ListFlowable(current_list, bulletType="bullet"))

    doc.build(elements)

# ====================== Fluxo Principal ======================
def main():
    """Fluxo principal de execução"""
    code_path, output_dir = process_args()

    try:
        # Carregar conteúdo do código
        with console.status("[bold green]Lendo arquivo...[/]", spinner="dots"):
            code_content = code_path.read_text(encoding="utf-8")

        # Validar API Key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not api_key.startswith("sk-"):
            console.print("[bold red]Erro: Chave API inválida ou não configurada[/]")
            sys.exit(1)

        # Gerar análise
        analysis = analyze_code(code_content, api_key)

        # Criar nome do arquivo de saída
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{code_path.stem}_analysis_{timestamp}.pdf"
        output_path = output_dir / output_filename

        # Gerar PDF
        with console.status("[bold green]Gerando PDF...[/]", spinner="dots"):
            create_pdf_document(analysis, output_path, code_path.name)

        console.print(f"\n[bold green]✓ Documento gerado com sucesso:[/]\n[cyan]{output_path}[/]")

    except Exception as e:
        console.print(f"[bold red]Erro fatal:[/] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
