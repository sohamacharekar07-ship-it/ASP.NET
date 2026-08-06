a. Create an HTML page that would be the starting point of the application. This HTML will contain a link to the file named manifest.json. This is an important file that would be created in the next step. 
CODE:
Student.cs
namespace StudentPWA.Models
{
    public class Student
    {
        public int RollNo { get; set; }

        public string Name { get; set; }
    }
}
StudentControler.cs
using Microsoft.AspNetCore.Mvc;
namespace StudentPWA.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class StudentController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok(new
            {
                RollNo = 101,
                Name = "Soham Acharekar"
            });
        }
    }
}
Index.cshtml
<h2>Student Record</h2>
<button onclick="loadStudent()">Load Student</button>
<p id="data"></p>
<script>
	function loadStudent() {
		fetch("/api/student")
			.then(response => response.json())
			.then(student => {
				document.getElementById("data").innerHTML =
					"Roll No : " + student.rollNo +
					"<br>Name : " + student.name;
			});
	}
</script>
manifest.json
{
  "name": "Student PWA",
  "short_name": "Student",
  "start_url": "/",
  "display": "standalone"
}
_Layout.cshtml
<head>
<link rel="manifest" href="/manifest.json">
</head>
OUTPUT:


b. Create a simple Web API that returns Student data in JSON format.
CODE:
Student.cs
namespace StudentPWA.Models
{
    public class Student
    {
        public int RollNo { get; set; }

        public string Name { get; set; }
    }
}
StudentController.cs
using Microsoft.AspNetCore.Mvc;
namespace StudentPWA.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class StudentController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok(new
            {
                RollNo = 101,
                Name = "Soham Acharekar"
            });
        }
    }
}
OUTPUT:

