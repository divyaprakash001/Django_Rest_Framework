// const res = fetch('http://127.0.0.1:8000/api/studentApi/')
//   .then((response) => {
//     // Log the entire headers object to the console
//     console.log(response);

//     // Get the 'date' header value directly
//     const dateValue = response.headers.get('date');
//     const dataServer = response.headers.get('server');

//     // Log the value of the 'date' header
//     console.log(dateValue);  // This will give you the value like 'Wed, 04 Dec 2024 07:01:32 GMT'
//     console.log(dataServer);  // This will give you the value like 'Wed, 04 Dec 2024 07:01:32 GMT'
//   })
//   .catch((err) => {
//     console.log("error", err);
//   });

// Retrieve all students (GET request)
// const id = 1;
// fetch(`http://127.0.0.1:8000/api/studentApi/${id}`)
//   .then(response => response.json())
//   .then(data => {
//     console.log('All students:', data);
//   })
//   .catch(error => console.error('Error fetching all students:', error));

document.querySelector('.create').addEventListener("click", function () {
  console.log('created');
  const newStudent = {
    name: 'Johny Kishan',
    roll: 22,
    city: 'Arrah',
  };
  json_data = JSON.stringify(newStudent)

  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 8bc84a92d3ad7adc9ed62f82458423ba25502626'
  }

  fetch('http://127.0.0.1:8000/api/studentapi/', {
    method: 'POST', headers: headers, body: json_data,
  })
    .then(response => response.json())
    .then(data => {
      console.log('New student created:', data);
    })
    .catch(error => console.error('Error creating student:', error));


})



document.addEventListener("DOMContentLoaded", function () {

  const table = document.querySelector('table')

  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 8bc84a92d3ad7adc9ed62f82458423ba25502626'
  };

  fetch('http://127.0.0.1:8000/api/studentapi/', {
    method: 'GET',
    headers: headers
  })
    .then(response => {
      if (!response) {
        throw new Error('Network response was not ok')
      }
      return response.json();
    })
    .then(data => {
      data.forEach(item => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
        <td>${item.id}</td>
        <td>${item.name}</td>
        <td>${item.roll}</td>
        <td>${item.city}</td>
        <td data-id="${item.id}"><button>Edit</button>&nbsp;&nbsp;&nbsp;<button>Delete</button></td>`
        table.appendChild(tr)
      });

      document.querySelectorAll('tr').forEach((element) => {
        element.addEventListener("click", function (event) {
          if (event.target.innerText == 'Edit') {
            const newStudent = {
              name: 'Johny Kishan',
              roll: 22,
              city: 'Arrah',
            };
            json_data = JSON.stringify(newStudent)
            const id = event.target.parentElement.getAttribute('data-id');
            fetch(`http://127.0.0.1:8000/api/studentapi/${id}/`, {
              method: 'PUT',
              headers: headers,
              body: json_data
            })
          }
          else if (event.target.innerText == 'Delete') {
            const id = event.target.parentElement.getAttribute('data-id');
            fetch(`http://127.0.0.1:8000/api/studentapi/${id}`, {
              method: 'DELETE',
              headers: headers
            })
          }

        })
      })

    })
    .catch(error => console.error('Error creating student:', error));




})