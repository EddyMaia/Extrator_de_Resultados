import flet as ft
from extracao import Extracao

def main(pagina: ft.Page):
    pagina.title="Extração de concursos"
    pagina.bgcolor='#3b2e2a'
    

    def iniciar_extracao(e):
    #valida os dados, instancia a classe e executa seus metodos
        jogo=dp_modo_jogo.value
        inicio=int(txtf_concurso_inicio.value)
        final=int(txtf_concurso_final.value)
        pagina.clean()
        pagina.add(ft.Text(value="EXTRAÇÃO INICIADA",color="red"))
        pagina.update()
        instancia_extrair=Extracao()
        instancia_extrair.definir_navegador(jogo)
        for concurso in range(inicio,final+1):
            instancia_extrair.buscar_concursos(concurso)
        pagina.clean()
        pagina.add(ft.Text(value="EXTRAÇÃO FINALIZADA COM SUCESSO!",color="green"))
        pagina.update()
        
#-------------------------------Elementos da pagina---------------------------------------------------
    dp_modo_jogo=ft.Dropdown(
        label="modo de jogo",
        options=[
            ft.dropdown.Option("Lotofacil"),
            ft.dropdown.Option("Mega-Sena"),
            ft.dropdown.Option("Lotomania")])

    txtf_concurso_inicio=ft.TextField(
        label="buscar a partir de:",hint_text="Em qual concurso devo iniciar",text_align=ft.TextAlign.CENTER)
    txtf_concurso_final=ft.TextField(
        label="buscar até:",hint_text="Até qual concurso devo consultar", text_align=ft.TextAlign.CENTER)
    btn_iniciar_extracao= ft.ElevatedButton("Iniciar Extração", on_click=iniciar_extracao)
    
#-------------------------------------Construção da página--------------------------------------------------
    pagina.add(
        dp_modo_jogo,txtf_concurso_inicio,txtf_concurso_final,btn_iniciar_extracao)


#executa o app e sua pagina inicial
ft.app(target=main)



