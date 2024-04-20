  document.getElementById('buildBtn').addEventListener('click', function() {
    const startStation = document.getElementById('Start station').value;
    const endStation = document.getElementById('End station').value;
    if (!startStation || !endStation) {
      alert('Пожалуйста, выберите станции отправления и прибытия.');
      return;
    }
    
    const apiKey = 'AQVN3FCrWyj6C_toFKyu0i5TMdYrjuotwTIveP-a';
    const query = `Как доехать от станции $\{Start station\} до станции $\{End station\}?`;
    
    fetch('https://llm.api.cloud.yandex.net/foundationModels/v1/completion', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer $\{apiKey\}`
      },
      body: JSON.stringify({
        prompt: query,
        maxTokens: 100,
        temperature: 1,
      })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('routeResult').innerText = data.choices[0].text;
    })
    .catch(error => {
      console.error('Ошибка:', error);
      document.getElementById('routeResult').innerText = 'Произошла ошибка при получении данных.';
    });
  });