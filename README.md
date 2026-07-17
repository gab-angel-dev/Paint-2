# Paint 2 — Sistema de Desenho 

Uma aplicação desktop interativa para criação, manipulação e persistência de formas geométricas vetoriais desenvolvida em Python. O projeto utiliza uma interface gráfica robusta construída sobre o ecossistema `tkinter` e implementa de forma rigorosa o padrão de arquitetura **MVC (Model-View-Controller)** junto com boas práticas de Programação Orientada a Objetos (Abstração, Herança e Polimorfismo).

---

## 👥 Equipe e Integrantes

* **Integrantes:**

  * Jorge Batista — 202600046073

  * Gabriel Angel — 202600045998

---

## 📝 Descrição do Sistema Documentado

O **Paint 2** é um software de desenho focado em renderização vetorial em tempo real. A separação clara de conceitos por meio da arquitetura MVC estrutura-se da seguinte forma:

* **Módulo Model (Dados e Formas):** Contém a estrutura de dados da aplicação (`Model`) responsável pelo histórico vetorial e pelas rotinas de persistência em arquivos binários compactos `.paint` através da serialização com a biblioteca `pickle`. Adicionalmente, possui o subsistema de geometria regido por uma classe abstrata (`Figuras`) e estendido por especializações concretas que encapsulam as regras matemáticas de redimensionamento e cálculo de vértices por translação trigonométrica.

* **Módulo View (Interface Gráfica):** Gerenciado pela classe `App` (derivada de `tk.Tk`), constrói uma janela otimizada de alta resolução contendo barras de menu personalizadas, seletores de cor interativos operados nativamente via `colorchooser` e uma superfície vetorial (`tk.Canvas`) responsável pelo redesenho otimizado da tela.

* **Módulo Controller (Fluxo de Eventos):** Centralizado na classe `Controller`, este componente gerencia o ciclo de vida das interações do usuário. Ele intercepta os estados do cursor do mouse no Canvas (`ButtonPress`, `B1-Motion`, `ButtonRelease`) para acionar o polimorfismo das figuras, orquestrar atualizações parciais (rascunhos provisórios) e consolidar os elementos no histórico definitivo.

---

## 📊 Métricas da Documentação

Abaixo estão descritas as métricas precisas coletadas a partir do mapeamento estático da árvore de código-fonte analisada:

* **Quantidade de Classes Documentadas:** `13`
  * `Model` (Gerenciador de dados)
  * `App` (Interface Gráfica / View)
  * `Controller` (Mediador de eventos)
  * `Figuras` (Superclasse Abstrata)
  * `Linha` (Especialização concreta)
  * `LinhaLivre` (Especialização concreta para rabiscos)
  * `Retangulo` (Especialização concreta)
  * `Oval` (Especialização concreta)
  * `Circulo` (Especialização concreta com restrição de raio equilátero)
  * `Poligono` (Especialização concreta para polígonos regulares de N lados)
  * `EstadoDesenho` (Superclasse Abstrata do padrão State)
  * `EstadoOcioso` (Estado concreto: aguardando início do desenho)
  * `EstadoDesenhando` (Estado concreto: figura em desenho/arrasto)

* **Quantidade de Métodos Documentados:** `37`

  * **Model:** `5` métodos (`__init__`, `adicionar_figura`, `get_figuras`, `limpar`, `salvar_arquivo`, `abrir_arquivo`).

  * **View (App):** `5` métodos (`__init__`, `construir_barra_menu`, `escolher_cor_borda`, `escolher_cor_preenchimento`, `redesenhar`).

  * **Controller:** `8` métodos (`__init__`, `iniciar`, `atualizar`, `incluir`, `salvar`, `abrir`, `pegar_figura_atual`, `aplicar_figura`).

  * **Figuras (Abstrata):** `4` métodos (`__init__`, `iniciar_figura`, `atualizar_figura`, `incompleta`).

  * **Formas Concretas (Especializações):** `11` métodos no total (distribuídos entre as inicializações, lógicas de arrasto, validações de tamanho zerado e o motor trigonométrico matemático `calcular_vertices` contido na classe `Poligono`).

  * **Estado (Padrão State):** `9` métodos no total (`iniciar`, `atualizar` e `incluir` implementados em cada uma das 3 classes: `EstadoDesenho`, `EstadoOcioso` e `EstadoDesenhando`).

---

## 🧩 Padrões de Projeto Aplicados

* **MVC (Model-View-Controller):** separação entre dados (`Model`), interface (`View`) e fluxo de eventos (`Controller`).
* **Strategy (implícito):** a hierarquia `Figuras` permite que cada tipo de forma (`Retangulo`, `Oval`, `Circulo`, `Poligono`, ...) implemente sua própria lógica de `iniciar_figura`/`atualizar_figura`, sendo usada de forma intercambiável pelo `Controller`.
* **State:** o `Controller` delega o tratamento dos eventos de mouse (`iniciar`, `atualizar`, `incluir`) ao objeto `self.estado` atual (`EstadoOcioso` ou `EstadoDesenhando`), eliminando verificações condicionais sobre a fase do desenho e tornando explícitas as transições entre "aguardando clique" e "desenhando".

---

## ▶️ Como Executar o Programa

O projeto utiliza apenas bibliotecas padrão do Python (`tkinter`, `pickle`), então não há dependências externas para instalar. Basta rodar a partir da raiz do projeto:

```zsh
python -m src.Paint_2.main
```

> Caso o comando acima retorne erro de módulo não encontrado, execute a partir da pasta raiz do projeto (onde está a pasta `src/`), garantindo que o Python reconheça os pacotes internos corretamente.

---

## 📚 Instruções para Visualizar a Documentação

A documentação do código foi extraída diretamente das *docstrings* estruturadas seguindo o padrão de documentação de APIs Python (equivalente ao Javadoc). Para gerá-la e visualizá-la localmente através de uma interface Web interativa gerada pelo `pdoc`, siga as etapas abaixo:

### 1. Preparação do Ambiente Virtual

```zsh
# Ative o ambiente virtual criado para o projeto
source venv/bin/activate

# Garanta que o gerador de documentação pdoc está instalado localmente
pip install pdoc
```

### 2. Geração da Documentação HTML

```zsh
# Gera a documentação HTML a partir do pacote principal do projeto
pdoc --output-dir docs src/Paint_2
```

Esse comando cria (ou atualiza) a pasta `docs/` na raiz do projeto, contendo todo o HTML navegável das classes documentadas.

### 3. Visualização da Documentação

```zsh
# Abre o documento principal gerado
xdg-open docs/index.html
```

---

## 🎨 Como Usar a Interface e o Programa

Ao iniciar o **Paint 2**, a interface gráfica será exibida com uma barra de ferramentas escura no topo (`barra_superior`) e uma grande área de desenho em branco (`canvas`). O fluxo de uso é intuitivo e segue os passos abaixo:

### 1. Desenhando Formas Geométricas

1. **Selecione a Forma:** No primeiro menu suspenso (que inicia com o texto *"Formas"*), escolha a figura que deseja desenhar: `Linha`, `Rabisco`, `Retângulo`, `Oval`, `Círculo` ou `Poligono`.

2. **Defina a Quantidade de Lados (Apenas para Polígono):** Se você escolheu a opção *Poligono*, utilize o seletor numérico (*Spinbox*) ao lado do menu de ferramentas para definir quantos lados a figura terá (valores aceitos entre 3 e 20).

3. **Desenhe no Canvas:**

    Clique com o **botão esquerdo do mouse** no Canvas e mantenha-o pressionado para definir o ponto inicial.

    **Arraste o mouse** para expandir a figura. O sistema exibirá um rascunho com linhas tracejadas em tempo real.
    
   **Solte o botão do mouse** para consolidar o desenho na tela.

### 2. Customizando Cores

Você pode alterar o estilo visual das próximas figuras que serão desenhadas utilizando os seletores de cores:

* **Botão "Cor da Borda":** Abre uma paleta gráfica. Escolha a cor do contorno da forma. O fundo do próprio botão mudará para a cor selecionada como confirmação visual.

* **Botão "Cor Preenchimento":** Abre a paleta para selecionar a cor interna que preencherá formas fechadas (como Círculos, Retângulos e Polígonos).

### 3. Utilizando Ferramentas Auxiliares

* No menu suspenso **"Ferramenta"**, você pode selecionar recursos extras como a **Borracha** para auxiliar na edição da sua área de desenho.

### 4. Salvando e Abrindo Projetos (Persistência)

O Paint 2 permite que você guarde o seu progresso para continuar trabalhando depois:

* **Botão Salvar:** Localizado no canto superior direito. Abre uma janela do sistema para você escolher uma pasta e dar um nome ao arquivo. O projeto será salvo com a extensão exclusiva `.paint`.

* **Botão Abrir:** Localizado ao lado do botão salvar. Permite buscar um arquivo `.paint` gravado anteriormente no seu computador para carregar todo o histórico de desenhos de volta para a tela.