const res = fetch('http://127.0.0.1:8000/api/allStudents/')
  .then((response) => {
    // Log the entire headers object to the console
    console.log(response.headers);

    // Get the 'date' header value directly
    const dateValue = response.headers.get('date');
    const dataServer = response.headers.get('server');

    // Log the value of the 'date' header
    console.log(dateValue);  // This will give you the value like 'Wed, 04 Dec 2024 07:01:32 GMT'
    console.log(dataServer);  // This will give you the value like 'Wed, 04 Dec 2024 07:01:32 GMT'
  })
  .catch((err) => {
    console.log("error", err);
  });
