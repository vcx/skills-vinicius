---
name: skill-manager
description: >
    Gerencia o ciclo de vida de skills (criação, download, sincronização e organização)
    em múltiplos ambientes (Desktop, Notebook, Cloudtop, VM) e plataformas (Gemini CLI, 
    Claude Code, Antigravity, Jetski). Garante a conformidade com as políticas de 
    segurança, separando skills neutros no repositório 'skills' (pessoal) e skills 
    privados no repositório 'skills-google' (organização google-cloud).
---

# Skill Manager

Este skill automatiza a organização e sincronização de skills entre seus diversos ambientes de trabalho.

## Ambientes e Plataformas

| Plataforma | Caminho dos Skills |
| :--- | :--- |
| **Gemini CLI** | `~/.gemini/skills` |
| **Antigravity** | `~/.antigravity/skills` (link para `~/.gemini/skills`) |
| **Jetski** | `~/.jetski/skills` (link para `~/.gemini/skills`) |
| **Claude Code** | `~/.claude/skills` |

## Repositórios de Skills

- **Google** `github.com/vcx/skills-google` (use para skills que mencionam `google3`, `mcp-google`, ou ferramentas internas).
- **Para skills não-corporativos:** `github.com/vcx/skills-vinicius`

## Repositórios de Skills feitos por amigos

- **Anderson Duboc** `github.com/duboc/gemini-skills`

## Comandos e Workflows

### 1. Baixar um Skill
- "Baixe um skill sobre migração de aplicações"
    - o skill manager deve buscar nos meus skills, nos dois repositórios, se algum corresponde ao assunto "migração de aplicações". caso haja mais de um, pergunte qual.
    - caso eu não tenha o repo `skills-vinicius` clonado ainda, clone em ~/sources
- "Baixe o skill X do repositório do duboc"
    - o skill manager deve visitar a homepage ou dos amigos listados acima para procurar um sobre o assunto
    - para instalação, o skill manager deve seguir instruções que estão na página
    - o skill manager não pode buscar outros repos não listados acima

### 2. Salvar/Atualizar Skill no Repo Correto
- "Salve o skill {nome do skill} no meu repo de skills"
    - O skill manager deve analisar o conteúdo:
        - Se houver referências a `google3`, `citc`, `fig`, ou ferramentas internas do Google: `skills-google`.
        - Caso contrário: `skills-vinicius`.
    - o skill deve fazer um commit e push das alterações no repo correspondente

### 3. Sincronizar Ambientes
- "Sincroniza meus skills entre o cloudtop e o notebook"
    - O sincronismo, por padrão, é apenas entre skills que existem nos dois lados (por exemplo, existe localmente em .gemini/skills e no repo de destino). Caso o usuário peça, envie skills novos de um lado para outro
    - Por padrão, use apenas o comando `ls` para obter tamanho e datas dos arquivos pra saber se foram alterados. Se o usuário pedir explicitamente, use hashes.

## Regras de Organização

1. **Simetria de Links:** Sempre que possível, mantenha `~/.gemini/skills` como a fonte da verdade e crie links simbólicos para Antigravity e Jetski. Se estiver num computador Windows e não-WSL, os links não estão disponíveis. Nesse caso, copie os arquivos.
2. **Privacidade:** NUNCA submeta segredos ou código interno ao repositório pessoal `skills`.