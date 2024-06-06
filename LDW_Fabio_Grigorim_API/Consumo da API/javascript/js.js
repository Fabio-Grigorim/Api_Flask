// Utilizando o AXIOS
// Capturar o botão de cadastrar
const createBtn = document.getElementById("createBtn")
// Escuta ao evento de click do usuário no botão
createBtn.addEventListener('click', createPet)

// Capturar o botão de alterar
const updateBtn = document.getElementById("updateBtn")
updateBtn.addEventListener('click', updatePet)

// Enviando uma requisição GET para listar todos os pets

axios.get("http://localhost:5000/pet").then(response => {
    const pets = response.data
    const listPets = document.getElementById('pets')
    pets.forEach(pet => {
        let item = document.createElement("li")
        // Setando o atributo ID para cada pet
        item.setAttribute("data-id", pet._id)
        item.setAttribute("data-nomePet", pet.nomePet)
        item.setAttribute("data-nomeTutor", pet.nomeTutor)
        item.setAttribute("data-diaBanho", pet.diaBanho)
        const id = listPets.getAttribute("data-id")

        item.innerHTML = `<h4>${pet.nomePet}</h4>
        <p>Nome do Tutor: ${pet.nomeTutor}</p>
        <p>Dia do Banho: ${ pet.diaBanho}</p>
        <p>ID: ${pet._id}</p>`

        var deleteBtn = document.createElement("button")
        deleteBtn.innerHTML = "Deletar"
        deleteBtn.classList.add("btn", "btn-danger", "mb-3", "mx-2")
        deleteBtn.addEventListener("click", () => {
            deletePet(item)
          })

        var editBtn = document.createElement("button")
        editBtn.innerHTML = "Editar"
        editBtn.classList.add("btn", "btn-warning", "mb-3", "mx-2")
        editBtn.addEventListener("click", () =>{
            loadForm(item)
        })

        item.appendChild(deleteBtn)
        item.appendChild(editBtn)
        listPets.appendChild(item)
    })
})

// Função para DELETAR 
function deletePet(listItem) {
    const id = listItem.getAttribute("data-id")
    axios.delete(`http://localhost:5000/pet/${id}`).then(response => {
        alert("Pet deletado!")
        location.reload()
    }).catch(err => {
        console.log(err)
    })
}

// Função para Cadastrar 
function createPet(){
    const form = document.getElementById('createForm')
    form.addEventListener("submit", function(event){
        event.preventDefault()
    })

    const nomePetInput = document.getElementById('nomePet')
    const nomeTutorInput = document.getElementById('nomeTutor')
    const diaBanhoInput = document.getElementById('diaBanho')

    const pet = {
        nomePet: nomePetInput.value,
        nomeTutor: nomeTutorInput.value,
        diaBanho: diaBanhoInput.value
    }
    axios.post("http://localhost:5000/pet", pet).then(response => {
        if(response.status == 201){
            alert("Pet cadastrado com sucesso!")
            location.reload()
        }
    }).catch(error=>{
        console.log(error)
    })
}

// Função para carregar o formulário de edição
function loadForm(listItem){
    const id = listItem.getAttribute("data-id")
    const nomePet = listItem.getAttribute("data-nomePet")
    const diaBanho = listItem.getAttribute("data-diaBanho")
    const nomeTutor = listItem.getAttribute("data-nomeTutor")

    document.getElementById("idEdit").value = id
    document.getElementById("nomePetEdit").value = nomePet
    document.getElementById("diaBanhoEdit").value = diaBanho
    document.getElementById("nomeTutorEdit").value = nomeTutor
}

// Função para alterar 
function updatePet(){
    const form = document.getElementById('editForm')
    form.addEventListener("submit", function(event){
        event.preventDefault()
    })

    const idInput = document.getElementById('idEdit')
    const nomePetInput = document.getElementById('nomePetEdit')    
    const diaBanhoInput = document.getElementById('diaBanhoEdit')
    const nomeTutorInput = document.getElementById('nomeTutorEdit')

    const pet = {
        nomePet: nomePetInput.value,        
        diaBanho: diaBanhoInput.value,
        nomeTutor: nomeTutorInput.value
    }

    var id = idInput.value

    axios.put(`http://localhost:5000/pet/${id}`, pet).then(response => {
        alert("Pet atualizado com sucesso!")
        location.reload()
    }).catch(error => {
        console.log(error)
    })
}
