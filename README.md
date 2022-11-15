## Instruções para merge com a main

Primeiro passo é criar um **pull request** da sua branch para main, que pode ser feito pela interface do github mesmo.

Após isso é importante que você atualize sua branch com a main, para garantir que nenhum dado seja perdido, você pode usar os comandos abaixo para isso.

```bash
# entra na sua branch
git checkout <sua_branch>

# Atualiza sua branch com base na main
git merge main

# Adiciona as alterações e sobe elas
git add .

git commit -m"<sua_mensagem>"

git push
```

> **Warning**
> Pode ser que tenha conflitos, nesse caso é importante tomar cuidado para não sobrescrever dados importantes