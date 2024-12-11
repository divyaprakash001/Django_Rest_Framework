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



const newStudent = {
  name: 'John Doe',
  roll: 22,
  city: 'A',
  // Add any other required fields
};
json_data = JSON.stringify(newStudent)

headers = { 'Content-Type': 'application/json' }
fetch('http://127.0.0.1:8000/api/studentApi/', {
  method: 'POST', headers: headers, body: json_data,
})
  .then(response => response.json())
  .then(data => {
    console.log('New student created:', data);
  })
  .catch(error => console.error('Error creating student:', error));
