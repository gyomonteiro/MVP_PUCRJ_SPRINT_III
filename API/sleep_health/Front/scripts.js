// URL base da API (ajuste conforme necessário)
const API_BASE_URL = 'http://127.0.0.1:5000';

// Função para obter a lista existente do servidor via requisição GET
const getList = () => {
    fetch(`${API_BASE_URL}/pessoas`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        data.pessoas.forEach(item => {
            insertList(
                item.person_id,
                item.gender,
                item.age,
                item.sleep_duration,
                item.quality_sleep,
                item.activity_level,
                item.stress_level,
                item.bmi_category,
                item.blood_pressure,
                item.heart_rate,
                item.daily_steps,
                item.outcome
            );
        });
    })
    .catch(error => {
        console.error('Erro ao obter a lista:', error);
    });
};

// Chamada da função para carregamento inicial dos dados
getList();

// Função para adicionar um novo paciente e diagnosticar
const newItem = () => {
    // Obtenção dos valores dos campos do formulário
    let patientData = {
        person_id: document.getElementById('newPersonID').value.trim(),
        gender: document.getElementById('newGender').value,
        age: document.getElementById('newAge').value.trim(),
        sleep_duration: document.getElementById('newDuration').value.trim(),
        quality_sleep: document.getElementById('newQuality').value.trim(),
        activity_level: document.getElementById('newLevelActivity').value.trim(),
        stress_level: document.getElementById('newLevelStress').value.trim(),
        bmi_category: document.getElementById('newBMI').value,
        blood_pressure: document.getElementById('newPressure').value.trim(),
        heart_rate: document.getElementById('newHeartRate').value.trim(),
        daily_steps: document.getElementById('newDailySteps').value.trim()
    };

    // Validação dos campos
    if (!validateForm(patientData)) {
        return;
    }

    // Envio dos dados para a API para obter o diagnóstico
    fetch(`${API_BASE_URL}/pessoa`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(patientData)
    })
    .then(response => response.json())
    .then(data => {
        // Adiciona o resultado na tabela
        insertList(
            patientData.person_id,
            patientData.gender,
            patientData.age,
            patientData.sleep_duration,
            patientData.quality_sleep,
            patientData.activity_level,
            patientData.stress_level,
            patientData.bmi_category,
            patientData.blood_pressure,
            patientData.heart_rate,
            patientData.daily_steps,
            data.outcome
        );
        // Limpa o formulário após o diagnóstico
        document.getElementById('patientForm').reset();
    })
    .catch(error => {
        console.error('Erro ao diagnosticar:', error);
        alert('Ocorreu um erro ao processar o diagnóstico.');
    });
};


const fieldIdMap = {
    person_id: 'newPersonID',
    gender: 'newGender',
    age: 'newAge',
    sleep_duration: 'newDuration',
    quality_sleep: 'newQuality',
    activity_level: 'newLevelActivity',
    stress_level: 'newLevelStress',
    bmi_category: 'newBMI',
    blood_pressure: 'newPressure',
    heart_rate: 'newHeartRate',
    daily_steps: 'newDailySteps'
};


// Função para validar o formulário
const validateForm = (data) => {
    let isValid = true;

    // Validação básica usando o mapeamento
    for (let key in data) {
        const elementId = fieldIdMap[key];
        const element = document.getElementById(elementId);
        
        if (data[key] === '' || data[key] === null || data[key] === undefined) {
            console.log(`Campo ${key} é inválido`);
            isValid = false;
            // Adiciona classe de erro
            element.classList.add('is-invalid');
        } else {
            // Remove classe de erro caso exista
            element.classList.remove('is-invalid');
        }
    }

    if (!isValid) {
        alert('Por favor, preencha todos os campos corretamente.');
    }

    return isValid;
};


// Função para capitalizar a primeira letra de uma string
const capitalizeFirstLetter = (string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
};

// Função para adicionar os dados e o diagnóstico à tabela
const insertList = (person_id, gender, age, sleep_duration, quality_sleep, activity_level, stress_level, bmi_category, blood_pressure, heart_rate, daily_steps, outcome) => {
    const tableBody = document.querySelector('#myTable tbody');

    // Cria uma nova linha
    let newRow = tableBody.insertRow();

    // Adiciona as células com os dados do paciente
    newRow.insertCell(0).innerText = person_id;
    newRow.insertCell(1).innerText = gender === '1' ? 'Feminino' : 'Masculino';
    newRow.insertCell(2).innerText = age;
    newRow.insertCell(3).innerText = sleep_duration;
    newRow.insertCell(4).innerText = quality_sleep;
    newRow.insertCell(5).innerText = activity_level;
    newRow.insertCell(6).innerText = stress_level;
    newRow.insertCell(7).innerText = getBMICategory(bmi_category);
    newRow.insertCell(8).innerText = blood_pressure;
    newRow.insertCell(9).innerText = heart_rate;
    newRow.insertCell(10).innerText = daily_steps;
    newRow.insertCell(11).innerText = getDiagnosisText(outcome);

    // Ações (botão para remover)
    let actionCell = newRow.insertCell(12);
    let deleteBtn = document.createElement('button');
    deleteBtn.className = 'btn btn-sm btn-danger';
    deleteBtn.innerText = 'Remover';
    deleteBtn.onclick = function() {
        if (confirm('Você tem certeza que deseja remover este paciente?')) {
            deleteItem(person_id);
            tableBody.deleteRow(newRow.rowIndex - 1);
        }
    };
    actionCell.appendChild(deleteBtn);
};


// Função para converter o valor do IMC em texto
const getBMICategory = (value) => {
    const category = Number(value); 
    switch (category) {
        case 1:
            return 'Normal';
        case 2:
            return 'Sobrepeso';
        case 3:
            return 'Obesidade';
        case 4:
            return 'Obesidade Severa';
        default:
            return 'Desconhecido';
    }
};



// Função para converter o diagnóstico em texto
const getDiagnosisText = (value) => {
    switch(value) {
        case 0:
            return 'Nenhum';
        case 1:
            return 'Insônia/Apneia do Sono';
        default:
            return 'Desconhecido';
    }
};

// Função para deletar um paciente da lista do servidor via requisição DELETE
const deleteItem = (person_id) => {
    fetch(`${API_BASE_URL}/pessoa?person_id=${person_id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert('Paciente removido com sucesso!');
    })
    .catch(error => {
        console.error('Erro ao remover o paciente:', error);
    });
};
