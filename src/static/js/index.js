const selectEstado = document.getElementById('estado');
    const selectCidade = document.getElementById('cidade');

    selectEstado.addEventListener('change', () => {
      const uf = selectEstado.value;
      selectCidade.innerHTML = '<option>Carregando...</option>';

      if (uf) {
        fetch(`/api/cidades/${uf}`)
          .then(response => response.json())
          .then(cidades => {
            selectCidade.innerHTML = '<option value="">Selecione uma cidade</option>';
            cidades.forEach(cidade => {
              const option = document.createElement('option');
              option.value = cidade;
              option.textContent = cidade;
              selectCidade.appendChild(option);
            });
          })
          .catch(() => {
            selectCidade.innerHTML = '<option value="">Erro ao carregar cidades</option>';
          });
      } else {
        selectCidade.innerHTML = '<option value="">Selecione uma cidade</option>';
      }
    });